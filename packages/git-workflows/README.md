# git-workflows 包

这个包承载与 git 工作区隔离、分支收尾和 worktree 生命周期相关的工作流能力。

## 组成

- `skills/using-git-worktrees/`
  - 建立隔离 worktree、校验 ignore、确认 baseline
- `skills/finishing-a-development-branch/`
  - 在实现完成后做验证、选择出口、处理分支与 worktree 清理
- `targets/codex/`
  - `git-workflows` 的 Codex target 包

## 设计边界

- 关注 git 工作区生命周期，不承担多 agent 编排本身
- 关注“完成后如何收尾”，不替代质量验证或代码评审 skill
- 关注本地 branch / worktree 生命周期，不处理 GitHub 远端 PR comments、checks 或 merge 执行面
- 默认保持平台无关；PR / MR、审批和运行时细节由具体 target 或当前会话决定

## 维护方式

- 先更新 `skills/`
- 再运行 `python3 scripts/sync_codex_targets.py git-workflows`
