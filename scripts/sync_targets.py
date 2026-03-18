#!/usr/bin/env python3

from __future__ import annotations

import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOMAINS_ROOT = ROOT / "src" / "domains"
TARGETS_ROOT = ROOT / "targets"


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def collect_skill_dirs() -> dict[str, Path]:
    assets: dict[str, Path] = {}
    for skill_path in sorted(DOMAINS_ROOT.glob("*/skills/*/SKILL.md")):
        name = skill_path.parent.name
        if name in assets:
            raise ValueError(f"Duplicate skill name across domains: {name}")
        assets[name] = skill_path.parent
    return assets


def collect_asset_files(kind: str) -> dict[str, Path]:
    assets: dict[str, Path] = {}
    for path in sorted(DOMAINS_ROOT.glob(f"*/{kind}/*.md")):
        name = path.stem
        if name in assets:
            raise ValueError(f"Duplicate {kind[:-1]} name across domains: {name}")
        assets[name] = path
    return assets


def sync_codex() -> None:
    codex_root = TARGETS_ROOT / "codex"
    skills_root = codex_root / "skills"
    agents_root = codex_root / "agents"
    commands_root = codex_root / "commands"

    reset_dir(skills_root)
    reset_dir(agents_root)
    reset_dir(commands_root)

    for name, source_dir in collect_skill_dirs().items():
        shutil.copytree(source_dir, skills_root / name)

    for name, source_path in collect_asset_files("agents").items():
        shutil.copy2(source_path, agents_root / f"{name}.md")

    commands = collect_asset_files("commands")
    for name, source_path in commands.items():
        shutil.copy2(source_path, commands_root / f"{name}.md")

    if not commands:
        (commands_root / ".gitkeep").write_text("", encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/sync_targets.py <target>")
        return 1

    target = sys.argv[1]
    if target == "codex":
        sync_codex()
        print("Synced target: codex")
        return 0

    print(f"Unknown target: {target}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
