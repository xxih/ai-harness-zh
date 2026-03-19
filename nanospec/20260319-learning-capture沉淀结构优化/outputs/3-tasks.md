## 1. 当前状态

- [x] 1.1 新建任务目录 `nanospec/20260319-learning-capture沉淀结构优化/`。
- [x] 1.2 将 `.nanospec/.current` 切换到 `20260319-learning-capture沉淀结构优化`。
- [x] 1.3 读取当前 `packages/learning-capture/`、`.learned/` 与相关历史 nanospec 任务。
- [x] 1.4 记录用户新增约束：`rules` 往往更有用；`notes` 定位模糊；learning 必须显著增强对 skill 的支撑；可借鉴 Claudeception hooks，但不能默认自动产出 skill。
- [x] 1.5 执行 `/align`：先研究 `ECC learning v2`、`Homunculus` 与行业方法论，再由用户定方向。
- [x] 1.6 用户确认：正式名称改为 `learning-evolution`，并要求直接优化一版闭环实现。

## 2. 已完成研究任务

- [x] 2.1 读取本地 `everything-claude-code` 翻译资产中的 `continuous-learning-v2`、observer、`/learn-eval` 与旧版 continuous-learning 文档。
- [x] 2.2 阅读 `humanplane/homunculus` 官方 README，核对 instinct / evolve / hooks-first 设计。
- [x] 2.3 调研行业持续学习方法论，覆盖 memory-first、instinct/evolution-first、outer-loop/compounding-first 路线。
- [x] 2.4 新增 `assets/research/ecc-learning-v2与homunculus调研.md`。
- [x] 2.5 新增 `assets/research/持续迭代学习-harness方法论调研.md`。

## 3. 本轮实现

- [x] 3.1 将 package 从 `packages/learning-capture/` 重命名为 `packages/learning-evolution/`。
- [x] 3.2 将 skill 从 `learning-capture` 改为 `learning-evolution`，重写闭环工作流与自动化路径说明。
- [x] 3.3 将 `.learned/notes.md` 重构为 `.learned/support.md`，并迁移现有内容。
- [x] 3.4 重写 `references/templates.md`，把长期候选定义为 `support` 卡片，而非普通 notes。
- [x] 3.5 更新包级 `_AGENTS.md`、包 README、根 README、`packages/README.md` 与根 `AGENTS.md`。
- [x] 3.6 运行 `python3 scripts/sync_codex_targets.py learning-evolution`，同步 Codex target 镜像。

## 4. 后续可选增强

- [ ] 4.1 补一个“重复翻译 / 改写流程”的 support 示例，验证闭环是否顺手。
- [ ] 4.2 评估是否在 target 层增加 reminder-first 或 observation-first 自动化入口。
- [ ] 4.3 若未来 target 支持 hooks / observer，再补自动捕获与周期性 stocktake 方案。

## 5. 范围纠正与补充实现

- [x] 5.1 根据用户纠正，撤回误改的 `spec-driven` / `nanospec` 正式资产，把范围收回 `learning-evolution`。
- [x] 5.2 更新当前任务 `alignment.md`、`outputs/1-spec.md`、`outputs/2-plan.md`，记录“只改 learning skill”的边界。
- [x] 5.3 更新 `packages/learning-evolution/skills/learning-evolution/SKILL.md`，把动作改成两阶段：默认先 `Observation / Selection / Representation`，明确指令后才 `Evolution`。
- [x] 5.4 运行 `python3 scripts/sync_codex_targets.py learning-evolution`，同步 Codex target 镜像。
- [x] 5.5 检查 source / target 的 learning-evolution 文案是否一致。
