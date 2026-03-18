# Source Asset Layout

`src/` 只负责保存核心源资产，不直接等同于某个运行时的分发目录。

## 领域分层

- 源资产统一放在 `src/domains/<domain>/`
- 每个领域用自己的 `_AGENTS.md` 承载公共规则、边界和命名口径；只有目录说明和人工导览才写 `README.md`
- 领域内部按资产类型继续拆分，例如 `skills/`、`agents/`、`commands/`
- 后续若某个领域需要 `hooks/`、templates 或其他补充层，也应优先挂在对应领域目录下，而不是回到 `src/` 顶层平铺

## 当前约定

- `skills/<name>/SKILL.md` 是 skill 的主入口
- `agents/<name>.md` 是可复用的独立 agent prompt
- `commands/` 留给更轻量的任务入口；没有资产时保留空目录即可
- `targets/` 中的分发层可以为运行时需要做平铺、映射或打包，但源资产真相仍以 `src/domains/` 为准

## 设计原则

- 先按领域聚合公共规则，再在领域内放具体资产
- 能放进领域 `_AGENTS.md` 的共性约束，就不要在同一领域的每个 skill 里重复解释一遍；结构说明再单独写 `README.md`
- 共享资产仍应默认工具无关；平台差异继续沉淀到 `targets/`
