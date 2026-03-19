# Codex Adapter Notes

## Source Of Truth

- 当前共享源资产在 `src/domains/<domain>/skills/`、`src/domains/<domain>/agents/`、`src/domains/<domain>/commands/`
- `targets/codex/skills/`、`targets/codex/agents/`、`targets/codex/commands/` 是这些共享资产的分发快照
- `packages/<package>/targets/codex/` 负责各自主题包的专属 Codex target 包
- 需要更新共享资产正文时，回到 `src/domains/` 修改；需要更新某个主题包时，回到对应 `packages/<package>/` 修改

## Multi-Agent Mapping

- `config.toml` 中的 `[agents.<name>]` 决定当前共享包里 Codex 可调用的角色
- 每个角色的具体行为定义在 `.codex/agents/*.toml`
- 包内独立角色应在各自 `packages/<package>/targets/codex/.codex/` 维护，不再混入根级共享配置
