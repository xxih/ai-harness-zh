# Codex Adapter Notes

这份文件补充仓库根目录的 `AGENTS.md`，并衔接 `src/` 内各领域的 `_AGENTS.md`；如果需要目录导览，再回看对应 `README.md`。这里只描述 Codex 适配层的特定约定。

## Source Of Truth

- 核心源资产在 `src/domains/<domain>/skills/`、`src/domains/<domain>/agents/`、`src/domains/<domain>/commands/`
- `targets/codex/skills/`、`targets/codex/agents/`、`targets/codex/commands/` 是从 `src/domains/*` 收集并平铺出的分发快照
- `targets/codex/.codex/` 负责 Codex 的运行配置与角色注册
- 需要更新资产正文时，回到 `src/domains/` 修改，再重新同步到 `targets/codex/`

## Multi-Agent Mapping

- `config.toml` 中的 `[agents.<name>]` 决定 Codex 可调用的角色
- 每个角色的具体行为定义在 `.codex/agents/*.toml`
- 若某个角色需要仓库内的可复用 prompt，应优先引用同级分发快照；需要回源时再引用 `src/domains/`
- `targets/codex/agents/*.md` 是分发出去的 agent 正文；只有被注册进 `config.toml` 的那部分，才是 Codex 运行时可直接调用的角色
- agent 文件名、角色名和 TOML 文件名不必完全同名，但必须在文档中明确映射关系
- 对 Codex 运行时而言，TOML 不是“补充说明”，而是实际加载的角色定义层
- 若角色需要绑定 skills，应在对应 TOML 中通过 `[[skills.config]]` 明确列出

## Packaging Rules

- 修改 `src/domains/*/agents/` 后，先同步到 `targets/codex/agents/`
- 如果某个 agent 需要在 Codex multi-agent 中直接使用，就必须同时补：
  - `.codex/config.toml` 中的 `[agents.<role>]`
  - `.codex/agents/<role>.toml`
- 如果某个 agent 只是分发归档而非运行时角色，也要在 `targets/codex/README.md` 中写清楚原因
