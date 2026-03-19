# writing-skills 包

这个包承载 skill 资产编写与重构能力。

## 组成

- `skills/writing-skills/`
  - `writing-skills` skill source
- `targets/codex/`
  - `writing-skills` 的 Codex target 包

## 维护方式

- 先更新 `skills/writing-skills/`
- 再运行 `python3 scripts/sync_codex_targets.py writing-skills`
