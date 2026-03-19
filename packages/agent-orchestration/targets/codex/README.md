# Codex Target 包

这个目录提供 `agent-orchestration` 的 Codex 分发副本。

## 组成

- `skills/agent-orchestration/`
  - 由 package source 同步过来的 skill 目录

## 维护方式

- 先更新 `packages/agent-orchestration/skills/agent-orchestration/`
- 再运行 `python3 scripts/sync_codex_targets.py agent-orchestration`
