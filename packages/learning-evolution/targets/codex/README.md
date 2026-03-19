# learning-evolution Codex target

这个目录提供 `learning-evolution` 的 Codex 分发副本。

## 组成

- `_AGENTS.md`
  - 载体块正文默认独立成立，直接写清出口判断、写入位置、写入内容和默认动作
- `skills/learning-evolution/`

## 维护

- 源资产变更后，先更新 `packages/learning-evolution/skills/` 与 `_AGENTS.md`
- 再运行 `python3 scripts/sync_codex_targets.py learning-evolution`
