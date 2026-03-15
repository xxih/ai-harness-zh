#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = ROOT / "src"
TARGETS_ROOT = ROOT / "targets"


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
        "src",
        "src/agents",
        "src/skills",
        "src/commands",
        "evals",
        "evals/agents",
        "evals/skills",
        "evals/commands",
        "scripts",
        "references",
        "references/repos",
        "targets",
        "targets/codex",
        "targets/codex/skills",
        "targets/codex/agents",
        "targets/codex/commands",
        "targets/codex/.codex",
        "targets/codex/.codex/agents",
    ):
        ok((ROOT / relative).is_dir(), f"directory exists: {relative}", failures)
    ok((ROOT / "AGENTS.md").is_file(), "file exists: AGENTS.md", failures)
    ok((ROOT / "references" / "README.md").is_file(), "file exists: references/README.md", failures)
    ok((ROOT / "references" / "repos" / ".gitignore").is_file(), "file exists: references/repos/.gitignore", failures)
    ok((TARGETS_ROOT / "README.md").is_file(), "file exists: targets/README.md", failures)
    ok((TARGETS_ROOT / "codex" / "README.md").is_file(), "file exists: targets/codex/README.md", failures)
    ok((TARGETS_ROOT / "codex" / ".codex" / "AGENTS.md").is_file(), "file exists: targets/codex/.codex/AGENTS.md", failures)
    ok((TARGETS_ROOT / "codex" / ".codex" / "config.toml").is_file(), "file exists: targets/codex/.codex/config.toml", failures)


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
        ok("src/skills/" in text and "src/commands/" in text, f"{label} covers both skills and commands", failures)
        ok("代码评分器" in text, f"{label} prefers code-based graders", failures)
        ok("references/templates.md" in text, f"{label} moves examples into references", failures)
    if skill_name == "search-first":
        ok("references/repos/" in text, f"{label} consults references/repos for external coding patterns", failures)
        ok("测试" in text, f"{label} searches tests before implementation", failures)
        ok(
            all(token in text.lower() for token in ("adopt", "adapt", "build")),
            f"{label} defines adopt/adapt/build decisions",
            failures,
        )
        ok("research-note.md" in text, f"{label} defines a durable research output", failures)
        ok(".research/research-note.md" in text, f"{label} uses a project-local default research output path", failures)
        ok(
            "新功能" in text and "bug" in text and "依赖" in text,
            f"{label} targets coding tasks such as features, bugs, and integrations",
            failures,
        )
        ok(
            (SRC_ROOT / "skills" / "search-first" / "references" / "research-checklist.md").is_file(),
            "research checklist reference exists for search-first",
            failures,
        )
    if skill_name == "quality-router":
        ok(
            all(token in text for token in ("/tdd", "/verify", "/review", "/review-feedback")),
            f"{label} routes explicit quality triggers",
            failures,
        )
        ok(
            all(token in text for token in ("quality-tdd", "quality-verify", "quality-review", "quality-review-feedback")),
            f"{label} routes to the quality-* skill family",
            failures,
        )
        ok("src/commands/" in text, f"{label} acts as a commands replacement", failures)
        ok(
            "不依赖 `nanospec`" in text or "不要把 `nanospec` 当成前提" in text or "不以任何单一任务框架为前提" in text,
            f"{label} does not hard-require nanospec output paths",
            failures,
        )
        ok(".quality/quality-check.md" in text, f"{label} uses a project-local fallback quality output path", failures)
        ok("nanospec/<task>/assets/quality-check.md" in text, f"{label} prefers task-container quality output when available", failures)
        ok("coding-quality-loop" not in text, f"{label} no longer routes to coding-quality-loop", failures)
    if skill_name == "quality-tdd":
        ok("失败测试" in text and "先写实现再补测试" in text, f"{label} enforces test-first discipline", failures)
        ok("没看到失败" in text or "没看到 fail" in text, f"{label} requires watching the test fail", failures)
        ok("Red-Green-Refactor" in text or "红-绿-重构" in text, f"{label} describes a red-green-refactor loop", failures)
        ok("这次先跳过" in text or "合理化" in text, f"{label} carries anti-rationalization guidance", failures)
        ok("references/testing-anti-patterns.md" in text, f"{label} links to anti-pattern references", failures)
        ok(
            "不依赖 `nanospec`" in text or "不要把 `nanospec` 当成前提" in text or "不以任何单一任务框架为前提" in text,
            f"{label} does not hard-require nanospec output paths",
            failures,
        )
        ok(".quality/quality-check.md" in text, f"{label} uses a project-local fallback quality output path", failures)
        ok("nanospec/<task>/assets/quality-check.md" in text, f"{label} prefers task-container quality output when available", failures)
    if skill_name == "quality-verify":
        ok("fresh evidence" in text and "not-ready" in text.lower(), f"{label} enforces fresh evidence before completion claims", failures)
        ok(
            all(token in text for token in ("识别", "执行", "读取", "核对", "宣称")),
            f"{label} describes a verification gate sequence",
            failures,
        )
        ok("应该可以" in text or "看起来没问题" in text, f"{label} warns against false completion wording", failures)
        ok("build" in text.lower() and "tests" in text.lower() and "diff" in text.lower(), f"{label} includes full verification scope", failures)
        ok(
            "不依赖 `nanospec`" in text or "不要把 `nanospec` 当成前提" in text or "不依赖任何特定任务框架" in text,
            f"{label} does not hard-require nanospec output paths",
            failures,
        )
        ok(".quality/quality-check.md" in text, f"{label} uses a project-local fallback quality output path", failures)
        ok("nanospec/<task>/assets/quality-check.md" in text, f"{label} prefers task-container quality output when available", failures)
    if skill_name == "quality-review":
        ok("独立 reviewer" in text or "multiagent" in text, f"{label} prefers an independent reviewer path", failures)
        ok("Critical" in text and "Important" in text and "Minor" in text, f"{label} acts on tiered review findings", failures)
        ok("references/reviewer-template.md" in text, f"{label} links to the reusable reviewer template", failures)
        ok("不依赖 `nanospec`" in text or "不以任何单一任务框架为前提" in text, f"{label} does not hard-require nanospec output paths", failures)
        ok(".quality/quality-check.md" in text, f"{label} uses a project-local fallback quality output path", failures)
        ok("nanospec/<task>/assets/quality-check.md" in text, f"{label} prefers task-container quality output when available", failures)
        ok(
            (SRC_ROOT / "skills" / "quality-review" / "references" / "reviewer-template.md").is_file(),
            "reviewer template reference exists for quality-review",
            failures,
        )
    if skill_name == "quality-review-feedback":
        ok(
            all(token in text for token in ("读取", "理解", "核实", "评估", "回应", "实现")),
            f"{label} defines a verification-first feedback handling flow",
            failures,
        )
        ok("表演性认同" in text or "盲从" in text, f"{label} forbids performative agreement", failures)
        ok("先澄清" in text or "不清楚" in text, f"{label} requires clarification before implementation", failures)
        ok("YAGNI" in text or "现有行为" in text, f"{label} includes technical pushback conditions", failures)
        ok("不依赖 `nanospec`" in text or "不能假设调用方一定有该类目录结构" in text, f"{label} does not hard-require nanospec output paths", failures)
        ok(".quality/quality-check.md" in text, f"{label} uses a project-local fallback quality output path", failures)
        ok("nanospec/<task>/assets/quality-check.md" in text, f"{label} prefers task-container quality output when available", failures)
    if skill_name == "agent-orchestration":
        ok(
            all(token in text for token in ("planner", "orchestrator", "worker", "explore", "reviewer")),
            f"{label} defines a role-layered orchestration model",
            failures,
        )
        ok(
            "research -> plan -> execute -> review -> verify" in text,
            f"{label} defines an explicit staged workflow",
            failures,
        )
        ok(
            "单任务" in text and "一次只交给一个明确任务" in text,
            f"{label} enforces single-task delegation",
            failures,
        )
        ok(
            "并行前必须先做独立性判定" in text or ("并行" in text and "独立性" in text),
            f"{label} requires independence checks before parallel work",
            failures,
        )
        ok(
            "反重复规则" in text and "不重复" in text,
            f"{label} forbids duplicating delegated work",
            failures,
        )
        ok(
            "不能直接信任" in text or "不要把摘要当证据" in text,
            f"{label} requires verification instead of trusting delegated summaries",
            failures,
        )
        ok(
            "targets/" in text,
            f"{label} pushes platform-specific APIs into target adapters",
            failures,
        )
        ok(
            ".research/orchestration-note.md" in text,
            f"{label} uses a project-local default orchestration output path",
            failures,
        )
        ok(
            "references/delegation-template.md" in text,
            f"{label} links to the reusable delegation template",
            failures,
        )
        ok(
            (SRC_ROOT / "skills" / "agent-orchestration" / "references" / "delegation-template.md").is_file(),
            "delegation template reference exists for agent-orchestration",
            failures,
        )
    if skill_name == "learning-capture":
        ok(
            "手工触发" in text or "手动触发" in text,
            f"{label} is explicitly manual-triggered",
            failures,
        )
        ok(
            "hooks" in text and "不依赖 hooks" in text,
            f"{label} explicitly avoids hook-dependent automation",
            failures,
        )
        ok(
            all(
                token in text
                for token in (
                    ".learning/learnings.md",
                    ".learning/promote-candidates.md",
                    ".learning/project-rules.md",
                )
            ),
            f"{label} defines project-local fallback learning output paths",
            failures,
        )
        ok(
            all(token in text for token in ("keep-local", "promote-later", "propose-agents-update", "drop")),
            f"{label} defines learning follow-up states",
            failures,
        )
        ok(
            "references/templates.md" in text,
            f"{label} links to the reusable learning templates",
            failures,
        )
        ok(
            "project-rules.md" in text and "AGENTS.md" in text,
            f"{label} captures project-level rule candidates and AGENTS update proposals",
            failures,
        )
        ok(
            ".learning/" in text and "不要把 `nanospec` 当成学习记录的默认载体" in text,
            f"{label} keeps .learning as the default learning sink instead of nanospec",
            failures,
        )
        ok(
            (SRC_ROOT / "skills" / "learning-capture" / "references" / "templates.md").is_file(),
            "templates reference exists for learning-capture",
            failures,
        )
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
        ok((SRC_ROOT / "skills" / "xiaohongshu-carousel" / "assets" / "base.css").is_file(), "base theme exists for xiaohongshu-carousel", failures)
        theme_files = sorted((SRC_ROOT / "skills" / "xiaohongshu-carousel" / "assets" / "themes").glob("*.css"))
        ok(len(theme_files) >= 3, "xiaohongshu-carousel has at least three themes", failures)
        ok((SRC_ROOT / "skills" / "xiaohongshu-carousel" / "references" / "visual-styles.md").is_file(), "visual style reference exists for xiaohongshu-carousel", failures)
        ok((SRC_ROOT / "skills" / "xiaohongshu-carousel" / "references" / "markdown-authoring.md").is_file(), "markdown authoring reference exists for xiaohongshu-carousel", failures)


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


