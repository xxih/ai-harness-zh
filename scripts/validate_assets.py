#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = ROOT / "src"
DOMAINS_ROOT = SRC_ROOT / "domains"
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


def collect_domains() -> list[Path]:
    return sorted(path for path in DOMAINS_ROOT.iterdir() if path.is_dir())


def collect_skill_files() -> list[Path]:
    return sorted(DOMAINS_ROOT.glob("*/skills/*/SKILL.md"))


def collect_agent_files() -> list[Path]:
    return sorted(DOMAINS_ROOT.glob("*/agents/*.md"))


def collect_command_files() -> list[Path]:
    return sorted(DOMAINS_ROOT.glob("*/commands/*.md"))


def collect_skill_dirs_by_name() -> dict[str, Path]:
    skills: dict[str, Path] = {}
    for skill_file in collect_skill_files():
        name = skill_file.parent.name
        if name in skills:
            raise ValueError(f"Duplicate skill name across domains: {name}")
        skills[name] = skill_file.parent
    return skills


def collect_asset_files_by_name(kind: str) -> dict[str, Path]:
    pattern = f"*/{kind}/*.md"
    assets: dict[str, Path] = {}
    for path in sorted(DOMAINS_ROOT.glob(pattern)):
        name = path.stem
        if name in assets:
            raise ValueError(f"Duplicate {kind[:-1]} name across domains: {name}")
        assets[name] = path
    return assets


