# Codex Adapter Notes

- `packages/quality-workflows/targets/codex/skills/quality-*` 是分发平铺副本
- `packages/quality-workflows/targets/codex/agents/quality-code-reviewer.md` 是 reviewer 正文
- `.codex/config.toml` 负责注册 `quality_code_reviewer` 角色
- `.codex/agents/quality-code-reviewer.toml` 负责挂载四个质量 skill
