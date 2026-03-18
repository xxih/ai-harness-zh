# Codex 适配层

这里存放 Codex CLI 的分发目录。

## 组成

- `skills/`
  - 从 `src/domains/*/skills/` 收集并平铺出的 Codex skills
- `agents/`
  - 从 `src/domains/*/agents/` 收集并平铺出的 Codex agents
- `commands/`
  - 从 `src/domains/*/commands/` 收集并平铺出的 Codex commands
- `.codex/config.toml`
  - 定义 Codex 项目基线，以及可用的 multi-agent 角色
- `.codex/agents/*.toml`
  - 定义每个 Codex 角色的运行约束与开发者指令

## 与 `src/` 的关系

- `src/domains/<domain>/...` 是源资产
- `targets/codex/skills/`、`targets/codex/agents/`、`targets/codex/commands/` 是面向 Codex 的运行时平铺快照
- Codex 专属差异只放在 `.codex/` 下，不混进通用资产正文

## Codex 角色规则

- `targets/codex/agents/*.md` 表示“要被 Codex 分发出去的 agent 资产”
- 每个需要在 Codex 中直接调用的 agent，都应在 `.codex/config.toml` 的 `[agents.<role>]` 中显式注册
- 每个已注册角色，都应有对应的 `.codex/agents/*.toml`
- 若角色是某个分发 agent 的运行时映射，TOML 中应明确说明它对应哪一个 `agents/*.md`
- 对 Codex 来说，`.codex/agents/*.toml` 才是运行时真正加载的角色定义层；不要只写一个薄摘要
- 若某个角色需要具备特定 skills，应在对应 TOML 中通过 `[[skills.config]]` 显式声明
- 当前已落地的显式映射：
  - `agents/quality-code-reviewer.md` -> `[agents.quality_code_reviewer]` -> `.codex/agents/quality-code-reviewer.toml`
  - 该角色额外挂载 `quality-review`、`quality-review-feedback`、`quality-verify`、`quality-tdd`、`quality-router`

## 分发方式

若要把这一层分发到某个 Codex 项目：

1. 修改 `src/` 后，按需手动同步 `targets/codex/` 中对应的分发副本
2. 确认新增的 `agents/*.md` 是否都已经在 `.codex/config.toml` 中注册为角色
3. 确认新增角色是否都有对应的 `.codex/agents/*.toml`
4. 将整个 `targets/codex/` 作为 Codex 分发目录使用
5. 保持 `src/` 仍然是源资产真相来源，并尽量减少 `targets/codex/` 内的漂移
