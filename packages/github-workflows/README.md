# github-workflows 包

这个包承载面向 GitHub / PR 生命周期的远端工作流能力。

## 组成

- `skills/pr-lifecycle/`
  - 统一入口；按意图路由到 create / review / comments / checks / merge 等原子动作
- `skills/merge-conflict-resolution/`
  - 处理 rebase / merge / update branch 产生的冲突
- `targets/codex/`
  - `github-workflows` 的 Codex target 包

## 包边界

- 这里处理的是远端 PR 生命周期，不处理本地 worktree 建立
- 这里负责“去 GitHub / gh / MCP 拿信息并执行动作”，不替代质量判断本身
- `pr-lifecycle` 是入口 skill，不默认自动跑完整闭环；执行哪些动作取决于当前意图
- 代码评审、评审反馈判断、完成前验证这些质量内核，继续由 `quality-workflows` 承担
- 本地 branch / worktree 生命周期，继续由 `git-workflows` 承担

## 默认记录位置

- 若当前任务已有自己的记录文件，优先回写到当前任务记录
- 若没有既定记录位置，默认写入 `.quality/pr-lifecycle.md`

## 维护方式

- 先更新 `skills/`
- 再运行 `python3 scripts/sync_codex_targets.py github-workflows`
