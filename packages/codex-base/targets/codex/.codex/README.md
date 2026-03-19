# Codex Adapter Notes

## Source Of Truth

- 各个 `packages/<package>/` 是仓库自有资产的 source of truth
- `packages/<package>/targets/codex/` 负责各自主题包的专属 Codex target 包
- 需要更新具体能力时，回到对应 package 修改；其中镜像型 target 默认通过 `scripts/sync_codex_targets.py` 同步

## Multi-Agent Mapping

- `config.toml` 中的 `[agents.<name>]` 决定当前 Codex 基线包里可调用的角色
- 每个角色的具体行为定义在 `.codex/agents/*.toml`
- 包内独立角色应在各自 `packages/<package>/targets/codex/.codex/` 维护，不再混入根级共享配置
