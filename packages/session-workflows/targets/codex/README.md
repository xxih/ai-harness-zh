# session-workflows Codex target

这个目录提供 `session-workflows` 的 Codex 分发副本。

## 组成

- `skills/session-handoff/`

## 维护方式

- 先更新 `packages/session-workflows/` 下的 source 资产
- 再运行 `python3 scripts/sync_codex_targets.py session-workflows`
- `targets/codex/README.md` 属于 target 侧说明文件，保留手工维护
