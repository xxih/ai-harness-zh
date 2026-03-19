# search-first 包

这个包承载 `search-first` 工作流能力。

## 组成

- `skills/search-first/`
  - `search-first` skill source
- `targets/codex/`
  - `search-first` 的 Codex target 包

## 维护方式

- 先更新 `skills/search-first/`
- 再运行 `python3 scripts/sync_codex_targets.py search-first`
