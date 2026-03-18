# 方案：learning-capture补充AGENTS联动

## 总体策略

本轮不再改具体 skill 正文，而是把需求上收为“领域级 `_AGENTS.md` 约定”。这样可以把默认注入的搭配上下文与 skill / command 本体分层，避免每个 asset 都重复抄一遍协同说明。

具体做法：

1. 先执行 align，把原先“要改 skill 正文”的范围改成“只补全局规则 + 一个领域示例”。
2. 在源资产说明里定义 `_AGENTS.md` 的语义、位置、分隔机制和与 `README.md` / `SKILL.md` 的分工。
3. 在 `asset-governance` 域落一个 `_AGENTS.md` 示例，专门承载 `learning-capture` 的补充上下文。
4. 在 Codex 分发说明里补充 `_AGENTS.md` 与运行时 `AGENTS.md` 的映射口径，但不做自动脚本。
5. 删除当前仓库自有范围内除根目录与 `.nanospec/AGENTS.md` 之外的 `AGENTS.md`，避免污染开发时上下文。
6. `targets/` 若需要承载这类分发内容，改存为 `_AGENTS.md`。

## 实施方式

### 阶段 1：先对齐 NanoSpec 工作面

同步更新：

- `alignment.md`
- `outputs/1-spec.md`
- `outputs/2-plan.md`
- `outputs/3-tasks.md`

确保本轮后续动作不再建立在“改 skill 正文”或“领域通用上下文文件”的旧范围上。

### 阶段 2：补源资产全局规则

更新仓库和 `src/` 说明，明确：

- `src/domains/<domain>/_AGENTS.md` 是领域根目录下的载体文件。
- `README.md` 负责目录导览，`SKILL.md` / `commands/*.md` 负责触发与正文，`_AGENTS.md` 只负责承载默认注入的搭配上下文。
- `_AGENTS.md` 使用 XML 注释标签作为块包裹，例如 `<!-- AGENTS: <name> -->` ... `<!-- /AGENTS: <name> -->`。
- `_AGENTS.md` 的块正文要脱离其他 prompt 也能独立读懂，至少写清用途、记录条件、写入位置、写入内容和默认动作。

### 阶段 3：落一个领域示例

在 `src/domains/asset-governance/_AGENTS.md` 中只写本轮真正需要的内容：

- `learning-capture` 搭配块。

不额外扩写其他 skill 的补充块，避免把示例做成另一个大而全的手册。

### 阶段 4：同步分发说明

更新 `targets/codex/README.md`，必要时补一个运行时 `AGENTS.md`，明确：

- 源资产中的领域 `_AGENTS.md` 是搭配上下文真相来源。
- 当前仓库中不保留 `targets/codex/AGENTS.md`，改为维护 `targets/codex/_AGENTS.md`。
- `targets/` 下这类分发位统一命名为 `_AGENTS.md`。
- 实际如何落成运行时 `AGENTS.md` 暂不在本轮展开，留待后续工具化分发。

### 阶段 5：清理仓库内非根 `AGENTS.md`

删除当前仓库自有范围内多余的 `AGENTS.md`，并把这条约束写回仓库规则，避免后续再把分发副本直接放进仓库。

## 风险与收口

### 风险 1：`_AGENTS.md` 被误写成领域总说明

收口：

- 不写标题壳子、通用规则总述或领域导言。
- 只保留实际需要的块，并用 `AGENTS:` XML 注释标签包裹。

### 风险 1.1：块正文虽然短，但前因后果不清

收口：

- 每个块直接写清“作用 / 记录条件 / 写入位置 / 默认动作”。
- 不用“排队”这类含混词，直接写“记录为候选，不直接改正式文档”。
- 不引用 `nanospec`、`align`、具体 skill 名等额外上下文，除非用户明确要求配合。

### 风险 2：`_AGENTS.md` 和 `SKILL.md` 职责重复

收口：

- `_AGENTS.md` 只写补充规则，不重复触发词、主流程和 references 导航。
- 一旦某段内容只能服务单个 skill 的核心使用方式，应继续留在 `SKILL.md`。

### 风险 3：把分发映射误写成已自动化能力

收口：

- 文档里只声明“需要映射”或“应同步”，不伪装成当前已经自动合并。
- 不新增脚本，不新增隐藏流程。

### 风险 4：示例反过来绑死全仓库

收口：

- 只把 `asset-governance/_AGENTS.md` 作为首个落地示例，且只保留一个 `learning-capture` 块。
- 其他 domain 先遵守同一规则，按需再补实际文件。

### 风险 5：非根 `AGENTS.md` 污染开发上下文

收口：

- 仓库规则明确限定：仅根目录保留 `AGENTS.md`。
- `.nanospec/AGENTS.md` 作为 NanoSpec 保留例外。
- `targets/` 内不再保存该文件；若需要对应分发副本，统一使用 `_AGENTS.md`。
