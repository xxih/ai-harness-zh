---
name: learning-evolution
description: 在一个会话、任务或阶段性回顾里，先把观察到的信号做 observation / selection / representation，再在明确指令下演化为规则、skill、command、eval 或文档更新；默认结合任务容器与 `.learned/`，既支持手工触发，也允许未来接入 hooks 或 observer。
---

# Learning Evolution

把“这次值得留下什么”做成闭环，但不要一上来就直接进入演化。默认先做第一阶段：`Observation`、`Selection`、`Representation`；只有用户明确给出 `evolution`、演化、收敛正式资产这类指令时，才进入第二阶段。默认落盘位置仍在当前任务容器与仓库根目录 `.learned/`；若目标平台支持 hooks 或 observer，也可以把自动观察接进同一套闭环，但不能跳过判断与证据。

## 何时使用

- 你刚完成一个非平凡任务，想把这次 learnings 真正沉淀为后续可复用资产
- 同一任务里出现了用户纠正、重复 workflow、关键失败与修复、研究结论或稳定 workaround
- 你怀疑这次经验不该只停留在任务内，而应该进入 `rules`、skill、command、eval 或文档
- 你想做阶段性 stocktake，把近期候选统一筛一遍，决定哪些 codify、哪些保留、哪些丢弃
- 目标平台支持 hooks / observer，想让系统自动捕获信号，再由本 skill 做后续演化

不适用：

- 只是一次性 typo、机械改名或偶发问题
- 还没有形成任何可复用结论或证据
- 你只想写一个正式资产，而不需要回顾证据、判断作用域或梳理沉淀路径

## 两阶段动作

### 第一阶段：Observation -> Selection -> Representation

这是默认动作；只要使用本 skill，先做这一阶段：

1. `Observation`
   - 观察本轮出现了哪些用户纠正、重复 workflow、失败修复、研究结论与验证信号。
2. `Selection`
   - 筛选哪些信号值得保留，哪些只是噪音，哪些只该留在 task-local，哪些值得进入长期候选。
3. `Representation`
   - 把筛选后的结果写到任务容器、`.learned/support.md`、`.learned/rules.md` 或其他合适位置。

### 第二阶段：Evolution

`Evolution` 不是默认动作。只有用户明确给出 `evolution`、演化、收敛正式资产、继续 codify 这类指令时，才进入第二阶段。

进入第二阶段后，才把第一阶段留下的结果继续升级为规则、skill、command、eval 或文档更新。没有明确指令时，不自动进入这一步。

## 闭环目标

每次使用本 skill，都要把候选收口到以下结论之一，而不是停在“记了一下”：

1. `drop`
   - 噪音、一次性问题或证据不足，不进入长期沉淀
2. `keep-task-local`
   - 只对当前任务后续步骤有用，留在任务容器，不进入 `.learned/`
3. `queue-support`
   - 值得长期保留，但证据还不足以直接改正式资产；写入 `.learned/support.md`
4. `codify-now`
   - 证据与目标都足够明确，直接更新 `rules`、skill、command、eval 或说明文档

## 默认产物

### 1. 任务内 learnings

- 若内容只服务当前任务或相邻步骤，优先写回当前任务容器已有文件
- 不要把短期局部经验一股脑塞进 `.learned/`
- task-local learnings 的目的，是先提升当前任务后续执行质量

### 2. `.learned/rules.md`

- 只放项目级 / 团队级 / 分发级长期规则
- 典型来源：用户明确纠正、长期口径、稳定接受 / 拒绝标准
- 规则默认先作为候选排队；若证据与目标都足够明确，可直接 codify 到正式资产

### 3. `.learned/support.md`

- 放跨任务、跨会话仍值得保留的支持卡片
- 它不是杂记，而是为正式资产化准备的原料层
- 每条都要能回答：它支持什么资产、为什么值得继续推进、下一步是什么

### 4. 正式资产更新

