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
- skill 正文默认把记录写到仓库根目录 `.quality/`
- Codex target 镜像通过 `python3 scripts/sync_codex_targets.py quality-workflows` 同步