def validate_agent(agent_path: Path, failures: list[str]) -> None:
    text = read_text(agent_path)
    frontmatter = parse_frontmatter(text)
    agent_name = agent_path.stem
    label = agent_path.relative_to(ROOT)

    ok(frontmatter is not None, f"{label} has YAML frontmatter", failures)
    if frontmatter is None:
        return

    ok(frontmatter.get("name") == agent_name, f"{label} frontmatter name matches filename", failures)
    ok(bool(frontmatter.get("description")), f"{label} has description", failures)

    for heading in ("## 何时使用", "## 输入", "## 输出", "## Prompt"):
        ok(heading in text, f"{label} contains heading: {heading}", failures)

    eval_path = ROOT / "evals" / "agents" / f"{agent_name}.md"
    ok(eval_path.is_file(), f"paired eval exists: {eval_path.relative_to(ROOT)}", failures)

    if agent_name == "quality-code-reviewer":
        ok("Critical" in text and "Important" in text and "Minor" in text, f"{label} uses tiered review severity", failures)
        ok("ready" in text.lower() and "not-ready" in text.lower(), f"{label} ends with an explicit readiness assessment", failures)

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


def validate_codex_target(failures: list[str]) -> None:
    codex_root = TARGETS_ROOT / "codex"
    codex_config_root = codex_root / ".codex"
    config_path = codex_config_root / "config.toml"
    agents_path = codex_config_root / "AGENTS.md"
    reviewer_path = codex_config_root / "agents" / "reviewer.toml"

    if config_path.is_file():
        config_text = read_text(config_path)
        ok("multi_agent = true" in config_text, "targets/codex enables Codex multi_agent mode", failures)
        ok('[agents.reviewer]' in config_text, "targets/codex registers a reviewer role", failures)
        ok('config_file = "agents/reviewer.toml"' in config_text, "targets/codex reviewer role points to its TOML config", failures)
        ok('[agents.quality_code_reviewer]' in config_text, "targets/codex registers the quality_code_reviewer role", failures)
        ok('config_file = "agents/quality-code-reviewer.toml"' in config_text, "targets/codex quality_code_reviewer role points to its TOML config", failures)
    if agents_path.is_file():
        agents_text = read_text(agents_path)
        ok("skills/" in agents_text and "agents/" in agents_text and "commands/" in agents_text, "targets/codex AGENTS.md uses same-shape distribution assets", failures)
        ok("src/skills/" in agents_text and "src/agents/" in agents_text and "src/commands/" in agents_text, "targets/codex AGENTS.md maps Codex behavior back to src assets", failures)
        ok("config.toml" in agents_text and ".codex/agents/" in agents_text, "targets/codex AGENTS.md explains config-to-agent-role wiring", failures)
        ok("quality_code_reviewer" in agents_text and "agents/quality-code-reviewer.md" in agents_text, "targets/codex AGENTS.md documents the quality-code-reviewer role mapping", failures)
    if reviewer_path.is_file():
        reviewer_text = read_text(reviewer_path)
        ok("agents/quality-code-reviewer.md" in reviewer_text or "src/agents/quality-code-reviewer.md" in reviewer_text, "targets/codex reviewer role aligns with the reusable reviewer prompt", failures)
    quality_reviewer_path = codex_config_root / "agents" / "quality-code-reviewer.toml"
    if quality_reviewer_path.is_file():
        quality_reviewer_text = read_text(quality_reviewer_path)
        ok("targets/codex/agents/quality-code-reviewer.md" in quality_reviewer_text or "agents/quality-code-reviewer.md" in quality_reviewer_text, "targets/codex quality_code_reviewer TOML points at the distributed agent asset", failures)
        ok("Requirements alignment" in quality_reviewer_text and "Code quality" in quality_reviewer_text and "Test quality" in quality_reviewer_text and "Risk judgment" in quality_reviewer_text, "targets/codex quality_code_reviewer TOML carries the full review dimensions", failures)
        ok("Strengths" in quality_reviewer_text and "Issues" in quality_reviewer_text and "Assessment" in quality_reviewer_text, "targets/codex quality_code_reviewer TOML carries the full output contract", failures)
        for skill_path in (
            '../../skills/quality-review/SKILL.md',
            '../../skills/quality-review-feedback/SKILL.md',
            '../../skills/quality-verify/SKILL.md',
            '../../skills/quality-tdd/SKILL.md',
            '../../skills/quality-router/SKILL.md',
        ):
            ok(skill_path in quality_reviewer_text, f"targets/codex quality_code_reviewer TOML enables skill: {skill_path}", failures)

    for source_dir, target_dir, label in (
        (SRC_ROOT / "skills", codex_root / "skills", "skills"),
        (SRC_ROOT / "agents", codex_root / "agents", "agents"),
        (SRC_ROOT / "commands", codex_root / "commands", "commands"),
    ):
        source_files = sorted(path.relative_to(source_dir) for path in source_dir.rglob("*") if path.is_file())
        target_files = sorted(path.relative_to(target_dir) for path in target_dir.rglob("*") if path.is_file())
        ok(source_files == target_files, f"targets/codex {label} mirror matches src/{label}", failures)


def main() -> int:
    failures: list[str] = []

    validate_repo_layout(failures)

    skill_files = sorted((SRC_ROOT / "skills").glob("*/SKILL.md"))
    ok(bool(skill_files), "at least one skill exists", failures)
    for skill_file in skill_files:
        validate_skill(skill_file, failures)

    agent_files = sorted((SRC_ROOT / "agents").glob("*.md"))
    for agent_file in agent_files:
        validate_agent(agent_file, failures)

    command_files = sorted((SRC_ROOT / "commands").glob("*.md"))
    for command_file in command_files:
        validate_command(command_file, failures)

    eval_files = sorted((ROOT / "evals").glob("**/*.md"))
    ok(bool(eval_files), "at least one eval definition exists", failures)
    for eval_file in eval_files:
        validate_eval(eval_file, failures)

    validate_codex_target(failures)

    if failures:
        print(f"\nValidation failed with {len(failures)} issue(s).")
        return 1

    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
