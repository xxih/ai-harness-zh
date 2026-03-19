# 方案：learning-evolution 闭环优化

## 总体判断

在用户最新要求下，这轮任务应先从“直接改结构”切回“研究先行”。当前真正需要先回答的不是命名，而是方法论来源：

1. `ECC learning v2` 与 `Homunculus` 分别把哪一层做强了。
2. 业界更广义的持续学习 harness 还有哪些路线。
3. 当前仓库应吸收哪一层方法，而不应该直接复制哪套系统。
4. 在用户定方向前，不直接修改 `packages/learning-capture/`。

## 当前推荐推进方式

### 第一步：完成研究对比，再收口方向

优先产出两份研究材料：

- `ECC learning v2` 与 `Homunculus` 调研
- 行业持续迭代学习方法论调研

目标不是收集概念，而是明确：

- 哪些机制是 `memory-first`
- 哪些机制是 `instinct / evolution-first`
- 哪些机制是 `outer loop / compounding-first`
- 当前仓库该借哪一层

### 第二步：按用户已选方向直接落一版

用户已确认：

- skill / package 名称改为 `learning-evolution`
- 目标是闭环，不只记录
- 长期方向保留自动化空间，不把当前实现锁死在“只能手工”

因此本轮直接落：

- package / skill 重命名
- `.learned/notes.md` -> `.learned/support.md`
- `support.md` 模板与闭环工作流
- 根文档与包文档同步更新
- `learning-evolution` 的两阶段动作：默认先 `Observation / Selection / Representation`，明确指令后才 `Evolution`

## 范围纠正

用户已明确：本轮只覆盖 `learning-evolution`。因此方案收口为：

- 只改 `packages/learning-evolution/skills/learning-evolution/SKILL.md`
- 只同步 `packages/learning-evolution/targets/codex/skills/learning-evolution/SKILL.md`
- 任务容器只回写当前 learning 任务，不修改 `spec-driven`、`nanospec` 等邻近 skill

## 暂存的结构方向

### 方向 1：先把 `notes` 的语义改掉，而不是先加字段

建议优先评估以下两种命名：

- `skill-support.md`
- `candidates.md`

相比 `notes.md`，这两个名字至少能表达：

- 不是普通笔记
- 它是给后续资产化用的
- 里面应该放证据、碎片、触发语、样例，而不是泛泛感想

如果评估后发现单文件仍然太泛，再退一步考虑更细拆分。

### 方向 2：把 learning 的第二层定义为“资产原料卡”

建议让规则之外的长期记录至少包含以下槽位：

- 类型：`skill` | `command` | `eval` | `doc` | `workflow`
- 触发：什么任务 / 口令 / 场景会用到它
- 重复信号：这类事情为何判断为可能重复
- 证据：本次来自哪里
- 原料：步骤骨架 / 输入输出样例 / 验证线索 / 边界
- 建议动作：`absorb-existing` | `new-skill` | `new-command` | `new-eval` | `keep-local` | `drop`

这样它不会自动变成 skill，但已经具备“以后可以顺着写”的骨架。

### 方向 3：把“重复流程”识别提升为一等公民

这轮要显式支持一种判断：

- 某件事不是单点技巧，而是反复出现的工作流。

例如用户举的“经常翻译一些东西”这类情形，应该能记录成：

- 重复任务类型：翻译 / 改写 / 本地化
- 常见输入：原文、术语约束、目标语气、目标平台
- 常见步骤：读原文、抽术语、定风格、翻译、复核
- 可能产物：新 skill、现有 skill 增补、模板、eval

也就是说，learning 要能感知“这类事已经像一个 skill 雏形了”。

### 方向 4：借鉴 Claudeception，但只吸收轻量部分

建议吸收：

- 对“非平凡、可复用、已验证知识”的高门槛判断
- 对“触发条件”和“验证方式”的强调
- 通过 hooks 或固定时机做提醒的思路

不建议吸收：

- 默认把候选直接写成 skill
- 自动创建后立刻应用
- 把 hooks 变成主流程依赖
- 引入重观察链路或后台 runtime

## 建议实施顺序

### 第一步：撤回越界修改，收回到 learning 范围

- 还原误改的 `spec-driven` / `nanospec` 正式资产
- 当前任务容器记录这次范围纠正

### 第二步：更新 learning-evolution 两阶段文案

- 在 `SKILL.md` 明确第一阶段 `Observation -> Selection -> Representation`
- 把 `Evolution` 改为显式指令触发，而不是默认后续动作
- 自动化路径只强调 observation / reminder，不自动触发 evolution

### 第三步：同步 target 镜像

- 运行 `python3 scripts/sync_codex_targets.py learning-evolution`

### 第四步：继续保留原研究产物

在当前任务容器内继续保留：

- ECC / Homunculus 研究笔记
- 行业方法论研究笔记
- 方向选项与判断依据

### 第五步：补一个“重复工作流”示例

建议补一个更贴近用户场景的示例，例如：

- 翻译 / 改写流程反复出现，逐渐逼近 skill 候选

该示例应展示：

- 哪些进 `rules`
- 哪些进第二层记录
- 第二层记录如何支撑后续 skill 创建

### 第六步：评估是否需要 target 层提醒型 hooks

只有当结构已经稳定后，再决定是否在 target 层加入轻量提醒，例如：

- 会话末提醒是否 capture
- 检测到重复触发语时提醒是否形成候选

提醒只生成候选，不直接写正式资产。

## 暂不建议的做法

- 不建议继续保留“其他记录”这种过宽表述。
- 不建议直接恢复多文件分层，先避免重新变重。
- 不建议把所有高价值经验都强行沉淀成 skill。
- 不建议现在就实现 hooks 自动写入 `.learned/`。

## 本轮产出目标

本轮更适合先产出一套可落地的结构调整方案，覆盖：

1. 第二层记录的名称与定位
2. 模板字段与判断门
3. 对 skill 支撑的最小骨架
4. hooks 的可选增强边界

然后再进入具体 package 改动。
