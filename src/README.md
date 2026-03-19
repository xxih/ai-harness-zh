# Source Asset Layout

`src/` 只负责保存**跨主题、跨 target 共享的核心源资产**，不直接等同于某个运行时的分发目录。

## 领域分层

- 源资产统一放在 `src/domains/<domain>/`
- 领域内部按资产类型继续拆分，例如 `skills/`、`agents/`、`commands/`
- 只有当某段搭配上下文本身仍然属于共享领域资产时，才放在 `src/domains/<domain>/_AGENTS.md`
- 若某个能力已经有独立主题边界，应优先移到 `packages/`，而不是继续留在 `src/domains/`

## 当前约定

- `skills/<name>/SKILL.md` 是共享 skill 的主入口
- `agents/<name>.md` 是共享独立 agent prompt
- `commands/` 留给轻量任务入口；没有资产时保留空目录即可
- `targets/` 中的共享分发层可以为运行时需要做平铺、映射或打包，但真相仍以 `src/` 为准

## 与 `packages/` 的分工

以下内容继续留在 `src/`：

- 工作流基建类能力
- 仍需要跨多个主题复用的共享资产
- 不适合独立成包的核心抽象

以下内容优先移到 `packages/`：

- 已经能独立理解、独立使用、独立分发的主题包
- 需要自己的 `_AGENTS.md`、专属 target 包或独立 README 的能力集合
- 不再适合放在某个领域里与其他共享资产平铺的主题组
