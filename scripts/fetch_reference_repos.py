#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

PROXY_ENV_KEYS = (
    "http_proxy",
    "https_proxy",
    "all_proxy",
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "wss_proxy",
    "WSS_PROXY",
)

GITHUB_SSH_PATTERNS = (
    re.compile(r"^git@github\.com:(?P<path>.+?)(?:\.git)?$"),
    re.compile(r"^ssh://git@github\.com/(?P<path>.+?)(?:\.git)?$"),
)


@dataclass
class FetchResult:
    repo: str
    ok: bool
    mode: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch reference repositories under references/repos with network-safe defaults: "
            "clear proxy env vars first, and fall back from GitHub SSH remotes to temporary HTTPS."
        )
    )
    parser.add_argument(
        "repos",
        nargs="*",
        help="Optional repo names under references/repos/. Defaults to every repo there.",
    )
    parser.add_argument(
        "--keep-proxy",
        action="store_true",
        help="Keep ambient proxy environment variables instead of clearing them before fetch.",
    )
    parser.add_argument(
        "--no-https-fallback",
        action="store_true",
        help="Do not retry GitHub SSH remotes over temporary HTTPS.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only print planned fetch mode per repo without executing git fetch.",
    )
    return parser.parse_args()


def list_repo_dirs(root: Path, names: list[str]) -> list[Path]:
    if names:
        repo_dirs = [root / name for name in names]
    else:
        repo_dirs = sorted(path for path in root.iterdir() if path.is_dir() and (path / ".git").exists())

    missing = [path.name for path in repo_dirs if not path.exists()]
    if missing:
        raise SystemExit("Unknown reference repo(s): " + ", ".join(sorted(missing)))

    not_git = [path.name for path in repo_dirs if not (path / ".git").exists()]
    if not_git:
        raise SystemExit("Not a git repo under references/repos/: " + ", ".join(sorted(not_git)))

    return repo_dirs


def build_env(keep_proxy: bool) -> dict[str, str]:
    env = dict(os.environ)
    if not keep_proxy:
        for key in PROXY_ENV_KEYS:
            env.pop(key, None)
    return env


def run_git(
    repo_dir: Path,
    env: dict[str, str],
    *,
    remote_url_override: str | None = None,
    dry_run: bool = False,
) -> tuple[bool, str]:
    cmd = ["git", "-C", str(repo_dir), "fetch", "--prune"]
    if remote_url_override is None:
        cmd.append("origin")
    else:
        cmd.append(remote_url_override)
        cmd.extend(get_origin_fetch_refspecs(repo_dir))

    if dry_run:
        return True, "DRY-RUN " + " ".join(cmd)

    completed = subprocess.run(
        cmd,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    output = (completed.stdout + completed.stderr).strip()
    return completed.returncode == 0, output


def get_origin_url(repo_dir: Path) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo_dir), "remote", "get-url", "origin"],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise SystemExit(f"Failed to read origin URL for {repo_dir.name}: {completed.stderr.strip()}")
    return completed.stdout.strip()


def get_origin_fetch_refspecs(repo_dir: Path) -> list[str]:
    completed = subprocess.run(
        ["git", "-C", str(repo_dir), "config", "--get-all", "remote.origin.fetch"],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise SystemExit(
            f"Failed to read fetch refspecs for {repo_dir.name}: {completed.stderr.strip()}"
        )
    refspecs = [line.strip() for line in completed.stdout.splitlines() if line.strip()]
    if not refspecs:
        raise SystemExit(f"No remote.origin.fetch refspecs configured for {repo_dir.name}")
    return refspecs


def github_https_url(origin_url: str) -> str | None:
    for pattern in GITHUB_SSH_PATTERNS:
        match = pattern.match(origin_url)
        if match:
            return f"https://github.com/{match.group('path')}.git"
    return None


def summarize_output(output: str) -> str:
    cleaned = " ".join(line.strip() for line in output.splitlines() if line.strip())
    return cleaned[:240] if len(cleaned) > 240 else cleaned


def fetch_repo(
    repo_dir: Path,
    *,
    keep_proxy: bool,
    no_https_fallback: bool,
    dry_run: bool,
) -> FetchResult:
    repo = repo_dir.name
    origin_url = get_origin_url(repo_dir)
    env = build_env(keep_proxy=keep_proxy)
    fallback_url = None if no_https_fallback else github_https_url(origin_url)

    remote_url_override = fallback_url if fallback_url is not None else None
    ok, output = run_git(
        repo_dir,
        env,
        remote_url_override=remote_url_override,
        dry_run=dry_run,
    )
    if ok:
        mode = "fetch"
        if not keep_proxy:
            mode = "fetch-no-proxy"
        if remote_url_override is not None:
            mode += "+https-fallback"
        return FetchResult(repo=repo, ok=True, mode=mode, detail=summarize_output(output) or "ok")

    return FetchResult(repo=repo, ok=False, mode="fetch-failed", detail=summarize_output(output))


def main() -> int:
    args = parse_args()
    repos_root = Path("references/repos")
    if not repos_root.exists():
        raise SystemExit("references/repos does not exist")

    repo_dirs = list_repo_dirs(repos_root, args.repos)
    results = [
        fetch_repo(
            repo_dir,
            keep_proxy=args.keep_proxy,
            no_https_fallback=args.no_https_fallback,
            dry_run=args.dry_run,
        )
        for repo_dir in repo_dirs
    ]

    failures = [result for result in results if not result.ok]
    for result in results:
        status = "OK" if result.ok else "FAIL"
        print(f"[{status}] {result.repo}: {result.mode}")
        if result.detail:
            print(f"  {result.detail}")

    print(
        f"\nSummary: {len(results) - len(failures)} succeeded, {len(failures)} failed, total {len(results)}."
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
