# quality-workflows 包

这个包承载一组可独立使用的质量工作流资产。

## 组成

- `skills/quality-tdd/`
- `skills/quality-verify/`
- `skills/quality-review/`
- `skills/quality-review-feedback/`
- `agents/quality-code-reviewer.md`
- `targets/codex/`
  - 面向 Codex 的最小 target 包与 reviewer 角色配置

## 包边界

- 这里保留四个真正有独立动作边界的 quality skill
- `quality-router` 已删除，不再作为独立资产保留
- 这里负责质量判断、评审门禁与反馈处理，不负责 GitHub 远端 PR 生命周期动作
- PR 创建、远端 comments、checks、merge 与冲突处理，交给 `packages/github-workflows/`
- skill 正文默认把记录写到仓库根目录 `.quality/`
- Codex target 镜像通过 `python3 scripts/sync_codex_targets.py quality-workflows` 同步
