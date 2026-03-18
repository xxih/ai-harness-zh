#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS_ROOT = ROOT / 'references' / 'translations'


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(65536), b''):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest(repo_name: str) -> tuple[Path, dict]:
    manifest_path = TRANSLATIONS_ROOT / repo_name / 'manifest.json'
    if not manifest_path.is_file():
        raise FileNotFoundError(f'missing manifest: {manifest_path.relative_to(ROOT)}')
    return manifest_path, json.loads(manifest_path.read_text(encoding='utf-8'))


def discover_repo_names(selected: list[str]) -> list[str]:
    if selected:
        return selected
    return sorted(path.name for path in TRANSLATIONS_ROOT.iterdir() if (path / 'manifest.json').is_file())


def run_git(repo_root: Path, *args: str) -> str:
    result = subprocess.run(
        ['git', '-C', str(repo_root), *args],
        capture_output=True,
        check=True,
        text=True,
    )
    return result.stdout.strip()


def tracked_source_files(repo_root: Path, include_patterns: list[str]) -> list[str]:
    files: set[str] = set()
    for pattern in include_patterns:
        for path in repo_root.glob(pattern):
            if path.is_file():
                files.add(path.relative_to(repo_root).as_posix())
    return sorted(files)


def refresh_repo(repo_name: str, manifest: dict) -> None:
    source = manifest['source']
    repo_root = ROOT / source['path']
    branch = source.get('branch') or run_git(repo_root, 'branch', '--show-current')
    dirty = run_git(repo_root, 'status', '--porcelain')
    if dirty:
        raise RuntimeError(f'{repo_name}: reference repo has local changes, cannot fast-forward safely')
    run_git(repo_root, 'fetch', '--quiet', 'origin', branch)
    run_git(repo_root, 'merge', '--ff-only', 'FETCH_HEAD')


def check_repo(repo_name: str, manifest: dict) -> int:
    source = manifest['source']
    repo_root = ROOT / source['path']
    translation_root = TRANSLATIONS_ROOT / repo_name
    expected_sources = tracked_source_files(repo_root, manifest['scope']['include'])
    entries = {entry['source']: entry for entry in manifest.get('translations', [])}

    current_head = run_git(repo_root, 'rev-parse', 'HEAD')
    recorded_head = source.get('head_commit', '')
    repo_moved = current_head != recorded_head

    missing_entries = [path for path in expected_sources if path not in entries]
    extra_entries = [path for path in entries if path not in expected_sources]
    changed_entries: list[str] = []
    missing_translations: list[str] = []
    missing_sources: list[str] = []

    for source_rel, entry in sorted(entries.items()):
        source_path = repo_root / source_rel
        translation_path = translation_root / entry['translation']
        if not source_path.is_file():
            missing_sources.append(source_rel)
            continue
        if not translation_path.is_file():
            missing_translations.append(entry['translation'])
            continue
        current_hash = sha256_file(source_path)
        if current_hash != entry.get('source_sha256'):
            changed_entries.append(source_rel)

    print(f'[{repo_name}]')
    print(f"  repo: {source['path']}")
    print(f"  recorded head: {recorded_head or '(missing)'}")
    print(f'  current head:  {current_head}')

    issues = 0
    if repo_moved:
        issues += 1
        print('  status: upstream head changed since last snapshot')
    else:
        print('  status: upstream head unchanged')

    if changed_entries:
        issues += len(changed_entries)
        print('  changed source files:')
        for item in changed_entries:
            print(f'    - {item}')
    elif repo_moved:
        print('  tracked source files: no content drift in current translation scope')
    else:
        print('  tracked source files: up to date')

    if missing_entries:
        issues += len(missing_entries)
        print('  missing manifest entries:')
        for item in missing_entries:
            print(f'    - {item}')

    if extra_entries:
        issues += len(extra_entries)
        print('  stale manifest entries:')
        for item in extra_entries:
            print(f'    - {item}')

    if missing_translations:
        issues += len(missing_translations)
        print('  missing translation files:')
        for item in missing_translations:
            print(f'    - {item}')

    if missing_sources:
        issues += len(missing_sources)
        print('  missing source files:')
        for item in missing_sources:
            print(f'    - {item}')

    if issues == 0:
        print('  result: OK')
        return 0

    print('  result: STALE')
    return 1


def snapshot_repo(repo_name: str, manifest_path: Path, manifest: dict) -> int:
    source = manifest['source']
    repo_root = ROOT / source['path']
    translation_root = manifest_path.parent
    branch = run_git(repo_root, 'branch', '--show-current')
    remote = run_git(repo_root, 'remote', 'get-url', 'origin')
    head_commit = run_git(repo_root, 'rev-parse', 'HEAD')
    expected_sources = tracked_source_files(repo_root, manifest['scope']['include'])

    missing_translations: list[str] = []
    translations: list[dict[str, str]] = []
    for source_rel in expected_sources:
        translation_rel = source_rel
        translation_path = translation_root / translation_rel
        if not translation_path.is_file():
            missing_translations.append(translation_rel)
            continue
        translations.append(
            {
                'source': source_rel,
                'translation': translation_rel,
                'source_sha256': sha256_file(repo_root / source_rel),
            }
        )

    if missing_translations:
        print(f'[{repo_name}] missing translation files, snapshot aborted:')
        for item in missing_translations:
            print(f'  - {item}')
        return 1

    manifest['source']['branch'] = branch
    manifest['source']['remote'] = remote
    manifest['source']['head_commit'] = head_commit
    manifest['translations'] = translations
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'[{repo_name}] snapshot updated at {manifest_path.relative_to(ROOT)}')
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Check or refresh tracked prompt translations for reference repositories.'
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    check_parser = subparsers.add_parser('check', help='check whether translations are stale')
    check_parser.add_argument('repos', nargs='*', help='repo names under references/translations/')
    check_parser.add_argument(
        '--pull',
        action='store_true',
        help='fetch and fast-forward the reference repo before checking',
    )

    snapshot_parser = subparsers.add_parser('snapshot', help='refresh manifest hashes after sync')
    snapshot_parser.add_argument('repos', nargs='*', help='repo names under references/translations/')
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    repo_names = discover_repo_names(getattr(args, 'repos', []))
    if not repo_names:
        print('No translation manifests found under references/translations/')
        return 1

    exit_code = 0
    for repo_name in repo_names:
        try:
            manifest_path, manifest = load_manifest(repo_name)
            if args.command == 'check':
                if args.pull:
                    refresh_repo(repo_name, manifest)
                exit_code = max(exit_code, check_repo(repo_name, manifest))
            elif args.command == 'snapshot':
                exit_code = max(exit_code, snapshot_repo(repo_name, manifest_path, manifest))
        except Exception as exc:
            print(f'[{repo_name}] ERROR: {exc}')
            exit_code = 1

    return exit_code


if __name__ == '__main__':
    sys.exit(main())