当证据已足够、目标资产也明确时，不要停在候选层，应继续把经验沉淀到最合适的正式资产：

- 规则 -> `AGENTS.md`、README、某个 skill / eval 说明
- 可复用 workflow -> skill 或 command
- 验证标准 -> eval
- 辅助说明 -> README 或包内文档

## 信号来源

优先从这些地方抓信号：

- 用户纠正
- 重复 workflow
- 错误与修复链路
- 验证失败 / 通过的关键信号
- 研究对比后的稳定判断
- 当前 diff、命令输出、review 结论、任务总结

如果目标平台支持 hooks 或 observer，可以自动采集 prompt、tool use、diff 或 session event；但这些自动 observation 只是信号输入，不等于可直接发布的资产。

## 工作流

1. 确认本次边界
   - 默认先做 `Observation -> Selection -> Representation`
   - 当前任务若已有容器，先读取 `alignment.md`、brief / spec / plan / tasks 与已有 learnings
   - 若用户没有明确给出 `evolution` / 演化类指令，不自动进入第二阶段
2. Observation：收集信号
   - 汇总用户纠正、重复 workflow、失败修复、研究结论与验证结果
   - 若只有模糊印象、没有证据，不进入长期沉淀
3. Selection：判断作用域与去向
   - 作用域：`task-local` | `project` | `cross-project`
   - 去向：长期规则 -> `rules.md`；资产支撑卡 -> `support.md`；局部 learnings -> 任务容器
4. Representation：先把结果落盘
   - 执行 `drop` | `keep-task-local` | `queue-support`
   - 先把筛选结论写回任务容器或 `.learned/*`，不要只停留在对话里
5. 若收到明确 `Evolution` 指令，再评估是否继续 codify
   - 至少回答：是否可复用、是否非平凡、是否有明确触发、是否有证据、是否已有更合适的现有资产
   - 若答案足够明确，再进入 `codify-now`
6. 执行 Evolution
   - `codify-now`
   - 同步更新目标资产与相关说明
7. 如任务口径因此变化，执行 align
   - 若沉淀结果改变了当前任务范围、方案或后续动作，更新 `alignment.md`
   - 若当前任务已有任务清单，也同步回写

## `support.md` 的定位

`support.md` 不是旧 `notes.md` 的改名版杂记，而是“资产支撑卡”集合。每条至少应包含：

- 它想支持的资产类型
- 触发场景
- 重复信号或证据强度
- 可直接复用的原料：步骤骨架、输入输出样例、验证线索、边界
- 下一步动作：继续排队、并入现有资产、直接新建资产或丢弃

如果一条内容回答不了“它在支撑什么”，那就不该进 `support.md`。

## 自动化路径

本 skill 的方法论不依赖某个特定运行时，但允许未来接入更自动的观察层：

- `manual-first`
  - 适用于没有 hooks 的环境；由用户或 agent 显式触发
- `reminder-first`
  - 在 `Stop`、阶段总结或 stocktake 时机触发提醒
- `observation-first`
  - 用 hooks / observer 自动采集信号，再由本 skill 做选择、分流与表示层回写

无论采用哪种路径，都要遵守同一条原则：

- 自动化可以帮助发现和整理信号
- 但不能绕过作用域判断、证据判断与资产去向判断
- 没有明确 `Evolution` 指令时，不因为观察层或候选层存在，就自动进入正式资产演化

## 记录约束

- 不要把所有高价值经验都强行沉淀成 skill；`rule`、`doc`、`eval` 同样是正式出口
- 不要把 task-local learnings 与长期候选混在一起
- 不要把用户对 agent 的当场纠正原样写回 prompt 正文，应提炼为稳定规则或支持卡
- 若已有相同候选，优先更新原条目，不要制造碎片
- 若某条候选已经足以直接 codify，就不要继续停留在 `support.md`

## 模板

需要模板时，读取 [references/templates.md](references/templates.md)。
