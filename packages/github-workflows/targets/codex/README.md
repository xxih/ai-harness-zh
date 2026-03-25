# Codex Target 包

这个目录提供 `github-workflows` 的 Codex 分发副本。

## 组成

- `skills/pr-lifecycle/`
- `skills/merge-conflict-resolution/`

## 维护方式

- 先更新 `packages/github-workflows/` 下的 source 资产
- 再运行 `python3 scripts/sync_codex_targets.py github-workflows`
- `targets/codex/README.md` 属于 target 侧说明文件，保留手工维护
