#!/usr/bin/env python3

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "xiaohongshu-carousel"
ASSET_DIR = SKILL_DIR / "assets"
THEMES_DIR = ASSET_DIR / "themes"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def escape_text(value: str) -> str:
    return html.escape(value, quote=True)


def with_breaks(value: str) -> str:
    return "<br />".join(escape_text(part) for part in value.split("\n"))


def paragraph(value: str, class_name: str) -> str:
    return f'<p class="{class_name}">{with_breaks(value)}</p>'


def bullet_list(items: list[str], class_name: str) -> str:
    if not items:
        return ""
    rendered = "".join(f"<li>{with_breaks(item)}</li>" for item in items)
    return f'<ul class="{class_name}">{rendered}</ul>'


def render_inline_markdown(text: str) -> str:
    escaped = escape_text(text)
    escaped = re.sub(r"`([^`]+)`", lambda m: f"<code>{m.group(1)}</code>", escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{escape_text(m.group(2))}" target="_blank" rel="noreferrer">{m.group(1)}</a>',
        escaped,
    )
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def normalize_title(value: str) -> str:
    return value.replace(" // ", "\n").strip()


def render_markdown_html(text: str) -> str:
    lines = text.splitlines()
    html_parts: list[str] = []
    index = 0

    def collect_list(start: int, ordered: bool) -> tuple[str, int]:
        tag = "ol" if ordered else "ul"
        items: list[str] = []
        cursor = start
        pattern = r"^\d+\.\s+" if ordered else r"^-\s+"
        while cursor < len(lines):
            stripped = lines[cursor].strip()
            if not stripped:
                break
            if not re.match(pattern, stripped):
                break
            item_text = re.sub(pattern, "", stripped, count=1)
            items.append(f"<li>{render_inline_markdown(item_text)}</li>")
            cursor += 1
        return f'<{tag} class="md-list">{"".join(items)}</{tag}>', cursor

    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()
        if not stripped:
            index += 1
            continue
        if stripped.startswith("```"):
            index += 1
            code_lines: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            code = escape_text("\n".join(code_lines).strip("\n"))
            html_parts.append(f'<pre class="md-code"><code>{code}</code></pre>')
            continue
        if stripped.startswith("### "):
            html_parts.append(f'<h3 class="md-h3">{render_inline_markdown(stripped[4:])}</h3>')
            index += 1
            continue
        if stripped.startswith("## "):
            html_parts.append(f'<h2 class="md-h2">{render_inline_markdown(stripped[3:])}</h2>')
            index += 1
            continue
        if re.match(r"^\d+\.\s+", stripped):
            rendered, index = collect_list(index, ordered=True)
            html_parts.append(rendered)
            continue
        if stripped.startswith("- "):
            rendered, index = collect_list(index, ordered=False)
            html_parts.append(rendered)
            continue

        paragraph_lines = [render_inline_markdown(stripped)]
        index += 1
        while index < len(lines):
            next_stripped = lines[index].strip()
            if not next_stripped:
                break
            if next_stripped.startswith(("## ", "### ", "```", "- ")) or re.match(r"^\d+\.\s+", next_stripped):
                break
            paragraph_lines.append(render_inline_markdown(next_stripped))
            index += 1
        html_parts.append(f'<p class="md-p">{"<br />".join(paragraph_lines)}</p>')

    return "".join(html_parts)


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    raw = text[4:end]
    body = text[end + 5 :]
    meta: dict[str, Any] = {}
    lines = raw.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            index += 1
            continue
        if ":" not in line:
            index += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value:
            meta[key] = value
            index += 1
            continue

        items: list[str] = []
        index += 1
        while index < len(lines):
            current = lines[index].strip()
            if not current:
                index += 1
                continue
            if current.startswith("- "):
                items.append(current[2:].strip())
                index += 1
                continue
            break
        meta[key] = items
    return meta, body


def append_meta(meta: dict[str, Any], key: str, value: str) -> None:
    if key in meta:
        current = meta[key]
        if isinstance(current, list):
            current.append(value)
        else:
            meta[key] = [current, value]
        return
    meta[key] = value


def meta_list(meta: dict[str, Any], key: str) -> list[str]:
    value = meta.get(key)
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def meta_value(meta: dict[str, Any], key: str, default: str = "") -> str:
    value = meta.get(key, default)
    if isinstance(value, list):
        return str(value[-1]) if value else default
    return str(value)


