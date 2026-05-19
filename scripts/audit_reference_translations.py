#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ManifestIssue:
    kind: str
    detail: str
    resolved: bool = False


@dataclass
class RepoAudit:
    repo: str
    manifest_path: Path
    updated: bool
    issues: list[ManifestIssue]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Audit references/translations manifests against local source repos. "
            "Reports missing source coverage, missing translation files, and stale source_sha256 values."
        )
    )
    parser.add_argument(
        "repos",
        nargs="*",
        help="Optional repo names under references/translations/. Defaults to every manifest there.",
    )
    parser.add_argument(
        "--write-sha",
        action="store_true",
        help="Rewrite stale source_sha256 values in manifest.json to match the current local source repo.",
    )
    return parser.parse_args()


def list_manifest_paths(root: Path, repos: list[str]) -> list[Path]:
    if repos:
        manifest_paths = [root / repo / "manifest.json" for repo in repos]
    else:
        manifest_paths = sorted(root.glob("*/manifest.json"))

    missing = [str(path.parent.name) for path in manifest_paths if not path.exists()]
    if missing:
        raise SystemExit("Unknown translation repo(s): " + ", ".join(sorted(missing)))

    return manifest_paths


def matched_source_files(source_root: Path, patterns: list[str]) -> list[str]:
    matched: set[str] = set()
    for pattern in patterns:
        for path in source_root.glob(pattern):
            if path.is_file():
                matched.add(str(path.relative_to(source_root)))
    return sorted(matched)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_manifest(manifest_path: Path, *, write_sha: bool) -> RepoAudit:
    data = json.loads(manifest_path.read_text())
    repo = data["repo"]
    source_root = Path(data["source"]["path"])
    if not source_root.exists():
        raise SystemExit(f"Missing source repo for {repo}: {source_root}")

    issues: list[ManifestIssue] = []
    updated = False

    translations = data.get("translations", [])
    tracked_sources = {item["source"] for item in translations if item.get("source")}
    for source in matched_source_files(source_root, data.get("scope", {}).get("include", [])):
        if source not in tracked_sources:
            issues.append(ManifestIssue("missing-source-entry", source))

    for item in translations:
        translation_path = manifest_path.parent / item["translation"]
        if not translation_path.exists():
            issues.append(ManifestIssue("missing-translation-file", item["translation"]))

        source = item.get("source")
        recorded_sha = item.get("source_sha256")
        if not source or not recorded_sha:
            continue

        source_path = source_root / source
        if not source_path.exists():
            issues.append(ManifestIssue("missing-source-file", source))
            continue

        current_sha = sha256(source_path)
        if current_sha != recorded_sha:
            if write_sha:
                item["source_sha256"] = current_sha
                updated = True
                issues.append(
                    ManifestIssue(
                        "updated-source-sha",
                        f"{source}: {recorded_sha} -> {current_sha}",
                        resolved=True,
                    )
                )
            else:
                issues.append(
                    ManifestIssue(
                        "stale-source-sha",
                        f"{source}: {recorded_sha} -> {current_sha}",
                    )
                )

    if updated:
        manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

    return RepoAudit(
        repo=repo,
        manifest_path=manifest_path,
        updated=updated,
        issues=issues,
    )


def main() -> int:
    args = parse_args()
    translations_root = Path("references/translations")
    if not translations_root.exists():
        raise SystemExit("references/translations does not exist")

    audits = [
        audit_manifest(manifest_path, write_sha=args.write_sha)
        for manifest_path in list_manifest_paths(translations_root, args.repos)
    ]

    issue_count = 0
    updated_count = 0
    for audit in audits:
        status = "OK"
        unresolved_issues = [issue for issue in audit.issues if not issue.resolved]
        if unresolved_issues:
            status = "ISSUES"
            issue_count += len(unresolved_issues)
        if audit.updated:
            updated_count += 1
            status += "+UPDATED" if status != "OK" else "UPDATED"
        print(f"[{status}] {audit.repo}")
        for issue in audit.issues:
            print(f"  - {issue.kind}: {issue.detail}")

    print(
        f"\nSummary: {len(audits)} manifests checked, {updated_count} updated, {issue_count} issue(s) found."
    )
    return 1 if issue_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
