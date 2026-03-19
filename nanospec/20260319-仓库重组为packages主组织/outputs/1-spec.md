# 规格说明：仓库重组为 packages 主组织

## 1. 背景

当前仓库已经同时存在多种顶层组织方式：

- `src/` 承载共享源资产
- `packages/` 承载部分独立主题资产包
- 根级 `targets/` 承载共享分发适配
- 根级 `references/` 承载参考资料与中文翻译

这种并列结构在仓库早期有助于区分“共享源资产”“独立主题包”“分发适配”“参考资料”，但随着更多资产开始独立成组，主组织方式已经出现分裂：

- 新能力到底应先进 `src/` 还是直接建包，判断成本变高
- 根级 `targets/` 与包内 `targets/` 并存，分发边界不够稳定
- `README.md`、`packages/README.md`、`src/README.md`、`targets/README.md` 需要反复解释多套入口
- 现有 `packages/` 已经成为真实组织方向之一，但还没有上升为仓库唯一主路径

用户进一步明确了新的组织原则：

- 能单独运行、单独分发、单独理解的能力，优先就是一个 package
- 没必要再额外塞进 `domains` 目录，用层级做“先分大类再找资产”
- 分类关系交给 README 和包清单来组织，而不是靠 `src/domains/*` 表达
- Codex target 分发需要脚本自动化，不能继续靠手工同步 source / target

本次任务要把这种“多入口并存 + domains 先行”的仓库结构，收敛为“去 `domains` 化、package-first、按 README 组织分类、Codex target 自动分发”的一致布局。

## 2. 任务目标

本次重组完成后，仓库中的自有资产应以 `packages/<package>/` 作为主归属单位；新增能力、已有能力、分发快照、配套参考资料都应优先围绕 package 组织，而不是继续把 `src/`、根级 `targets/`、根级 `references/` 作为长期主承载层。

## 3. 交付范围

### 3.1 仓库主结构收敛

需要把当前仓库的主要交付资产收敛到 `packages/` 体系下，使 `packages/` 成为默认主入口。

成功标志：

- 仓库对“正式资产放哪里”的默认答案变成 `packages/<package>/`
- 根目录不再同时维护 `src/`、根级 `targets/`、根级内部 `references/` 这些并列资产主入口来表达长期结构
- 用户阅读根 `README.md` 时，能够先从 package 清单理解仓库主体，而不是先理解分层历史

验收证据：

- `README.md`
- `packages/README.md`
- 重组后的 `packages/*`

### 3.2 单主题能力 package 化

当前仍直接挂在 `src/`、根级 `targets/` 中的可分发自有资产，需要按可独立理解、可独立分发的主题重组为 package。至少覆盖以下现有能力：

- `nanospec`
- `spec-driven`
- `search-first`
- `agent-orchestration`
- `writing-skills`
- `learning-capture`
- `quality-workflows`
- 现有 Codex 适配基线与角色配置

成功标志：

- 每个能力都能通过某个明确 package 被理解、维护和定位
- package 内可以同时容纳该主题的源资产、说明文档、搭配上下文与目标平台分发内容
- 新增同类资产时，不再需要先判断是否继续向 `src/domains/*` 或根级 `targets/` 追加目录

验收证据：

- 重组后的 `packages/*/README.md`
- 重组后的 `packages/*/skills/`
- 重组后的 `packages/*/agents/`
- 重组后的 `packages/*/targets/`
- 重组后的 `packages/*/references/` 或等价包内资料目录

### 3.3 README 负责分类组织，而不是目录分层

重组后的 package 不能只是“把原目录整体塞进 `packages/`”；每个 package 都需要表达稳定主题边界，仓库层的分类关系交给 README 清单来组织，而不是继续依赖 `domains` 目录。

成功标志：

- 每个 package 名称都能直接表达其主题，而不是沿用历史技术分层名
- package README 能独立说明这个包承载什么、为什么独立成包、内部有哪些资产类型
- 根 `README.md` 与 `packages/README.md` 能把 package 按工作流、治理、质量、翻译、平台适配等维度做清晰分组
- 资产的 source / target / references 等内容在 package 内部关系清楚，不需要依赖仓库历史知识才能理解

验收证据：

- `README.md`
- `packages/README.md`
- `packages/*/README.md`
- 相关 package 内部目录结构

