#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None

    frontmatter: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def ok(condition: bool, message: str, failures: list[str]) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {message}")
    if not condition:
        failures.append(message)


def validate_repo_layout(failures: list[str]) -> None:
    for relative in (
        "skills",
        "commands",
        "evals",
        "evals/skills",
        "evals/commands",
        "scripts",
        "references",
        "references/repos",
    ):
        ok((ROOT / relative).is_dir(), f"directory exists: {relative}", failures)
    ok((ROOT / "AGENTS.md").is_file(), "file exists: AGENTS.md", failures)
    ok((ROOT / "references" / "README.md").is_file(), "file exists: references/README.md", failures)
    ok((ROOT / "references" / "repos" / ".gitignore").is_file(), "file exists: references/repos/.gitignore", failures)


def validate_skill(skill_path: Path, failures: list[str]) -> None:
    text = read_text(skill_path)
    frontmatter = parse_frontmatter(text)
    skill_name = skill_path.parent.name
    label = skill_path.relative_to(ROOT)

    ok(frontmatter is not None, f"{label} has YAML frontmatter", failures)
    if frontmatter is None:
        return

    ok(frontmatter.get("name") == skill_name, f"{label} frontmatter name matches directory", failures)
    ok(bool(frontmatter.get("description")), f"{label} has description", failures)

    for heading in ("## 何时使用", "## 产物", "## 工作流"):
        ok(heading in text, f"{label} contains heading: {heading}", failures)

    eval_path = ROOT / "evals" / "skills" / f"{skill_name}.md"
    ok(eval_path.is_file(), f"paired eval exists: {eval_path.relative_to(ROOT)}", failures)

    if skill_name == "eval-harness":
        ok("Claude Code" not in text, f"{label} is tool-neutral about Claude Code", failures)
        ok(".claude/" not in text, f"{label} does not hardcode .claude storage", failures)
        ok("skills/" in text and "commands/" in text, f"{label} covers both skills and commands", failures)
        ok("代码评分器" in text, f"{label} prefers code-based graders", failures)
        ok("references/templates.md" in text, f"{label} moves examples into references", failures)
    if skill_name == "xiaohongshu-carousel":
        ok("已有" in text and "内容" in text, f"{label} targets existing content", failures)
        ok("不适用：" in text and "选题" in text and "竞品" in text, f"{label} excludes pre-production work", failures)
        ok("1242x1660" in text and "3:4" in text, f"{label} defines Xiaohongshu-friendly dimensions", failures)
        ok("slide-01.png" in text and "manifest.md" in text, f"{label} defines concrete deliverables", failures)
        ok("slides.md" in text, f"{label} defines markdown source input", failures)
        ok("source.json" in text, f"{label} keeps compiled structured output", failures)
        ok("HTML" in text or "SVG" in text, f"{label} includes renderable source files", failures)
        ok("不编造事实" in text, f"{label} forbids inventing unsupported facts", failures)
        ok("封面" in text and "结尾页" in text, f"{label} defines key page roles", failures)
        ok("references/page-patterns.md" in text, f"{label} keeps page templates in references", failures)
        ok("scripts/build_xiaohongshu_carousel.py" in text, f"{label} references reusable build script", failures)
        ok("默认优先使用 `layout: markdown`" in text or "正文页默认优先使用 `layout: markdown`" in text, f"{label} defaults to markdown-first page authoring", failures)
        ok("references/visual-styles.md" in text, f"{label} references theme guidance", failures)
        ok("references/markdown-authoring.md" in text, f"{label} references markdown authoring guidance", failures)
        ok((ROOT / "scripts" / "build_xiaohongshu_carousel.py").is_file(), "build script exists: scripts/build_xiaohongshu_carousel.py", failures)
        ok((ROOT / "skills" / "xiaohongshu-carousel" / "assets" / "base.css").is_file(), "base theme exists for xiaohongshu-carousel", failures)
        theme_files = sorted((ROOT / "skills" / "xiaohongshu-carousel" / "assets" / "themes").glob("*.css"))
        ok(len(theme_files) >= 3, "xiaohongshu-carousel has at least three themes", failures)
        ok((ROOT / "skills" / "xiaohongshu-carousel" / "references" / "visual-styles.md").is_file(), "visual style reference exists for xiaohongshu-carousel", failures)
        ok((ROOT / "skills" / "xiaohongshu-carousel" / "references" / "markdown-authoring.md").is_file(), "markdown authoring reference exists for xiaohongshu-carousel", failures)


def validate_command(command_path: Path, failures: list[str]) -> None:
    text = read_text(command_path)
    frontmatter = parse_frontmatter(text)
    command_name = command_path.stem
    label = command_path.relative_to(ROOT)

    ok(frontmatter is not None, f"{label} has YAML frontmatter", failures)
    if frontmatter is None:
        return

    ok(frontmatter.get("name") == command_name, f"{label} frontmatter name matches filename", failures)
    ok(bool(frontmatter.get("description")), f"{label} has description", failures)

    for heading in ("## 何时使用", "## 输入", "## 输出", "## Prompt"):
        ok(heading in text, f"{label} contains heading: {heading}", failures)

    eval_path = ROOT / "evals" / "commands" / f"{command_name}.md"
    ok(eval_path.is_file(), f"paired eval exists: {eval_path.relative_to(ROOT)}", failures)

def validate_eval(eval_path: Path, failures: list[str]) -> None:
    text = read_text(eval_path)
    label = eval_path.relative_to(ROOT)

    for heading in (
        "## Asset Under Test",
        "## Capability Evals",
        "## Regression Evals",
        "## Exit Criteria",
    ):
        ok(heading in text, f"{label} contains heading: {heading}", failures)


def main() -> int:
    failures: list[str] = []

    validate_repo_layout(failures)

    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    ok(bool(skill_files), "at least one skill exists", failures)
    for skill_file in skill_files:
        validate_skill(skill_file, failures)

    command_files = sorted((ROOT / "commands").glob("*.md"))
    for command_file in command_files:
        validate_command(command_file, failures)

    eval_files = sorted((ROOT / "evals").glob("**/*.md"))
    ok(bool(eval_files), "at least one eval definition exists", failures)
    for eval_file in eval_files:
        validate_eval(eval_file, failures)

    if failures:
        print(f"\nValidation failed with {len(failures)} issue(s).")
        return 1

    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
