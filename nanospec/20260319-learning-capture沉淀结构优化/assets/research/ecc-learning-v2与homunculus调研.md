# ECC learning v2 与 Homunculus 调研

## 1. 研究范围

本文件聚焦：

1. `Homunculus` v2 的原始设计与机制。
2. `everything-claude-code` (`ECC`) 中 `continuous-learning-v2` 对这套机制的吸收与改写。
3. 两者对当前仓库 `learning-capture` 的启发与风险。

## 2. Homunculus v2 是什么

根据 `humanplane/homunculus` 官方 README，`Homunculus` v2 的核心口号是：

- instinct-based learning
- reliable observation
- real evolution

它的基本链路是：

1. 用 hooks 捕获 prompt 与 tool use。
2. 后台 observer（Haiku）读取 observation。
3. 抽取成原子 instinct。
4. instinct 聚类后再演化为 command / skill / agent。

### 2.1 关键设计

#### 观察层：hooks-first

`Homunculus` 明确认为 v1 的问题是“skills 来观察，触发概率只有 50%-80%”，因此 v2 改成：

- hooks observe (100%)
- analysis in background agent
- instincts as atomic unit

也就是说，它把“观察可靠性”放到第一优先级，认为学习系统如果不能稳定看到发生了什么，后面一切都是空谈。

#### 知识单元：instinct

`instinct` 不是完整 skill，而是更小的行为原子：

- 一个 trigger
- 一个 action
- 一个 confidence
- 一个 domain
- 一段 evidence

这和“直接从 session 提炼成完整 skill”相比，更像先存行为片段，再决定是否值得聚成更大的资产。

#### 演化路径：默认自动，演化半自动

`Homunculus` README 给出的链路是：

- Observations -> Instincts (auto-approved)
- Instincts cluster around a domain
- User runs `/homunculus:evolve`
- 产出 command / skill / agent

它的哲学是：

- 捕获与原子沉淀尽量自动
- 更大结构的生成保留一个显式 evolve 动作

### 2.2 存储形态

`Homunculus` README 展示的项目内目录是：

- `.claude/homunculus/identity.json`
- `.claude/homunculus/observations.jsonl`
- `.claude/homunculus/instincts/{personal,inherited}/`
- `.claude/homunculus/evolved/{agents,skills,commands}/`

这说明它默认把学习状态放进项目作用域目录，而不是抽象成工具无关的仓库内中间文档。

### 2.3 优势

1. 观察完整，信号损失少。
2. instinct 粒度比完整 skill 更适合持续积累。
3. 演化路径清晰：observation -> instinct -> clustered capability。
4. 有 evidence / confidence / domain 等结构化维度，便于后续筛选。

### 2.4 风险

1. 强依赖 hooks 与 observer runtime。
2. instinct 默认 auto-approved，容易先堆很多半成品。
3. 默认落点与 Claude 插件目录强绑定。
4. 以“最终演化为 skill / command / agent”为默认出口，对“只该沉淀为规则 / 提醒 / 证据”的内容支持不足。

## 3. ECC continuous-learning-v2 做了什么

ECC 本地文档显示，`continuous-learning-v2` 继承了 `Homunculus` 的关键思想，但做了两层重要改造：

1. 从“全局 instincts”扩展为“项目作用域 + 全局作用域”。
2. 把 instinct 管理命令、导入导出、promotion、project registry 做得更完整。

### 3.1 ECC v2 的核心机制

ECC 文档中给出的 v2.1 特征包括：

- `PreToolUse/PostToolUse` hooks 做观察
- observer agent 做后台分析
- instinct 作为原子行为单元
- confidence 0.3-0.9
- domain tagging
- project-scoped instincts + global instincts
- `/evolve` 聚类成 skills / commands / agents
- `/promote` 把跨项目高置信度 instinct 升级为全局

### 3.2 ECC 相比 Homunculus 的主要增强

#### 作用域治理更强

ECC v2.1 新增项目哈希与 `projects.json` 注册表：

- 优先用 `CLAUDE_PROJECT_DIR`
- 再用 git remote URL
- 再用 repo path

然后把 instinct 默认放到：

- `~/.claude/homunculus/projects/<project-hash>/instincts/...`

只有明显跨项目、满足条件时，才提升到全局。

这一步是 ECC 对 Homunculus 最重要的现实改造：

- 它开始正视“跨项目污染”问题。
- 不再假设所有 learned pattern 都该全局生效。

#### 命令面更完整

ECC v2 配了这些命令：