### 3.4 翻译资产保留在 references

外部 prompt 中文翻译资产不属于当前要分发出去的 package，应继续保留在 `references/` 体系下，或其他根级显眼入口；本轮采用 `references/translations/`。

成功标志：

- 翻译资产不再放进 `packages/`
- `references/translations/` 继续作为中文翻译资产入口
- 根 `README.md` 与 `references/README.md` 已明确“翻译资产属于参考资料，不属于分发 package”

验收证据：

- `references/translations/README.md`
- `references/translations/<repo>/...`
- `README.md`
- `references/README.md`

### 3.5 Codex target 分发脚本自动化

Package 内面向 Codex 的分发副本，需要从“手工同步”改成“脚本自动同步”。

成功标志：

- 仓库中存在一个明确的同步脚本，用于把 package source 侧的 `skills/`、`agents/`、`commands/`、`_AGENTS.md` 等内容同步到对应 `packages/<package>/targets/codex/`
- 脚本能清理过期镜像文件，避免 target 与 source 长期漂移
- 维护方式在 README 中被写清楚：优先修改 package source，再运行脚本同步 Codex target

验收证据：

- `scripts/sync_codex_targets.py`
- 受影响的 `packages/*/targets/codex/`
- 受影响的 README / 维护说明

### 3.6 仓库约定与说明文档同步

由于本次属于结构性重组，所有受影响说明文档都需要同步更新，避免“结构已经改了，但约定仍在解释旧世界”。

成功标志：

- 根 `README.md` 已切换为 package-first 叙述
- 受影响的包级 README、参考说明、分发说明与仓库规则文档已同步改写
- 文档中不再把 `src/`、根级 `targets/` 写成未来长期主组织形式
- 文档中已明确：`references/` 是参考资料入口，其中翻译资产属于参考资料例外，不是 package
- 仓库明确保留的根级例外目录，只包括控制/记录目录与外部参考仓库目录，例如 `.nanospec/`、`nanospec/`、`.learned/`、`.quality/`、`.research/`、`references/repos/`、`scripts/`

验收证据：

- `README.md`
- `packages/README.md`
- 受影响的 `packages/*/README.md`
- `AGENTS.md`
- `references/README.md`
- 其他因重组而必须同步的说明文件

## 4. 非目标

- 本轮 spec 不直接展开具体迁移步骤、批次顺序或脚本方案
- 不要求在 spec 阶段拍板每个 package 的最终命名细节
- 不把“未来可能生成 `dist/`”这类发布机制一并纳入本次重组目标
- 不把 Git 元数据或运行时临时文件纳入交付资产讨论

## 5. 约束与注意事项

- 仓库默认使用简体中文；代码、路径、API 名称、协议关键字保持原文
- 共享资产默认保持工具无关，只有目标平台明确绑定时才写入平台细节
- 结构性变更后必须同步更新对应说明文档
- 当前仓库自有资产中，仅允许保留根目录 `AGENTS.md` 与 `.nanospec/AGENTS.md`；若 package 需要承载搭配上下文，继续使用 `_AGENTS.md`
- `references/repos/` 继续只承载外部参考仓库，不承载当前仓库自有资产
- 控制目录与工作记录目录继续保留在仓库根级，不纳入 package 资产层重组
- `references/translations/` 继续承载外部 prompt 中文翻译资产；这类资料默认不当作分发 package
- 若 package-first 目标与现行 `AGENTS.md` 中的目录规则发生冲突，需要先执行 align，并同步修正规则口径

## 6. 完成标志

满足以下条件即可认为本次规格对应的重组目标被满足：

1. `packages/` 已成为仓库自有资产的默认主组织入口。
2. 当前仍分散在 `src/`、根级 `targets/` 的主要可分发资产，都已迁入明确 package，不再依赖 `domains` 目录组织。
3. `references/translations/` 已作为翻译资产入口保留在 references，而不是被纳入 package。
4. 根 `README.md` 与 `packages/README.md` 已承担分类导航职责，package 命名、边界和 README 能独立说明自身主题与内部结构。
5. Codex target 分发已改为脚本自动同步，相关 package 的 `targets/codex/` 已完成回写。
6. 根级与包级说明文档已经同步到 package-first 口径，且保留的根级例外目录已被明确说明。
