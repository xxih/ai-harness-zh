# Codex Target 包

这个目录提供 `git-workflows` 的 Codex 分发副本。

## 组成

- `skills/using-git-worktrees/`
  - Codex 侧的隔离 worktree 建立能力
- `skills/finishing-a-development-branch/`
  - Codex 侧的分支收尾与清理能力

## 维护方式

- 先更新 `packages/git-workflows/` 下的 source 资产
- 再运行 `python3 scripts/sync_codex_targets.py git-workflows`
- `targets/codex/README.md` 属于 target 侧说明文件，保留手工维护
