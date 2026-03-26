# Codex Target 包

这个目录提供 `local-development-workflows` 的 Codex 分发副本。

## 组成

- `skills/local-development-workflow/`

## 维护方式

- 先更新 `packages/local-development-workflows/` 下的 source 资产
- 再运行 `python3 scripts/sync_codex_targets.py local-development-workflows`
- `targets/codex/README.md` 属于 target 侧说明文件，保留手工维护
