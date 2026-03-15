#!/usr/bin/env python3

from __future__ import annotations

import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = ROOT / "src"
TARGETS_ROOT = ROOT / "targets"


def replace_tree(source: Path, destination: Path) -> None:
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)


def sync_codex() -> None:
    codex_root = TARGETS_ROOT / "codex"
    replace_tree(SRC_ROOT / "skills", codex_root / "skills")
    replace_tree(SRC_ROOT / "agents", codex_root / "agents")
    replace_tree(SRC_ROOT / "commands", codex_root / "commands")


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
