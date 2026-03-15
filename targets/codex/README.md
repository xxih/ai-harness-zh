# Codex 适配层

这里存放 Codex CLI 的分发适配文件，而不是核心 prompt 正文。

## 组成

- `.codex/config.toml`
  - 定义 Codex 项目基线，以及可用的 multi-agent 角色
- `.codex/agents/*.toml`
  - 定义每个 Codex 角色的运行约束与开发者指令
- `.codex/AGENTS.md`
  - 把 Codex 的运行约定和 `src/` 下的核心资产连接起来

## 与 `src/` 的关系

- `src/skills/` 是通用 skill 源资产
- `src/agents/` 是通用 agent prompt 源资产
- `src/commands/` 是通用 command 源资产
- Codex 不直接消费 `src/commands/` 的 slash 命令形态，因此应通过 `.codex/AGENTS.md` 把它们解释成自然语言触发入口

## 分发方式

若要把这一层分发到某个 Codex 项目：

1. 将 `targets/codex/.codex/` 同步到目标项目根目录的 `.codex/`
2. 按需把 `src/skills/` 暴露给 Codex 的 skill 发现机制
3. 保持 `src/` 仍然是源资产真相来源，不要在目标项目中手改复制品
