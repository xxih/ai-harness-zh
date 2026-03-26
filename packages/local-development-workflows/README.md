# local-development-workflows 包

这个包承载面向本地开发阶段的默认工作流约定。

## 组成

- `skills/local-development-workflow/`
  - 本地开发默认主线 skill
- `references/default-local-development-workflow.md`
  - 本地开发默认主线
- `references/local-review-trigger-rules.md`
  - local review 的触发条件、非触发条件与最小执行要求
- `targets/codex/`
  - `local-development-workflows` 的 Codex target 包

## 包边界

- 这里处理的是本地开发阶段如何推进，不处理 GitHub 远端 PR 生命周期动作
- 这里负责把 `spec-driven`、`search-first`、TDD、alignment、local review、verify、finish 串成一条默认主线
- 远端 PR / comments / checks / merge，继续交给 `packages/github-workflows/`
- TDD、review、verify 这些原子质量动作本身，继续由 `packages/quality-workflows/` 承担
- worktree 建立与分支收尾，继续由 `packages/git-workflows/` 承担

## 维护方式

- 先更新 `skills/` 与 `references/`
- 再运行 `python3 scripts/sync_codex_targets.py local-development-workflows`
