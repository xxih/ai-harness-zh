# Codex Target 包

这个目录提供 `learning-capture` 的 Codex 分发副本。

## 组成

- `_AGENTS.md`
  - 分发侧搭配上下文
- `skills/learning-capture/`
  - Codex 侧平铺 skill

## 维护方式

- 源资产变更后，先更新 `packages/learning-capture/skills/` 与 `_AGENTS.md`
- 再运行 `python3 scripts/sync_codex_targets.py learning-capture`