def validate_repo_layout(failures: list[str]) -> None:
    for relative in (
        "src",
        "src/domains",
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

    for relative in (
        "AGENTS.md",
        "src/AGENTS.md",
        "references/README.md",
        "references/repos/.gitignore",
        "targets/README.md",
        "targets/codex/README.md",
        "targets/codex/.codex/AGENTS.md",
        "targets/codex/.codex/config.toml",
    ):
        ok((ROOT / relative).is_file(), f"file exists: {relative}", failures)


def validate_domain_layout(domain_dir: Path, failures: list[str]) -> None:
    label = domain_dir.relative_to(ROOT)
    ok((domain_dir / "AGENTS.md").is_file(), f"{label} has AGENTS.md", failures)
    ok((domain_dir / "skills").is_dir(), f"{label} has skills/", failures)
    ok((domain_dir / "agents").is_dir(), f"{label} has agents/", failures)
    ok((domain_dir / "commands").is_dir(), f"{label} has commands/", failures)


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
        ok(
            "src/domains/<domain>/skills/" in text and "src/domains/<domain>/commands/" in text,
            f"{label} covers both domain-local skills and commands",
            failures,
        )
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
        ok((skill_path.parent / "references" / "research-checklist.md").is_file(), "research checklist reference exists for search-first", failures)
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
        ok("commands/" in text, f"{label} acts as a commands replacement", failures)
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
        ok(all(token in text for token in ("识别", "执行", "读取", "核对", "宣称")), f"{label} describes a verification gate sequence", failures)
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
        ok((skill_path.parent / "references" / "reviewer-template.md").is_file(), "reviewer template reference exists for quality-review", failures)
    if skill_name == "quality-review-feedback":
        ok(all(token in text for token in ("读取", "理解", "核实", "评估", "回应", "实现")), f"{label} defines a verification-first feedback handling flow", failures)
        ok("表演性认同" in text or "盲从" in text, f"{label} forbids performative agreement", failures)
        ok("先澄清" in text or "不清楚" in text, f"{label} requires clarification before implementation", failures)
        ok("YAGNI" in text or "现有行为" in text, f"{label} includes technical pushback conditions", failures)
        ok("不依赖 `nanospec`" in text or "不能假设调用方一定有该类目录结构" in text, f"{label} does not hard-require nanospec output paths", failures)
        ok(".quality/quality-check.md" in text, f"{label} uses a project-local fallback quality output path", failures)
        ok("nanospec/<task>/assets/quality-check.md" in text, f"{label} prefers task-container quality output when available", failures)
    if skill_name == "agent-orchestration":
        ok(all(token in text for token in ("planner", "orchestrator", "worker", "explore", "reviewer")), f"{label} defines a role-layered orchestration model", failures)
        ok("research -> plan -> execute -> review -> verify" in text, f"{label} defines an explicit staged workflow", failures)
        ok("单任务" in text and "一次只交给一个明确任务" in text, f"{label} enforces single-task delegation", failures)
        ok("并行前必须先做独立性判定" in text or ("并行" in text and "独立性" in text), f"{label} requires independence checks before parallel work", failures)
        ok("反重复规则" in text and "不重复" in text, f"{label} forbids duplicating delegated work", failures)
        ok("不能直接信任" in text or "不要把摘要当证据" in text, f"{label} requires verification instead of trusting delegated summaries", failures)
        ok("targets/" in text, f"{label} pushes platform-specific APIs into target adapters", failures)
        ok(".research/orchestration-note.md" in text, f"{label} uses a project-local default orchestration output path", failures)
        ok("references/delegation-template.md" in text, f"{label} links to the reusable delegation template", failures)
        ok((skill_path.parent / "references" / "delegation-template.md").is_file(), "delegation template reference exists for agent-orchestration", failures)
    if skill_name == "learning-capture":
        ok("手工触发" in text or "手动触发" in text, f"{label} is explicitly manual-triggered", failures)
        ok("hooks" in text and "不依赖 hooks" in text, f"{label} explicitly avoids hook-dependent automation", failures)
        ok(all(token in text for token in (".learned/notes.md", ".learned/rules.md")), f"{label} defines project-local fallback learning output paths", failures)
        ok(all(token in text for token in ("keep-local", "promote-later", "propose-agents-update", "drop")), f"{label} defines learning follow-up states", failures)
        ok("references/templates.md" in text, f"{label} links to the reusable learning templates", failures)
        ok("rules.md" in text and "AGENTS.md" in text, f"{label} captures project-level rule candidates and AGENTS update proposals", failures)
        ok(".learned/" in text and "不要把 `nanospec` 当成学习记录的默认载体" in text, f"{label} keeps .learned as the default learning sink instead of nanospec", failures)
        ok((skill_path.parent / "references" / "templates.md").is_file(), "templates reference exists for learning-capture", failures)
    if skill_name == "spec-driven":
        ok("alignment.md" in text and "outputs/3-tasks.md" in text, f"{label} centers alignment propagation and shared task tracking", failures)
        ok("只提供“目录规范 + align”" in text or "只提供“目录规范 + align" in text, f"{label} stays focused on directory structure and align only", failures)
        ok("不负责内置流程阶段" in text and "不提供 `init`" in text, f"{label} explicitly avoids built-in phase routing", failures)
        ok("其他 skill" in text and "共享工作面" in text, f"{label} positions other skills as the phase executors", failures)
        ok("`/init`" not in text and "`/run`" not in text, f"{label} does not document slash-command routing", failures)


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

    for heading in ("## Asset Under Test", "## Capability Evals", "## Regression Evals", "## Exit Criteria"):
        ok(heading in text, f"{label} contains heading: {heading}", failures)


def compare_directory_contents(source_dir: Path, target_dir: Path, label: str, failures: list[str]) -> None:
    source_files = sorted(path.relative_to(source_dir) for path in source_dir.rglob("*") if path.is_file())
    target_files = sorted(path.relative_to(target_dir) for path in target_dir.rglob("*") if path.is_file()) if target_dir.is_dir() else []
    ok(source_files == target_files, f"{label} file set matches source", failures)


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
        ok("skills/" in agents_text and "agents/" in agents_text and "commands/" in agents_text, "targets/codex AGENTS.md describes flat distribution assets", failures)
        ok("src/domains/" in agents_text, "targets/codex AGENTS.md maps Codex behavior back to domain source assets", failures)
        ok("config.toml" in agents_text and ".codex/agents/" in agents_text, "targets/codex AGENTS.md explains config-to-agent-role wiring", failures)
        ok("quality_code_reviewer" in agents_text and "agents/quality-code-reviewer.md" in agents_text, "targets/codex AGENTS.md documents the quality-code-reviewer role mapping", failures)
    if reviewer_path.is_file():
        reviewer_text = read_text(reviewer_path)
        ok("agents/quality-code-reviewer.md" in reviewer_text or "src/domains/quality/agents/quality-code-reviewer.md" in reviewer_text, "targets/codex reviewer role aligns with the reusable reviewer prompt", failures)
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

    for name, source_dir in collect_skill_dirs_by_name().items():
        compare_directory_contents(source_dir, codex_root / "skills" / name, f"targets/codex skill mirror matches src domain asset: {name}", failures)

    source_skill_names = sorted(collect_skill_dirs_by_name())
    target_skill_names = sorted(path.name for path in (codex_root / "skills").iterdir() if path.is_dir()) if (codex_root / "skills").is_dir() else []
    ok(source_skill_names == target_skill_names, "targets/codex skills contain the same asset names as src domains", failures)

    source_agents = collect_asset_files_by_name("agents")
    target_agents = sorted(path.stem for path in (codex_root / "agents").glob("*.md"))
    ok(sorted(source_agents) == target_agents, "targets/codex agents contain the same asset names as src domains", failures)
    for name, source_path in source_agents.items():
        target_path = codex_root / "agents" / f"{name}.md"
        ok(target_path.is_file(), f"targets/codex agent exists: {target_path.relative_to(ROOT)}", failures)
        if target_path.is_file():
            ok(read_text(source_path) == read_text(target_path), f"targets/codex agent content matches src domain asset: {name}", failures)

    source_commands = collect_asset_files_by_name("commands")
    target_commands = sorted(path.stem for path in (codex_root / "commands").glob("*.md"))
    ok(sorted(source_commands) == target_commands, "targets/codex commands contain the same asset names as src domains", failures)
    if not source_commands:
        ok((codex_root / "commands" / ".gitkeep").is_file(), "targets/codex commands keeps .gitkeep when empty", failures)


def main() -> int:
    failures: list[str] = []

    validate_repo_layout(failures)

    domain_dirs = collect_domains()
    ok(bool(domain_dirs), "at least one domain exists", failures)
    for domain_dir in domain_dirs:
        validate_domain_layout(domain_dir, failures)

    skill_files = collect_skill_files()
    ok(bool(skill_files), "at least one skill exists", failures)
    for skill_file in skill_files:
        validate_skill(skill_file, failures)

    agent_files = collect_agent_files()
    for agent_file in agent_files:
        validate_agent(agent_file, failures)

    command_files = collect_command_files()
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
