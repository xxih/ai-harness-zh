# Codex Target 包

这个目录提供 `search-first` 的 Codex 分发副本。

## 组成

- `skills/search-first/`
  - 由 package source 同步过来的 skill 目录

## 维护方式

- 先更新 `packages/search-first/skills/search-first/`
- 再运行 `python3 scripts/sync_codex_targets.py search-first`
