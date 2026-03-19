# Codex Target 包

这个目录提供 `quality-workflows` 的 Codex 分发副本。

## 组成

- `skills/quality-*`
  - Codex 侧平铺 quality skills
- `agents/quality-code-reviewer.md`
  - 独立 reviewer agent
- `.codex/config.toml`
  - 注册 `quality_code_reviewer` 角色
- `.codex/agents/quality-code-reviewer.toml`
  - reviewer 角色的运行配置与挂载 skill

## 维护方式

- 先更新 `packages/quality-workflows/` 下的 source 资产
- 再运行 `python3 scripts/sync_codex_targets.py quality-workflows`
- `.codex/` 目录保留为 target 侧手写 runtime 文件，不由脚本覆盖
