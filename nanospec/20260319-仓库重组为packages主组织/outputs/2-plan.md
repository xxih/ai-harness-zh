# 方案：仓库重组为packages主组织

## 1. 总体策略

本轮按“先对齐结构原则，再整体搬迁，再脚本化分发，最后统一校验”的顺序推进。

新的默认口径是：

- package 是仓库内自有资产的主组织单元
- 能单独理解、单独分发的能力，直接独立成 package
- 分类关系通过根 `README.md` 与 `packages/README.md` 组织
- 根级仅保留仓库控制目录、任务记录目录、自动化脚本目录，以及 `references/repos/` 这类外部参考例外

## 2. 结构重组方案

### 2.1 去 `domains` 化迁移

把当前 `src/domains/*` 中仍属于自有资产的内容，按单主题 package 迁入 `packages/`。本轮采用以下映射：

- `src/domains/workflow/skills/nanospec/` -> `packages/nanospec/`
- `src/domains/workflow/skills/spec-driven/` -> `packages/spec-driven/`
- `src/domains/workflow/skills/search-first/` -> `packages/search-first/`
- `src/domains/workflow/skills/agent-orchestration/` -> `packages/agent-orchestration/`
- `src/domains/asset-governance/skills/writing-skills/` -> `packages/writing-skills/`

迁移后删除 `src/` 作为长期资产层入口，不再保留“共享层先放 `src/domains/*`，再考虑是否升包”的叙述。

### 2.2 根级 references 收口

`references/repos/` 继续作为外部参考仓库例外保留在根级；`references/translations/` 也继续保留在 references，作为翻译资料入口。

本轮至少执行：

- `references/quality-agent-landscape.md` -> `packages/quality-workflows/references/quality-agent-landscape.md`

调整后，`references/README.md` 需要明确两类内容：

- `references/repos/`：外部参考仓库
- `references/translations/`：不分发的中文翻译资料

### 2.3 根级 targets 收口

根级 `targets/` 不再作为仓库长期资产主入口保留。

处理方式：

- 现有单主题 target 包统一回到各自 package 内维护，例如 `packages/<package>/targets/codex/`
- 当前根级 `targets/codex/.codex/` 中仍有价值的 Codex 基线与角色配置，迁入新的 `packages/codex-base/targets/codex/.codex/`
- 迁移完成后删除根级 `targets/`

## 3. Codex target 自动分发方案

新增一个仓库脚本 `scripts/sync_codex_targets.py`，作为所有 package 的统一同步入口。

脚本职责：

- 扫描 `packages/*/`
- 对存在 `targets/codex/` 的 package，将 package source 侧的 `skills/`、`agents/`、`commands/`、`_AGENTS.md` 镜像到对应 target
- 清理 target 中已不存在于 source 的镜像文件
- 保留 target 侧手写 runtime 文件，例如 `README.md`、`.codex/`

这样做的原因是：

- package source 与 Codex target 的“镜像关系”高度重复，适合脚本化
- target 侧仍允许保留少量平台专属手写文件，不必把一切都塞进脚本模板
- 后续更新 skill 正文时，只需修改 package source，再运行脚本同步，降低 token 与人工成本

## 4. 文档同步策略

本轮同步更新以下说明面：

- 根 `README.md`：改成 package-first 仓库地图
- `packages/README.md`：按主题分组展示 package，而不是解释 `src/` / `targets/` 的分层
- 新增或更新各 package README：说明包边界、组成、Codex target 维护方式
- `AGENTS.md`：更新目录约定，明确去 `domains` 化与 package-first
- `references/README.md`：明确 refs 下的外部参考仓库与翻译资料边界

## 5. 执行顺序

1. 先更新 NanoSpec 产物，消除旧 spec 中对 `src/domains` 的依赖口径。
2. 创建新 package 目录并搬迁 source / target 基线文件，同时保留翻译资料在 `references/translations/`。
3. 补齐迁移后各 package 的 README。
4. 实现 `scripts/sync_codex_targets.py`。
5. 运行脚本同步各 package 的 `targets/codex/`。
6. 删除已失效的根级 `src/`、`targets/` 与已迁走的根级内部 references 内容。
7. 统一校对 README、AGENTS、脚本结果与目录结构。

## 6. 风险与收口

### 6.1 README 与历史 NanoSpec 文档漂移

仓库说明文档中有大量对 `src/domains/*`、根级 `targets/codex/`、`references/translations/` 的引用。本轮只同步正式仓库说明文档与当前任务容器，不追溯改写历史 NanoSpec 旧任务内容。

### 6.2 target 侧存在手写文件

部分 package 的 `targets/codex/` 下包含 `.codex/*` 等平台专属手写文件。脚本必须只镜像 source 资产，不覆盖这些 runtime 文件。

### 6.3 控制目录不进入 package

`.nanospec/`、`nanospec/`、`.learned/`、`.quality/`、`.research/`、`scripts/` 继续留在根级。它们不是要分发的主题资产，而是仓库运行与沉淀基础设施。
