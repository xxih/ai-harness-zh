# agent-orchestration 包

这个包承载多 agent 协作与委派编排能力。

## 组成

- `skills/agent-orchestration/`
  - `agent-orchestration` skill source
- `targets/codex/`
  - `agent-orchestration` 的 Codex target 包

## 维护方式

- 先更新 `skills/agent-orchestration/`
- 再运行 `python3 scripts/sync_codex_targets.py agent-orchestration`