def split_slide_chunks(text: str) -> list[str]:
    return [chunk.strip() for chunk in re.split(r"\n---\n", text.strip()) if chunk.strip()]


def parse_slide_block(chunk: str) -> dict[str, Any]:
    lines = chunk.splitlines()
    index = 0
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index >= len(lines) or not lines[index].startswith("# "):
        raise ValueError("each slide block must start with '# ' title")

    title = normalize_title(lines[index][2:].strip())
    index += 1

    meta: dict[str, Any] = {}
    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped:
            index += 1
            continue
        if not stripped.startswith(">"):
            break
        content = stripped[1:].strip()
        if ":" in content:
            key, value = content.split(":", 1)
            append_meta(meta, key.strip(), value.strip())
        index += 1

    body = "\n".join(lines[index:]).strip()
    layout = meta_value(meta, "layout", "markdown")
    slide_id = meta_value(meta, "id")
    if not slide_id:
        raise ValueError(f"slide '{title}' is missing '> id:' metadata")

    slide = {
        "id": slide_id,
        "layout": layout,
        "title": title,
        "eyebrow": meta_value(meta, "eyebrow"),
        "manifest_goal": meta_value(meta, "goal"),
        "manifest_layout": meta_value(meta, "layout-note"),
        "manifest_body": meta_list(meta, "body-note"),
    }

    if layout == "cover":
        slide.update(parse_cover_body(body, meta))
    elif layout == "markdown":
        slide.update(parse_markdown_body(body, meta))
    elif layout == "card-grid":
        slide.update(parse_card_grid_body(body, meta))
    elif layout == "spec-grid":
        slide.update(parse_spec_grid_body(body, meta))
    elif layout == "code-and-checks":
        slide.update(parse_code_and_checks_body(body, meta))
    elif layout == "check-grid":
        slide.update(parse_check_grid_body(body, meta))
    elif layout == "faq-list":
        slide.update(parse_faq_list_body(body, meta))
    else:
        raise ValueError(f"unsupported markdown layout: {layout}")
    return slide


def split_sections(body: str) -> tuple[str, list[dict[str, str]]]:
    lines = body.splitlines()
    preamble: list[str] = []
    sections: list[dict[str, str]] = []
    current_title: str | None = None
    current_lines: list[str] = []

    for line in lines:
        if line.startswith("## "):
            if current_title is None:
                preamble = current_lines[:]
            else:
                sections.append({"title": normalize_title(current_title), "body": "\n".join(current_lines).strip()})
            current_title = line[3:].strip()
            current_lines = []
            continue
        current_lines.append(line)

    if current_title is None:
        preamble = current_lines[:]
    else:
        sections.append({"title": normalize_title(current_title), "body": "\n".join(current_lines).strip()})

    return "\n".join(preamble).strip(), sections


