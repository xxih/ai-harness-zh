# Codex 适配层

这里存放**当前仓库共享源资产**的 Codex 分发目录。

## 组成

- `skills/`
  - 从 `src/domains/*/skills/` 收集并平铺出的共享 Codex skills
- `agents/`
  - 从 `src/domains/*/agents/` 收集并平铺出的共享 Codex agents
- `commands/`
  - 从 `src/domains/*/commands/` 收集并平铺出的共享 Codex commands
- `.codex/config.toml`
  - 定义共享分发包的 Codex 项目基线与角色注册
- `.codex/agents/*.toml`
  - 定义共享角色的运行约束与开发者指令

## 不再包含

以下主题已迁到包内 target：

- `packages/learning-capture/targets/codex/`
- `packages/quality-workflows/targets/codex/`

## 与 `src/` / `packages/` 的关系

- `src/domains/<domain>/...` 是共享源资产的真相来源
- `targets/codex/` 是这些共享资产的平铺快照
- 若某个主题包在 `packages/<package>/` 内已经自带 `targets/codex/`，则回对应包内维护，不再在这里重复保留
