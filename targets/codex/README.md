# Codex Target 包

这里存放当前总仓仍保留的 Codex 分发快照。它只覆盖**仍然留在当前仓库的共享源资产**，不再包含已拆出去的独立能力。

## 当前组成

- `skills/agent-orchestration/`
- `skills/nanospec/`
- `skills/search-first/`
- `skills/spec-driven/`
- `skills/writing-skills/`
- `.codex/config.toml`
- `.codex/agents/*.toml`

## 已拆出

以下内容已移出当前 target 包：

- `learning-capture` -> `references/repos/learning-capture/targets/codex`
- `quality-workflows` -> `references/repos/quality-workflows/targets/codex`

## 与 `src/` 的关系

- `src/domains/<domain>/...` 是当前总仓内共享源资产的真相来源
- `targets/codex/skills/` 是这些共享资产的平铺快照
- Codex 专属运行时差异只放在 `.codex/` 下，不混进通用正文

## 分发方式

1. 修改 `src/` 后，按需手动同步对应的 `targets/codex/` 副本
2. 确认 `.codex/config.toml` 与 `.codex/agents/*.toml` 仍反映当前包内的角色边界
3. 对已经拆到独立 repo 的能力，回对应 repo 的 `targets/codex/` 维护
