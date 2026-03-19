# spec-driven 包

这个包承载 `spec-driven` 工作流能力。

## 组成

- `skills/spec-driven/`
  - `spec-driven` skill source
- `targets/codex/`
  - `spec-driven` 的 Codex target 包

## 维护方式

- 先更新 `skills/spec-driven/`
- 再运行 `python3 scripts/sync_codex_targets.py spec-driven`