- `/instinct-status`
- `/evolve`
- `/instinct-export`
- `/instinct-import`
- `/promote`
- `/projects`

因此 ECC 不只是“会学”，而是把 learned artifacts 的治理、共享与提升也产品化了。

#### observer 更克制

ECC 文档里的 `observer.enabled` 默认值是 `false`。

这说明它虽然保留了背景观察者架构，但默认并没有强行要求每个人都打开自动后台分析。这比 Homunculus README 里的“fully automatic except evolution”更保守一些。

### 3.3 ECC 相比 Homunculus 的不足 / 成本

1. 系统复杂度仍然很高：hooks、CLI、observer、home 目录存储、project registry、promotion 规则缺一不可。
2. 对当前仓库这类“prompt / skill 资产仓”来说，落点仍然偏运行时系统，而不是仓库内可审查的中间文档。
3. instinct 虽然比 skill 更细，但最终出口仍主要是 `skill / command / agent`，对 `rules`、`doc-update`、`workflow evidence` 这类更轻的资产形态支持弱。

## 4. Homunculus 与 ECC v2 的关系判断

可以把两者理解为：

- `Homunculus` 更像原始的“instinct-based self-evolving plugin”原型。
- `ECC continuous-learning-v2` 更像把这条思路工程化、治理化后的 harness 版本。

二者共享的关键方法论有：

1. 观察要尽量可靠。
2. 学习单元应是原子行为，而不是一上来就完整 skill。
3. 持续学习需要 evidence / confidence / domain / scope。
4. 演化到更大资产应是后一步，不应和观察混成一步。

ECC 额外补的关键能力有：

1. 项目 / 全局作用域隔离。
2. 提升与共享机制。
3. 命令化治理入口。

## 5. 对当前仓库的启发

### 5.1 值得吸收的部分

1. **原子单元思维**
   - `notes` 不该是泛化杂记，而应更接近某种原子行为 / workflow signal / evidence card。
2. **证据 + 置信度 / 强度**
   - 当前 `learning-capture` 只有“证据”，但没有“重复程度 / 确信程度”维度。
3. **作用域意识**
   - 当前仓库至少需要区分：任务内、项目级、跨项目 / 跨分发级。
4. **演化分阶段**
   - observation / signal -> candidate support -> formal asset，不要一步到 skill。

### 5.2 不宜直接吸收的部分

1. **hooks-first 作为主流程前提**
   - 当前仓库仍应保持手工触发和文件驱动为主。
2. **auto-approved instinct 堆积**
   - 容易制造大量噪音。
3. **默认出口只有 skill / command / agent**
   - 当前仓库明确还有 `rules` 这类非常重要的沉淀形态。
4. **强绑定用户目录 runtime**
   - 当前仓库更适合仓库内可审查、可提交、可回顾的中间文档。

## 6. 对 learning-capture 的直接影响

如果要借鉴 ECC / Homunculus，当前仓库更适合吸收的是“中间层方法”，而不是整套运行时：

### 适合吸收

- 把第二层记录从 `notes` 改成更明确的原子候选 / signal / support card
- 增加重复信号、证据强度、作用域、建议演化动作
- 明确从 signal 到 skill / rule / doc / eval 的分流

### 不适合吸收

- 一上来就实现 observation hooks
- 后台 observer 自动写入长期资产
- 默认朝 skill 化单一路径演化

## 7. 初步结论

ECC v2 和 Homunculus 给当前仓库最大的启发，不是“自动产出 skill”，而是：

1. **持续学习的最小单元应该更原子。**
2. **持续学习必须有作用域治理。**
3. **持续学习要把“观察 / 候选 / 正式资产”拆成阶段。**
4. **正式资产不应只有 skill，一定要允许 rule / doc / eval / workflow support 等多种出口。**

这意味着当前 `learning-capture` 的第二层如果继续存在，它更像：

- signal / support / candidate card

而不是：

- notes / learnings / 杂记

## 8. 主要来源

### 本地参考

- `references/translations/everything-claude-code/docs/zh-CN/skills/continuous-learning-v2/SKILL.md`
- `references/translations/everything-claude-code/docs/zh-CN/skills/continuous-learning-v2/agents/observer.md`
- `references/translations/everything-claude-code/docs/zh-CN/commands/learn-eval.md`
- `references/translations/everything-claude-code/docs/zh-CN/skills/continuous-learning/SKILL.md`

### 外部来源

- Homunculus 官方仓库：<https://github.com/humanplane/homunculus>
- ECC 官方站点：<https://ecc.tools/>
