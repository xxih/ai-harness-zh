# Source Asset Layout

`src/` 只负责保存核心源资产，不直接等同于某个运行时的分发目录。

## 领域分层

- 源资产统一放在 `src/domains/<domain>/`
- 每个领域用自己的 `_AGENTS.md` 作为载体文件，存放某些 skill / command 需要默认注入的搭配上下文
- 领域内的目录说明和人工导览继续写在 `README.md`，不要让 `README.md` 和 `_AGENTS.md` 职责混在一起
- 领域内部按资产类型继续拆分，例如 `skills/`、`agents/`、`commands/`
- 后续若某个领域需要 `hooks/`、templates 或其他补充层，也应优先挂在对应领域目录下，而不是回到 `src/` 顶层平铺

## 当前约定

- `_AGENTS.md` 不要求文件标题，也不要求“通用规则”块
- 每个块用 XML 注释标签包裹，例如 `<!-- AGENTS: <name> -->` ... `<!-- /AGENTS: <name> -->`
- 块体只放需要默认注入的补充上下文，不重复正文主流程
- `skills/<name>/SKILL.md` 是 skill 的主入口
- `agents/<name>.md` 是可复用的独立 agent prompt
- `commands/` 留给 slash commands 的入口；没有资产时保留空目录即可
- `targets/` 中的分发层可以为运行时需要做平铺、映射或打包，但源资产真相仍以 `src/domains/` 为准

## 设计原则

- `_AGENTS.md` 更像“领域根目录下的搭配上下文容器”，不是另一份领域总说明
- 某段内容只有在搭配某个 skill / command 时才有意义，就放进 `_AGENTS.md` 对应块，不要回写到每个正文里重复
- `_AGENTS.md` 里的每个块要能脱离其他 skill 或 command 正文独立读懂，至少写清楚：用途、记录条件、写入位置、写入内容、默认动作
- 当前仓库自有资产中，仅根目录 `AGENTS.md` 与 `.nanospec/AGENTS.md` 可以保留原名；`targets/` 若要承载这类分发内容，统一使用 `_AGENTS.md`
- 共享资产仍应默认工具无关；平台差异继续沉淀到 `targets/`
