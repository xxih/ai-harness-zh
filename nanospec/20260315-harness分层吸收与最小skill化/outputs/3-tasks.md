## 1. 已完成

验收条件：当前任务目录已建立，且已经形成能指导后续吸收工作的研究结论初稿。

- [x] 1.1 创建 `nanospec/20260315-harness分层吸收与最小skill化/` 任务骨架，并写入 `.nanospec/.current`。
- [x] 1.2 盘点 `references/repos/` 中三个参考仓库与当前仓库已有 skill 现状。
- [x] 1.3 产出 `assets/reference-map.md`，建立按能力层拆分的参考地图。
- [x] 1.4 产出 `outputs/1-spec.md`，明确本次研究的交付边界、成功标志与非目标。
- [x] 1.5 产出 `outputs/2-plan.md`，明确“分类优先、最小 skill 吸收、eval-first 落地”的推进方案。

## 2. 本轮执行

验收条件：研究检索与质量保障两类 coding skill 已在仓库内落地，并通过结构校验。

- [x] 2.1 执行 `/align`，纠正“误做成仓库治理 skill”的偏差，明确目标是 coding skill。
- [x] 2.2 撤回误产出的 `reference-search-first` 与 `asset-review-gate`。
- [x] 2.3 编写 `evals/skills/search-first.md` 与质量闭环对应 eval。
- [x] 2.4 落地 `skills/search-first/` 与 `skills/coding-quality-loop/`，并补充最小 `references/` 文档。
- [x] 2.5 更新 `scripts/validate_assets.py`，覆盖两个新 skill 的最小确定性约束。
- [x] 2.6 更新 `README.md`，按类别组织当前 skills。
- [x] 2.7 运行 `python3 scripts/validate_assets.py` 并确认通过。

## 3. 新的对齐后续

验收条件：后续不再按参考 skill 名称逐个复刻，而是先确定能力压缩方案。

- [x] 3.1 明确质量保障领域采用“两段式”还是“单 skill 三阶段式”压缩方案。
- [x] 3.2 采用单 skill 三阶段式，并重构为 `coding-quality-loop`，避免与未来的 `tdd-workflow`、`requesting-code-review` 形成平铺重复。
- [x] 3.3 在真正新增下一批 coding skill 前，先更新相应 eval，约束压缩后的边界。

## 3. 延后项

验收条件：这些事项保持明确记录，但不进入第一波交付范围。

- [ ] 3.0 暂不吸收 `skill-stocktake` 这类 prompt 资产治理能力，留待下一轮。
- [ ] 3.1 暂不吸收多 agent 编排、hooks 自动学习、MCP 运行时、tmux、Hashline 等重运行时能力。
- [ ] 3.2 暂不复制完整命令体系、rules 体系或平台安装流程。

## 4. 本次文案对齐

验收条件：`coding-quality-loop` 的默认入口改为面向用户任务场景与质量阶段，并有对应回归约束。

- [x] 4.1 执行 `/align`，纠正 `coding-quality-loop` 默认入口混入内部设计理由的问题。
- [x] 4.2 先更新 `evals/skills/coding-quality-loop.md` 与 `scripts/validate_assets.py`，约束入口文案应面向场景与质量动作。
- [x] 4.3 重写 `skills/coding-quality-loop/SKILL.md` 默认入口，去掉“分别记忆多个 skill”之类的内部话术。
