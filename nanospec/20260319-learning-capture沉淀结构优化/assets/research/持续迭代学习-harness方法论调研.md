# 持续迭代学习 AI harness 方法论调研

## 1. 研究目标

本文件回答的问题不是“谁最自动”，而是：

1. 业界在持续学习 / 持续积累上主要有哪些方法论家族。
2. 这些家族分别把重点放在 observation、memory、reflection、skill evolution、还是 outer loop。
3. 对当前仓库 `learning-capture` 这种以 prompt / skill 资产为中心的仓库，哪些路径适合吸收，哪些只适合作为远期参考。

## 2. 方法论家族

### 2.1 反思记忆流：Reflection / Memory-first

代表：

- Reflexion
- LangMem
- Letta
- Mem0

#### 核心思路

- 不更新模型权重。
- 通过反思、memory extraction、memory consolidation 来持续改进后续行为。
- memory 可以是 episodic、semantic、procedural，也可以是 prompt rules、memory blocks、memory store。

#### 代表特征

##### Reflexion

Reflexion 代表的是“语言反馈强化”：

- 从任务反馈中生成 reflection
- 把 reflection 放进 episodic memory buffer
- 下一轮再利用这些 reflection

它强调的是：

- 失败后反思
- 反思文本本身就是学习载体
- 不需要参数更新

##### LangMem

LangMem 把持续学习拆得很清楚：

- hot path：agent 在交互中主动决定记什么
- background：后台自动从会话提取 memory
- prompt optimization：不仅记忆事实，也能更新 prompt 规则

它的优势在于：

- 把“记忆”和“prompt 优化”同时纳入统一框架
- 明确区分 semantic / episodic / procedural memory
- 强调 memory creation / consolidation / retrieval 都是可配置的

##### Letta

Letta 的核心是 stateful agent：

- 同一个 agent 可跨 session 持续存在
- agent 可以 self-edit memory
- 有 sleep-time reflection subagent
- 新版 MemFS 把 memory 组织成 git-backed markdown repository

它比普通 memory layer 更进一步的地方在于：

- memory 不是外接 KV，而是 agent 自己维护的长期上下文仓库
- 通过 memory hierarchy 管理哪些内容固定进上下文，哪些只是树状可查
- 反思、defrag、commit/push 都是 memory lifecycle 的组成部分

##### Mem0

Mem0 更偏“生产级 memory infrastructure”：

- 作为独立 memory engine / managed layer 提供
- 支持 user / agent / session memory
- 支持 graph memory、rerankers、webhooks、integrations

它的目标不是 prompt 资产化，而是：

- 为 agent 提供长期可检索、可扩展、可治理的 memory service

#### 对当前仓库的意义

这一路方法论最值得吸收的是：

1. memory 类型要分清（事实、经历、规则 / 行为）。
2. 交互内主动记忆与后台提取可以分层。
3. “学习”不只等于生成 skill，也可以是更新行为规则与长期上下文。

#### 局限

- 更偏 memory 系统，不天然解决“如何沉淀成 skill / command / doc / eval”。
- 若直接产品化，往往需要额外存储与检索基础设施。

### 2.2 原子行为演化流：Instinct / Skill-library-first

代表：

- Homunculus
- ECC continuous-learning-v2
- Voyager
- A-MEM
- MemInsight

#### 核心思路

- 不把“学到的东西”直接做成大而全的记忆块。
- 先存成更小、更原子的行为单元或结构化 note。
- 再通过聚类、链接、进化，演化成 skill / command / agent / richer memory。

#### 代表特征

##### Homunculus / ECC

这一系更强调：

- observation 要完整
- atom 要小（instinct）
- evolve 要后置

其方法论价值是：

- 学习单元和正式资产分层
- 允许在正式 skill 之前先存很多“还不值得发布”的行为片段

##### Voyager

Voyager 的关键是：

- automatic curriculum
- ever-growing skill library
- iterative prompting with environment feedback / execution errors / self-verification

它告诉我们的不是“如何做 Claude skill”，而是：

- skill library 一旦可执行、可组合，就会产生复利
- 持续学习要和探索、验证、组合一起设计

##### A-MEM

A-MEM 强调：

- memory 不能只是平铺存取
- 需要 agentic organization
- 新记忆应能动态链接旧记忆，并反过来更新旧记忆的表示

它借鉴 Zettelkasten：

- 新 note 进入后，不是简单 append
- 而是要参与整个记忆网络的重组

##### MemInsight

MemInsight 关注点是：

- 当 memory 规模变大后，关键问题变成 semantic structuring 与 retrieval quality
- 通过 autonomous augmentation 强化历史 memory 的表示与召回

#### 对当前仓库的意义

这一路最值得吸收的是：

1. 第二层记录应是“原子候选 / 结构化 note”，不是模糊 notes。
2. 新记录进入后，允许回头更新旧记录，而不是只 append。
3. 正式资产化是后一步，前面需要“候选演化层”。

#### 局限

- 很容易滑向“最后都要变成 skill”。
- 如果没有治理，候选层会膨胀成噪音池。

### 2.3 外循环复利流：CI / Loop / Compounding-first

代表：

- Continuous Claude
- Compound Engineering Plugin

#### 核心思路

- 持续改进不一定从 memory 开始，也可以从工程循环开始。
- 让 agent 在 PR / CI / review / codify 的外循环里不断积累上下文与 learnings。

