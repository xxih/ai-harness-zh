## 1. 已完成

验收条件：本轮范围已从“改 skill 正文”切换为“补领域级 `_AGENTS.md` 规则”。

- [x] 1.1 读取当前任务容器，确认 `.nanospec/.current` 指向 `20260318-learning-capture补充AGENTS联动`。
- [x] 1.2 执行 `/align`，记录“本轮只补全局规则，不改 skill 正文”的范围变化。
- [x] 1.3 同步更新 `outputs/1-spec.md` 与 `outputs/2-plan.md`，去掉旧的 skill 正文改造范围。

## 2. 本轮执行

验收条件：仓库已具备“`_AGENTS.md` 作为搭配上下文载体文件”的规则和首个示例。

- [x] 2.1 更新仓库说明文档，定义 `src/domains/<domain>/_AGENTS.md` 的语义、位置与分隔机制。
- [x] 2.2 新增 `src/domains/asset-governance/_AGENTS.md`，写入 `learning-capture` 搭配块。
- [x] 2.3 同步 `src/domains/asset-governance/README.md` 的结构说明。
- [x] 2.4 补充 Codex 分发说明，写明 `_AGENTS.md` 与运行时 `AGENTS.md` 的关系。

## 3. 本轮校验

验收条件：文档口径一致，且没有把载体文件误写成领域总说明或自动能力。

- [x] 3.1 检查新增说明是否明确区分 `README.md`、`SKILL.md`、`_AGENTS.md` 的职责。
- [x] 3.2 检查文档中是否把 `_AGENTS.md` 的映射误写成当前已经自动完成。
- [x] 3.3 检查 NanoSpec 任务文件与实际改动口径一致。

## 4. 本轮纠偏

验收条件：`_AGENTS.md` 的语义已从“领域通用上下文”纠正为“搭配上下文载体文件”。

- [x] 4.1 执行 `/align`，记录“不要 `## 通用规则` / 标题壳子”的纠正。
- [x] 4.2 删除 `src/domains/asset-governance/_AGENTS.md` 与 `targets/codex/AGENTS.md` 中的标题与通用块，只保留 `learning-capture` 搭配块。
- [x] 4.3 同步修正 README 与 NanoSpec 产物中的错误语义。

## 5. 后续候选

验收条件：后续若其他 domain 需要补充上下文，有统一扩展方向。

- [x] 5.1 执行 `/align`，记录“除根目录外禁止 `AGENTS.md`，包括 `targets/`”的新规则。
- [x] 5.2 执行二次 `/align`，记录“.nanospec 允许保留、targets 改存 `_AGENTS.md`”的纠正。
- [x] 5.3 删除 `targets/codex/AGENTS.md`，改为维护 `targets/codex/_AGENTS.md`。
- [x] 5.4 执行三次 `/align`，把 `_AGENTS.md` 的分隔方式改成 XML 注释标签包裹。
- [x] 5.5 将现有 source / target `_AGENTS.md` 示例同步改为 XML 注释标签格式。
- [x] 5.6 执行四次 `/align`，把 `_AGENTS.md` 示例改成独立可读的简洁写法，明确作用、记录条件、写入位置和默认动作。
- [x] 5.7 执行五次 `/align`，把 XML 注释头统一改成 `AGENTS: xxx`，并移除示例正文里对 `learning-capture`、`nanospec`、`align` 的依赖。
- [ ] 5.8 视需要为 `workflow`、`quality` 等 domain 分别补实际 `_AGENTS.md`。
- [ ] 5.9 若未来某个分发目标确实需要自动拼装，再单开任务实现工具化分发流程。