def parse_content_blocks(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    paragraphs: list[str] = []
    bullets: list[str] = []
    code_blocks: list[str] = []
    index = 0

    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped:
            index += 1
            continue
        if stripped.startswith("```"):
            fence = stripped[:3]
            index += 1
            code_lines: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith(fence):
                code_lines.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            code_blocks.append("\n".join(code_lines).strip("\n"))
            continue
        if stripped.startswith("- "):
            bullets.append(stripped[2:].strip())
            index += 1
            continue

        paragraph_lines = [stripped]
        index += 1
        while index < len(lines):
            next_stripped = lines[index].strip()
            if not next_stripped or next_stripped.startswith("## ") or next_stripped.startswith("- ") or next_stripped.startswith("```"):
                break
            paragraph_lines.append(next_stripped)
            index += 1
        paragraphs.append("\n".join(paragraph_lines).strip())

    return {"paragraphs": paragraphs, "bullets": bullets, "code_blocks": code_blocks}


def join_paragraphs(blocks: dict[str, Any]) -> str:
    return "\n".join(blocks["paragraphs"]).strip()


def text_from_section(blocks: dict[str, Any]) -> str:
    parts = list(blocks["paragraphs"])
    if blocks["bullets"]:
        parts.append("；".join(blocks["bullets"]))
    return "\n".join(part for part in parts if part).strip()


def split_pair(value: str) -> tuple[str, str]:
    for sep in ("｜", "|", ":", "："):
        if sep in value:
            left, right = value.split(sep, 1)
            return left.strip(), right.strip()
    return "", value.strip()


def footer_from_meta(meta: dict[str, Any]) -> dict[str, str] | None:
    title = meta_value(meta, "footer-title")
    text = meta_value(meta, "footer-text")
    if not title and not text:
        return None
    return {"title": title, "text": text}


def parse_cover_body(body: str, meta: dict[str, Any]) -> dict[str, Any]:
    preamble, sections = split_sections(body)
    lead = join_paragraphs(parse_content_blocks(preamble))
    metrics = []
    for section in sections:
        label, title = split_pair(section["title"])
        blocks = parse_content_blocks(section["body"])
        metrics.append({"label": label, "title": title, "text": text_from_section(blocks)})
    return {
        "lead": lead,
        "chips": meta_list(meta, "chip"),
        "metrics": metrics,
        "footer": footer_from_meta(meta),
    }


def parse_markdown_body(body: str, meta: dict[str, Any]) -> dict[str, Any]:
    blocks = parse_content_blocks(body)
    lead = "\n".join(blocks["paragraphs"][:1]).strip() if blocks["paragraphs"] else ""
    return {
        "lead": lead,
        "markdown_body": body,
        "footer": footer_from_meta(meta),
    }


def section_to_card(section: dict[str, str]) -> dict[str, Any]:
    blocks = parse_content_blocks(section["body"])
    card = {"title": section["title"]}
    text = join_paragraphs(blocks)
    if text:
        card["text"] = text
    if blocks["bullets"]:
        card["bullets"] = blocks["bullets"]
    return card


def parse_card_grid_body(body: str, meta: dict[str, Any]) -> dict[str, Any]:
    preamble, sections = split_sections(body)
    lead = join_paragraphs(parse_content_blocks(preamble))
    columns = meta_value(meta, "columns")
    return {
        "lead": lead,
        "columns": int(columns) if columns.isdigit() else None,
        "cards": [section_to_card(section) for section in sections],
        "footer": footer_from_meta(meta),
    }


def parse_spec_grid_body(body: str, meta: dict[str, Any]) -> dict[str, Any]:
    preamble, sections = split_sections(body)
    pre_blocks = parse_content_blocks(preamble)
    values = []
    for bullet in pre_blocks["bullets"]:
        label, value = split_pair(bullet)
        if not label:
            continue
        values.append({"label": label, "value": value})

    reminders = [section_to_card(section) for section in sections]
    return {
        "lead": join_paragraphs(pre_blocks),
        "values": values,
        "reminders": reminders,
        "reminder_columns": 2,
        "footer": footer_from_meta(meta),
    }


def parse_code_and_checks_body(body: str, meta: dict[str, Any]) -> dict[str, Any]:
    preamble, sections = split_sections(body)
    blocks = parse_content_blocks(preamble)
    code = blocks["code_blocks"][0] if blocks["code_blocks"] else ""
    lead_parts = blocks["paragraphs"][:]
    if blocks["bullets"]:
        lead_parts.extend(blocks["bullets"])
    side_items = [{"kind": "panel", "title": section["title"], "text": text_from_section(parse_content_blocks(section["body"]))} for section in sections]
    return {
        "lead": "\n".join(lead_parts).strip(),
        "code": code,
        "side_items": side_items,
        "footer": footer_from_meta(meta),
    }


def parse_check_grid_body(body: str, meta: dict[str, Any]) -> dict[str, Any]:
    blocks = parse_content_blocks(body)
    checks = []
    for bullet in blocks["bullets"]:
        title, text = split_pair(bullet)
        checks.append({"title": title or bullet, "text": text if title else ""})
    return {
        "lead": join_paragraphs(blocks),
        "checks": checks,
        "footer": footer_from_meta(meta),
    }


def parse_faq_list_body(body: str, meta: dict[str, Any]) -> dict[str, Any]:
    preamble, sections = split_sections(body)
    faqs = []
    for section in sections:
        blocks = parse_content_blocks(section["body"])
        faqs.append({"question": section["title"], "answer": text_from_section(blocks)})
    return {
        "lead": join_paragraphs(parse_content_blocks(preamble)),
        "faqs": faqs,
        "footer": footer_from_meta(meta),
    }


def parse_markdown_payload(path: Path) -> tuple[dict[str, Any], str]:
    text = read_text(path)
    meta, body = parse_frontmatter(text)
    slides = [parse_slide_block(chunk) for chunk in split_slide_chunks(body)]
    payload = {
        "theme": meta.get("theme", "clean-notes"),
        "title": meta.get("title", slides[0]["title"].replace("\n", " ")),
        "cover_title": meta.get("cover_title", slides[0]["title"].replace("\n", " ")),
        "cta": meta.get("cta", ""),
        "restructure_notes": meta.get("restructure_notes", []),
        "slides": slides,
    }
    return payload, text


def render_footer_band(band: dict[str, Any] | None) -> str:
    if not band:
        return ""
    title = f'<h3 class="panel-title">{with_breaks(band["title"])}</h3>' if band.get("title") else ""
    text = paragraph(band["text"], "footer-text") if band.get("text") else ""
    return f'<div class="footer-band">{title}{text}</div>'


def render_cards(cards: list[dict[str, Any]], columns: int | None = None) -> str:
    grid_cols = columns or min(max(len(cards), 1), 3)
    rendered_cards = []
    for card in cards:
        kicker = f'<span class="card-kicker">{escape_text(card["kicker"])}</span>' if card.get("kicker") else ""
        title = f'<h3 class="card-title">{with_breaks(card["title"])}</h3>' if card.get("title") else ""
        text = paragraph(card["text"], "card-text") if card.get("text") else ""
        bullets = bullet_list(card.get("bullets", []), "card-list")
        rendered_cards.append(f'<article class="card">{kicker}{title}{text}{bullets}</article>')
    return f'<div class="card-grid cols-{grid_cols}">{"".join(rendered_cards)}</div>'


def render_stack_item(item: dict[str, Any]) -> str:
    kind = item.get("kind", "panel")
    class_name = "panel"
    if kind == "note":
        class_name = "note"
    elif kind == "alert":
        class_name = "alert"
    elif kind == "code":
        code = escape_text(item.get("code", ""))
        title = f'<h3 class="panel-title">{with_breaks(item["title"])}</h3>' if item.get("title") else ""
        return f'<div class="code-panel">{title}<pre>{code}</pre></div>'

    title = f'<h3 class="panel-title">{with_breaks(item["title"])}</h3>' if item.get("title") else ""
    text = paragraph(item["text"], "panel-text") if item.get("text") else ""
    bullets = bullet_list(item.get("bullets", []), "panel-list")
    return f'<div class="{class_name}">{title}{text}{bullets}</div>'


def render_cover(slide: dict[str, Any]) -> str:
    eyebrow = f'<div class="eyebrow">{escape_text(slide["eyebrow"])}</div>' if slide.get("eyebrow") else ""
    title = f'<h1 class="title-hero">{with_breaks(slide["title"])}</h1>'
    lead = paragraph(slide["lead"], "lead") if slide.get("lead") else ""
    chips = ""
    if slide.get("chips"):
        chips = '<div class="chip-row">' + "".join(f'<span class="chip">{escape_text(chip)}</span>' for chip in slide["chips"]) + "</div>"

    metrics = ""
    if slide.get("metrics"):
        parts = []
        for metric in slide["metrics"]:
            label = f'<span class="metric-label">{escape_text(metric["label"])}</span>' if metric.get("label") else ""
            title_part = f'<h3 class="metric-title">{with_breaks(metric["title"])}</h3>'
            text = paragraph(metric["text"], "metric-text") if metric.get("text") else ""
            parts.append(f'<article class="metric">{label}{title_part}{text}</article>')
        metrics = f'<div class="metric-row cols-{min(max(len(parts), 1), 3)}">{"".join(parts)}</div>'

    footer = render_footer_band(slide.get("footer"))
    return eyebrow + title + lead + chips + metrics + footer


def render_markdown_layout(slide: dict[str, Any]) -> str:
    eyebrow = f'<div class="eyebrow">{escape_text(slide["eyebrow"])}</div>' if slide.get("eyebrow") else ""
    title = f'<h1 class="title-page">{with_breaks(slide["title"])}</h1>'
    body = f'<div class="markdown-flow">{render_markdown_html(slide.get("markdown_body", ""))}</div>'
    footer = render_footer_band(slide.get("footer"))
    return eyebrow + title + body + footer


def render_card_grid(slide: dict[str, Any]) -> str:
    eyebrow = f'<div class="eyebrow">{escape_text(slide["eyebrow"])}</div>' if slide.get("eyebrow") else ""
    title = f'<h1 class="title-page">{with_breaks(slide["title"])}</h1>'
    lead = paragraph(slide["lead"], "lead") if slide.get("lead") else ""
    cards = render_cards(slide.get("cards", []), slide.get("columns"))
    footer = render_footer_band(slide.get("footer"))
    return eyebrow + title + lead + cards + footer


def render_spec_grid(slide: dict[str, Any]) -> str:
    eyebrow = f'<div class="eyebrow">{escape_text(slide["eyebrow"])}</div>' if slide.get("eyebrow") else ""
    title = f'<h1 class="title-page">{with_breaks(slide["title"])}</h1>'
    lead = paragraph(slide["lead"], "lead") if slide.get("lead") else ""

    parts = []
    for item in slide.get("values", []):
        wide = " wide" if item.get("wide") else ""
        label = f'<span class="kv-label">{escape_text(item["label"])}</span>' if item.get("label") else ""
        value = f'<h3 class="kv-value">{with_breaks(item["value"])}</h3>' if item.get("value") else ""
        sub = paragraph(item["sub"], "kv-sub") if item.get("sub") else ""
        parts.append(f'<article class="kv-card{wide}">{label}{value}{sub}</article>')
    values = f'<div class="kv-grid cols-2">{"".join(parts)}</div>'

    reminders = ""
    if slide.get("reminders"):
        reminders = render_cards(slide["reminders"], slide.get("reminder_columns", 2))
    footer = render_footer_band(slide.get("footer"))
    return eyebrow + title + lead + values + reminders + footer


def render_code_and_checks(slide: dict[str, Any]) -> str:
    eyebrow = f'<div class="eyebrow">{escape_text(slide["eyebrow"])}</div>' if slide.get("eyebrow") else ""
    title = f'<h1 class="title-page">{with_breaks(slide["title"])}</h1>'
    lead = paragraph(slide["lead"], "lead") if slide.get("lead") else ""
    code_panel = f'<div class="code-panel"><pre>{escape_text(slide.get("code", ""))}</pre></div>'
    right_stack = "".join(render_stack_item(item) for item in slide.get("side_items", []))
    body = f'<div class="split"><div>{code_panel}</div><div class="stack">{right_stack}</div></div>'
    footer = render_footer_band(slide.get("footer"))
    return eyebrow + title + lead + body + footer


def render_check_grid(slide: dict[str, Any]) -> str:
    eyebrow = f'<div class="eyebrow">{escape_text(slide["eyebrow"])}</div>' if slide.get("eyebrow") else ""
    title = f'<h1 class="title-page">{with_breaks(slide["title"])}</h1>'
    lead = paragraph(slide["lead"], "lead") if slide.get("lead") else ""
    parts = []
    for item in slide.get("checks", []):
        parts.append(
            f"""
<article class="check-card">
  <div class="check-row">
    <div class="check-mark">✓</div>
    <div>
      <h3 class="check-title">{with_breaks(item["title"])}</h3>
      <p class="check-text">{with_breaks(item["text"])}</p>
    </div>
  </div>
</article>
"""
        )
    grid = f'<div class="check-grid cols-2">{"".join(parts)}</div>'
    footer = render_footer_band(slide.get("footer"))
    return eyebrow + title + lead + grid + footer


def render_faq_list(slide: dict[str, Any]) -> str:
    eyebrow = f'<div class="eyebrow">{escape_text(slide["eyebrow"])}</div>' if slide.get("eyebrow") else ""
    title = f'<h1 class="title-page">{with_breaks(slide["title"])}</h1>'
    lead = paragraph(slide["lead"], "lead") if slide.get("lead") else ""
    rows = []
    for item in slide.get("faqs", []):
        rows.append(
            f"""
<article class="faq-item">
  <h3 class="faq-title">{with_breaks(item["question"])}</h3>
  <p class="faq-text">{with_breaks(item["answer"])}</p>
</article>
"""
        )
    body = f'<div class="faq-list">{"".join(rows)}</div>'
    footer = render_footer_band(slide.get("footer"))
    return eyebrow + title + lead + body + footer


LAYOUTS = {
    "cover": render_cover,
    "markdown": render_markdown_layout,
    "card-grid": render_card_grid,
    "spec-grid": render_spec_grid,
    "code-and-checks": render_code_and_checks,
    "check-grid": render_check_grid,
    "faq-list": render_faq_list,
}


def render_slide(slide: dict[str, Any]) -> str:
    layout = slide["layout"]
    renderer = LAYOUTS.get(layout)
    if renderer is None:
        raise ValueError(f"unsupported layout: {layout}")
    body = renderer(slide)
    title = escape_text(slide.get("id", "slide"))
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1242, initial-scale=1.0" />
    <title>{title}</title>
    <link rel="stylesheet" href="theme.css" />
  </head>
  <body>
    <main class="slide layout-{escape_text(layout)}">
      <section class="frame">
        {body}
      </section>
    </main>
  </body>
</html>"""


def render_manifest(payload: dict[str, Any], theme_name: str) -> str:
    lines = [
        "# Xiaohongshu Manifest",
        "",
        "## 总标题",
        "",
        payload["title"],
        "",
        "## 封面标题",
        "",
        payload["cover_title"],
        "",
        "## 主题",
        "",
        theme_name,
        "",
        "## 页面明细",
        "",
    ]

    for slide in payload["slides"]:
        lines.extend(
            [
                f"### {slide['id']}",
                "",
                f"- 目标：{slide.get('manifest_goal', '')}",
                "- 正文：",
            ]
        )
        for item in slide.get("manifest_body", []):
            lines.append(f"  - {item}")
        lines.extend(
            [
                f"- 版式：{slide.get('manifest_layout', '')}",
                "",
            ]
        )

    lines.extend(
        [
            "## 结尾行动引导",
            "",
            payload.get("cta", ""),
            "",
            "## 重组说明",
            "",
        ]
    )
    for item in payload.get("restructure_notes", []):
        lines.append(f"- {item}")

    return "\n".join(lines)


def build_theme_css(theme_name: str) -> str:
    base_path = ASSET_DIR / "base.css"
    theme_path = THEMES_DIR / f"{theme_name}.css"
    if not theme_path.is_file():
        available = ", ".join(path.stem for path in sorted(THEMES_DIR.glob("*.css")))
        raise ValueError(f"unknown theme '{theme_name}', available: {available}")
    return (
        "/* generated by scripts/build_xiaohongshu_carousel.py */\n"
        f"/* theme: {theme_name} */\n\n"
        + read_text(base_path)
        + "\n\n"
        + read_text(theme_path)
    )


def clean_output(output_dir: Path) -> None:
    for pattern in ("slide-*.html", "slide-*.png", "manifest.md", "theme.css", "source.json"):
        for path in output_dir.glob(pattern):
            if path.is_file():
                path.unlink()


def write_source_artifacts(source_path: Path, output_dir: Path, payload: dict[str, Any], original_markdown: str | None) -> None:
    if original_markdown is not None:
        slides_target = output_dir / "slides.md"
        if source_path.resolve() != slides_target.resolve():
            write_text(slides_target, original_markdown)
    source_target = output_dir / "source.json"
    write_text(source_target, json.dumps(payload, ensure_ascii=False, indent=2))


def load_payload(source_path: Path) -> tuple[dict[str, Any], str | None]:
    if source_path.suffix.lower() == ".md":
        return parse_markdown_payload(source_path)
    if source_path.suffix.lower() == ".json":
        return read_json(source_path), None
    raise ValueError("source must be a .md or .json file")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Xiaohongshu carousel HTML assets from markdown or JSON source.")
    parser.add_argument("source", type=Path, help="Path to slides.md or source.json")
    parser.add_argument("--output-dir", type=Path, default=None, help="Directory for generated files; defaults to the source file parent")
    parser.add_argument("--theme", default=None, help="Override theme name from source metadata")
    parser.add_argument("--clean", action="store_true", help="Remove previous generated files before writing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload, original_markdown = load_payload(args.source)
    output_dir = args.output_dir or args.source.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.clean:
        clean_output(output_dir)

    theme_name = args.theme or payload.get("theme", "clean-notes")
    write_source_artifacts(args.source, output_dir, payload, original_markdown)
    write_text(output_dir / "theme.css", build_theme_css(theme_name))
    write_text(output_dir / "manifest.md", render_manifest(payload, theme_name))

    for slide in payload["slides"]:
        write_text(output_dir / f"{slide['id']}.html", render_slide(slide))

    print(f"Built {len(payload['slides'])} slides in {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