#### 代表特征

##### Continuous Claude

它的重点不是提炼 skill，而是：

- 用持续 loop 代替 one-shot coding
- 持久化 relevant context 与上轮结果
- 通过 PR、CI、review 形成真实反馈回路

它更像：

- persistence + automated retry + GitHub workflow

##### Compound Engineering

它的哲学是：

- 每一轮工程工作都应让下一轮更容易
- 通过 plan / review / codify 让知识变可复用

这和 `learning-capture` 最接近的地方在于：

- 把 capture learnings 当成工程循环的一部分，而不是额外负担
- 强调 codify reusable knowledge

#### 对当前仓库的意义

这一路最有价值的启发是：

1. learning 不应只在任务末尾发生。
2. 记录应回流到下一轮 plan / review / execute。
3. 持续学习的真正反馈不一定是“我记住了”，更可能是“下一次更容易做对”。

#### 局限

- 更偏执行闭环，不天然解决知识分类与长期资产治理。
- 需要与 CI / review / automation 生态结合，当前仓库吸收时要裁剪。

## 3. 一条更完整的行业共识

把这些方法论并在一起看，当前较成熟的持续学习系统通常至少包含 5 层：

1. **Observation**：如何看到发生了什么。
2. **Selection**：哪些信号值得留下。
3. **Representation**：用什么粒度存下来（memory / instinct / note / rule）。
4. **Evolution**：如何从原子单元进化成更大资产。
5. **Feedback Loop**：下一轮如何真正用上这些沉淀。

不同系统的区别主要在于：

- 把哪一层做得最强
- 哪些层自动化，哪些层保留人工门禁

## 4. 对当前仓库的适配判断

### 4.1 当前仓库最不适合的路线

#### 重 runtime / hooks-first 路线

直接做成 Homunculus / ECC 那种：

- hooks 捕获一切
- observer 自动分析
- instinct 自动入库
- evolve 自动出资产

对于当前仓库过重，原因是：

1. 当前仓库是资产仓，不是 agent runtime 产品。
2. 目标是沉淀可审查 prompt / skill / rule 资产，不是先做一个完整 memory engine。
3. 用户已经明确不希望默认自动优化 skills。

### 4.2 当前仓库最适合的路线

#### 轻量 candidate / support 层 + 人工门禁

更适合的组合是：

- 借 LangMem / Letta 的 memory type 思维
- 借 Homunculus / ECC 的 atom / scope / evolve 思维
- 借 Compound Engineering 的 codify 反馈循环
- 保留 superpowers / 当前仓库一贯的人工最终决策

也就是：

1. 先把记录单元做对。
2. 再把记录如何回流到 skill / rule / doc / eval 说清楚。
3. 最后才考虑提醒型 hooks。

## 5. 对 `learning-capture` 的结构启示

结合这次调研，`learning-capture` 更适合承接三类长期沉淀：

1. **Rule candidates**
   - 未来默认应怎样做
2. **Support / signal cards**
   - 为 skill / command / eval / doc 提供原料
3. **Task-local learnings**
   - 优先留在任务容器，服务当前任务后续动作

最关键的变化是：

- `.learned/` 不应该继续承接模糊 notes。
- `.learned/` 更适合承接跨任务、跨会话仍值得保留的长期候选。
- 普通局部 learnings 应尽量留在任务容器。

## 6. 给用户定方向前可选的三条路

### 方向 A：rule + support 双层长期沉淀

- `.learned/rules.md`
- `.learned/support.md`（或更合适的新名）

适合：

- 当前仓库优先做轻量治理
- 不引入更多文件类型
- 重点增强对 skill 的支撑

### 方向 B：rule 长期沉淀 + task-local learnings + candidate promotion

- `.learned/rules.md`
- 任务容器内 learnings / support
- 只有跨任务证据足够时才 promote 到 `.learned/`

适合：

- 希望显著降低 `.learned/` 噪音
- 更强调 nanospec 容器与学习协作

### 方向 C：rule + atomized signals + 远期提醒 hooks

- 先把长期候选卡结构做成 `signal` / `support` card
- 远期在 target 层加提醒 hooks

适合：

- 想明显吸收 ECC / Homunculus 的方法论
- 但暂不复制其 runtime

## 7. 初步结论

如果用户暂时不想上重自动化，当前最平衡的不是“做一个 memory engine”，而是：

- 先把长期沉淀单元改造成更明确的 candidate / support card
- 让 task-local learnings 与 long-term candidates 分层
- 保留人工门禁决定是否升级为 skill / rule / doc / eval

## 8. 主要来源

- Reflexion：<https://arxiv.org/abs/2303.11366>
- Voyager：<https://arxiv.org/abs/2305.16291>
- A-MEM：<https://arxiv.org/abs/2502.12110>
- MemInsight：<https://arxiv.org/abs/2503.21760>
- Lifelong Learning of LLM-based Agents: A Roadmap：<https://arxiv.org/abs/2501.07278>
- LangMem 文档：<https://langchain-ai.github.io/langmem/>
- Letta Code Memory 文档：<https://docs.letta.com/letta-code/memory>
- Mem0 文档：<https://docs.mem0.ai/overview>
- Continuous Claude：<https://github.com/AnandChowdhary/continuous-claude>
- Compound Engineering Plugin：<https://github.com/EveryInc/compound-engineering-plugin>
