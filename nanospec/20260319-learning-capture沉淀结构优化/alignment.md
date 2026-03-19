# 对齐记录：learning-capture 沉淀结构优化

## 2026-03-19

- [变更] 用户要求本轮先不要直接推进 `learning-capture` 结构改写，而是先仔细调研 `everything-claude-code` 的 `continuous-learning-v2`、其背后的 `Homunculus`，以及业界更广泛的“持续迭代学习 / 持续积累”的 AI harness 方法论。
- [变更] 本轮交付重心从“直接给出 `notes.md` 替代方案并修改 package”调整为“先完成研究、比较与方向选项，再由用户定方向”。
- [变更] 研究范围至少覆盖三层：
  1. `ECC learning v2` 的工作机制、存储形态、hooks 依赖、演化路径；
  2. `Homunculus` 与 ECC v2 的继承关系、相同点、差异点与风险；
  3. 业界其他持续学习方法论，包括 memory-first、reflection-first、skill/evolution-first、CI/loop-first 等路径。
- [变更] 当前任务在用户定方向前，不修改 `packages/learning-capture/` 正式资产；若研究中形成新的判断，只回写到任务容器与研究材料。

## 影响传播

### 对 `outputs/1-spec.md` 的影响

- 增加“研究先行”的任务目标与完成标志。
- 增加对 ECC / Homunculus / 行业方法论对比的需求。

### 对 `outputs/2-plan.md` 的影响

- 从“直接命名第二层记录并改模板”改为“先形成研究对比，再给方向选项”。
- package 改动后移到用户选方向之后。

### 对 `outputs/3-tasks.md` 的影响

- 新增 ECC / Homunculus / 行业方法论研究任务。
- 原先直接改 `SKILL.md` / 模板 / `_AGENTS.md` 的动作改为暂缓。

## 2026-03-19（继续）

- [变更] 用户进一步确认：正式名称改为 `learning-evolution`，并要求本轮直接先优化一版正式实现。
- [变更] 用户补充：并不排斥未来全自动化；当前只是受限于运行环境没有 Claude Code hooks，因此实现不应被“只能手工”这个事实束缚。
- [变更] 本轮正式方案应保留自动化演进接口，但 source 资产仍以工具无关、文件驱动为主。

## 2026-03-19（范围纠正）

- [偏差] 本轮修改一度误扩散到 `spec-driven`、`nanospec` 等邻近 skill；用户明确要求：当前覆盖范围只限 `learning-evolution`，不要修改无关 skill。
- [变更] `learning-evolution` 的动作需要显式分成两阶段：第一阶段先做 `Observation`、`Selection`、`Representation`；第二阶段才是 `Evolution`。
- [变更] `Evolution` 只有在收到明确指令时才执行；默认不因为进入 learning skill、看到 observation、或存在候选，就自动进入演化与 codify。

## 影响传播（范围纠正后）

### 对 `outputs/1-spec.md` 的影响

- 增加 `learning-evolution` 的两阶段动作约束。
- 增加“当前范围不覆盖 `spec-driven` / `nanospec`”的边界。

### 对 `outputs/2-plan.md` 的影响

- 方案收口为只更新 `packages/learning-evolution/` 及其 target 镜像。
- 不再修改邻近 skill 的正式资产。

### 对 `outputs/3-tasks.md` 的影响

- 新增“撤回越界改动”“更新 learning-evolution 两阶段文案”“同步 target 镜像”的动作。
