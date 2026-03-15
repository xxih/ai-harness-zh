# Codex Adapter Notes

这份文件补充仓库根目录的 `AGENTS.md`，只描述 Codex 适配层的特定约定。

## Source Of Truth

- 核心源资产在 `src/skills/`、`src/agents/`、`src/commands/`
- `targets/codex/.codex/` 只负责 Codex 的运行配置与角色注册
- 需要更新资产正文时，回到 `src/` 修改，而不是在 `.codex/` 内复制维护

## How Codex Should Use This Repo

- 需要通用 workflow 时，优先读取 `src/skills/<name>/SKILL.md`
- 需要独立 reviewer prompt 时，优先对齐 `src/agents/quality-code-reviewer.md`
- 需要轻量任务入口时，把 `src/commands/` 视为“命名意图”，而不是强依赖 slash commands

## Multi-Agent Mapping

- `config.toml` 中的 `[agents.<name>]` 决定 Codex 可调用的角色
- 每个角色的具体行为定义在 `.codex/agents/*.toml`
- 若某个角色需要仓库内的可复用 prompt，应显式引用对应的 `src/agents/` 或 `src/skills/`

## Current Roles

- `explorer`：只读探索，负责梳理源资产和适配层之间的真实关系
- `reviewer`：审查实现与分发适配是否偏离 `src/` 的源资产约定
- `docs_researcher`：验证 Codex 配置、能力边界和分发假设
