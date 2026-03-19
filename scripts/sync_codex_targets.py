#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

MIRROR_DIRS = ("skills", "agents", "commands")
MIRROR_FILES = ("_AGENTS.md",)


def remove_path(path: Path) -> None:
    if not path.exists():
        return
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink()


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def sync_package(package_dir: Path) -> tuple[bool, str]:
    target_dir = package_dir / "targets" / "codex"
    if not target_dir.exists():
        return False, "skip: no targets/codex"

    mirrored: list[str] = []

    for dirname in MIRROR_DIRS:
        src = package_dir / dirname
        dst = target_dir / dirname
        if src.exists():
            copy_tree(src, dst)
            mirrored.append(dirname)
        else:
            remove_path(dst)

    for filename in MIRROR_FILES:
        src = package_dir / filename
        dst = target_dir / filename
        if src.exists():
            shutil.copy2(src, dst)
            mirrored.append(filename)
        else:
            remove_path(dst)

    if mirrored:
        return True, "synced: " + ", ".join(mirrored)
    return True, "synced: no mirrorable source assets"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync package source assets into packages/*/targets/codex."
    )
    parser.add_argument(
        "packages",
        nargs="*",
        help="Optional package names. Defaults to every package under packages/.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    packages_root = Path("packages")
    if not packages_root.exists():
        raise SystemExit("packages/ does not exist")

    if args.packages:
        package_dirs = [packages_root / name for name in args.packages]
    else:
        package_dirs = sorted(
            path for path in packages_root.iterdir() if path.is_dir() and not path.name.startswith(".")
        )

    missing = [path.name for path in package_dirs if not path.exists()]
    if missing:
        raise SystemExit("Unknown package(s): " + ", ".join(sorted(missing)))

    for package_dir in package_dirs:
        changed, message = sync_package(package_dir)
        status = "OK" if changed else "SKIP"
        print(f"[{status}] {package_dir.name}: {message}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
