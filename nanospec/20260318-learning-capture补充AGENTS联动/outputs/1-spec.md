# 规格说明：learning-capture补充AGENTS联动

## 1. 背景

当前任务原本准备通过修改 `learning-capture` 正文来补上 `AGENTS.md` 协同说明。但用户进一步收敛需求：skill 文档本身可以不改，只需要在领域层补一条全局规则，让 `src/domains/<domain>/_AGENTS.md` 成为领域根目录下的载体文件，用来放某些 skill / command 需要默认注入的搭配上下文。

这意味着本轮重点不再是改具体 skill 的正文，而是把“领域级 `_AGENTS.md` 如何作为搭配上下文容器”这件事定义清楚，并至少落一个可复用示例。

## 2. 目标

1. 明确 `src/domains/<domain>/_AGENTS.md` 的语义、位置和使用边界。
2. 约定 `_AGENTS.md` 内用于“搭配 skill / command”的统一分隔机制。
3. 在不改 `learning-capture` 等 skill 正文的前提下，给当前仓库补上这条全局规则和首个领域示例。
4. 在分发说明中补充“源资产 `_AGENTS.md` 与运行时 `AGENTS.md` 的关系”，但不引入自动合并脚本。
5. 当前仓库自有资产中，仅保留根目录 `AGENTS.md` 与 `.nanospec/AGENTS.md`。
6. `targets/` 若需要承载这类内容，统一保存为 `_AGENTS.md`。

## 3. 非目标

- 不重写 `learning-capture` 或其他 skill 的正文。
- 不引入 hooks、observer、后台扫描或自动上下文拼装脚本。
- 不要求本轮一次性为所有 domain 写满完整补充内容。
- 不把 `_AGENTS.md` 变成新的 skill 入口；它只是载体文件，不承担触发词职责。

## 4. `_AGENTS.md` 约定

### 4.1 位置

- 文件位置固定为 `src/domains/<domain>/_AGENTS.md`。
- 它位于领域根目录，和 `skills/`、`commands/`、`agents/` 平级。
- `README.md` 继续负责目录导览；`_AGENTS.md` 只是承载搭配注入内容的文件。

### 4.2 内容边界

`_AGENTS.md` 只承载以下内容：

- 某个 skill / command 需要默认注入的补充上下文。
- 不适合直接写回 skill 正文、但确实要伴随该入口一起被加载的说明。

`_AGENTS.md` 不负责：

- 充当领域总说明或领域通用规则索引。
- 代替 `SKILL.md` 的触发说明、主流程或 references 导航。
- 代替 `commands/*.md` 的命令入口定义。
- 承担自动执行逻辑。

### 4.3 分隔机制

本轮统一采用 XML 注释标签包裹：

- `<!-- skill: <name> -->`
- `<!-- /skill: <name> -->`
- `<!-- command: <name> -->`
- `<!-- /command: <name> -->`

标签之间直接写正文，不要求文件标题，也不要求 `## 通用规则` 之类的额外层级。
这样做的目的，是让 agent 或分发层在读取 `_AGENTS.md` 时，直接知道“这段内容要和哪个 skill / command 搭配加载”，同时也便于后续工具化抽取。

## 5. 产物要求

### 5.1 源资产规则

至少需要同步以下说明文件：

- `src/README.md`
- 仓库根 `README.md`
- 受影响 domain 的 `README.md`

这些文档需要明确：

- 为什么 `_AGENTS.md` 放在 domain 根目录。
- 它和 `README.md`、`SKILL.md`、`commands/*.md` 的分工。
- 结构变化后，分发层需要同步相关说明。

### 5.2 领域示例

至少补一个实际 `src/domains/<domain>/_AGENTS.md`，用于证明这套语义能承载至少一个与具体 skill 搭配的补充块。

本轮示例域使用 `asset-governance`，并以 `learning-capture` 为配套示例。

### 5.3 分发说明

需要在 Codex 分发说明中补充：

- 领域 `_AGENTS.md` 是搭配上下文块的源资产真相来源。
- 当前仓库自有资产中，仅保留根目录 `AGENTS.md` 与 `.nanospec/AGENTS.md`。
- `targets/` 若需要承载这类内容，统一保存为 `_AGENTS.md`。
- `targets/` 下这类“AGENTS 分发位”统一按 `_AGENTS.md` 命名，不再各自发明名字。

## 6. 完成标志

满足以下条件即可认为本轮完成：

1. 当前任务的 `alignment.md`、`outputs/1-spec.md`、`outputs/2-plan.md`、`outputs/3-tasks.md` 已同步到新范围。
2. 仓库文档已经把“领域级 `_AGENTS.md` 是搭配上下文载体文件”定义清楚。
3. `src/domains/asset-governance/_AGENTS.md` 已落地，并只保留 `learning-capture` 搭配块。
4. Codex 分发说明已补上 `_AGENTS.md` 与运行时 `AGENTS.md` 的关系说明。
5. 当前仓库内除根目录与 `.nanospec/AGENTS.md` 外，不再保留其他 `AGENTS.md`。
6. `targets/codex/_AGENTS.md` 已作为分发侧副本落地。
