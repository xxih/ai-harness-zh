# 方案：harness分层吸收与最小skill化

## 总体策略

本任务采用“按能力层吸收，而不是按仓库吸收”的策略。原因很直接：三个参考仓库虽然都属于 harness，但解决的问题层次不同。若按仓库整体迁移，最终会把流程、运行时、平台假设、命令体系和资产治理全部绑在一起，直接违背当前仓库“小而可复用”的目标。

因此，本次方案把参考能力拆成五层：任务流转层、研究检索层、质量保障层、资产治理层、运行时基础设施层。进一步地，吸收时不按参考 skill 名称逐个落地，而按“能力内核”压缩吸收。只有前四层中的“单一意图、可 eval、可复用”部分进入近期候选，运行时基础设施层整体延后；其中 multiagent 如果只是执行路径，不再单列为延后项。

## 吸收顺序

### 阶段 1：建立分类与筛选标准

先把三个参考仓库的能力映射到统一分类，形成最小 skill 的准入标准。这个阶段的目标不是产出新 skill，而是避免后续每次都从零判断“该不该吸收”。

落地产物：

- `assets/reference-map.md`
- `outputs/1-spec.md`
- `outputs/2-plan.md`

### 阶段 2：确定第一波能力内核

在分类基础上，只选择少量高价值、低耦合、易验证的方向进入第一波。本轮更合理的做法不是逐个复刻 skill，而是先定义能力内核：

1. 研究检索类：以 `search-first`、`iterative-retrieval` 为来源，沉淀“写代码前先搜本地实现、测试和外部方案”的最小 skill，采用名称 `search-first`。
2. 质量保障类：以 `superpowers` 的 `test-driven-development`、`verification-before-completion`、`requesting-code-review`、`receiving-code-review` 为主，拆成 `quality-*` skill 家族，并补一个 `quality-router` 作为手动触发入口。

不建议第一波吸收的方向：

- prompt 资产治理类 `skill-stocktake`
- worktree 前置约束、平台绑定 orchestration runtime
- hooks 自动学习
- 平台插件安装与市场分发
- 多模型路由、MCP 运行时、tmux、Hashline

### 阶段 3：按 eval-first 压缩质量保障能力

研究检索类可以单独成立，因为它的边界很清晰。质量保障类则不应直接拆成多个并列 skill，而应先理解三者的关系：

- `search-first` 负责“先研究再实现”
- `test-driven-development` 负责“实现时的过程约束”
- `verification-loop` 负责“改动后的机械性验证”
- `requesting-code-review` 负责“独立视角的审查判断”
- `verification-before-completion` 负责“完成宣称前必须先有 fresh evidence”

它们属于同一领域，但不在同一时点发挥作用：

1. `test-driven-development`
   - 时点：编码前 / 编码中
   - 作用：防止实现一开始就偏掉
   - 类型：过程约束
2. `verification-loop`
   - 时点：一轮改动完成后
   - 作用：用 build、types、lint、tests、diff review 做确定性收口
   - 类型：机械验证
3. `requesting-code-review`
   - 时点：关键任务后 / 合并前
   - 作用：用第二视角发现方案、边界和代码质量问题
   - 类型：判断性审查
4. `verification-before-completion`
   - 时点：完成宣称前
   - 作用：防止把旧结论、口头说明或主观信心当成完成证据
   - 类型：完成门禁

三者不是同一个动作，但属于同一条质量链路。

### 阶段 4：推荐压缩方式

相比逐个复刻，更推荐两种压缩方案中的一种：

1. 两段式
   - `implementation-loop`
   - 内容：吸收 `tdd-workflow` 的“测试先行” + `verification-loop` 的“改动后验证”
   - 单独保留一个较轻的 `code-review-gate`，吸收 `requesting-code-review`
2. 单 skill 三阶段式
   - `coding-quality-loop`
   - 内部分三段：实现前后约束、验证闭环、独立评审，并附完成宣称门禁
   - 入口保持轻量，只在显式触发时路由到具体阶段

当前采用第二种，因为它更符合“精简吸收、取长补短”的目标。

但采用单 skill 三阶段式，并不意味着要把“为什么没有拆成多个 skill”直接写进默认入口。入口文案应只表达用户可感知的内容：什么场景该使用、默认会经历哪些质量阶段、何时可以判断 ready / not-ready。内部压缩策略只保留在计划、评估和设计说明中。

落地顺序：

1. 先定义“能力内核”，再决定是否拆成 1 个或 2 个 skill
2. 先写 eval，约束能力边界
3. 再创建最小 skill
4. 为复杂模板补 `references/`
5. 更新 `scripts/validate_assets.py`
6. 更新 `README.md`
7. 运行 `python3 scripts/validate_assets.py`

在完成第一波落地之后，还需要补一轮“证据层研究”：把三个参考仓库里真正承载质量约束的 prompt 文件继续拆开，分别看它们属于 skill、command、agent，还是源码中的 hook/template。这样后续再调整 `coding-quality-loop` 时，依据会更具体，不会只停留在抽象口号层面。

## 最小 skill 的定义

后续要吸收的 skill，需要满足以下实现约束：

### 一条核心意图

skill 只解决一个明确问题，或者覆盖一条天然闭环。例如“写代码前先检索现有模式”是一个问题；“测试先行 + 改动验证 + 评审门禁”也可以作为一条完整质量闭环存在。关键不是名字多少，而是边界是否自然。

### 明确输入与产物

skill 必须说明输入是什么、会生成或更新什么产物。如果只能改变会话行为，却没有稳定产物或稳定验收点，就不适合当前仓库优先吸收。

### 依赖可裁剪

如果原始参考能力依赖 hooks、专属工具、平台插件或仓库绑定的 worktree 规则，吸收时需要先裁掉这些依赖，只保留在当前环境中可成立的核心方法。若只是需要独立 reviewer、并行执行或 multiagent 节奏，则可作为可选路径吸收，但不能写死在单一 harness API 上。

### 可定义最小 eval

即使是文档型 skill，也要能定义基础检查，例如文件结构、关键章节、必要边界、触发条件、非目标和产物约束。

## 与现有资产的关系

### `nanospec`

`nanospec` 已承担任务容器、brief/spec/plan/tasks 和 align 机制，因此不需要再吸收一个完整的 brainstorming 或 planning harness。参考仓库中与流程相关的内容，只应作为补充方法，而不是替换当前目录规范。

### `eval-harness`

`eval-harness` 已提供 eval-first 的核心约束。后续从参考仓库吸收的 coding skill，应默认接入这套思路，而不是重新引入另一套评价框架。

## 风险与收口

### 风险 1：分类太粗，最后仍然变成大清单

收口方式：任何候选方向都必须落到“单一意图 + 单个产物 + 最小 eval”三个约束上，不满足就继续停留在参考层。

### 风险 2：过度借鉴工程 harness，脱离当前任务真实目标

收口方式：把“是否直接服务 coding 工作流”作为第一优先级，重运行时能力全部后置。

### 风险 3：第一波扩张太快，重新走向大而全

收口方式：即使本轮落地两个 skill，也只覆盖“研究检索”和“验证闭环”两个动作，不把资产治理、执行编排一起拉进来。

### 风险 4：把内部设计纠偏写成面向用户的规则

收口方式：共享资产的默认入口只写用户任务、质量动作和交付结果；“为什么压缩成一个 skill”“为什么不拆开记忆”这类内部理由留在 plan、alignment 和 eval 中。

### 风险 5：把“质量 prompt”与“运行时质量机制”混为一谈

收口方式：研究时单独标注文件类型与承载位置。像 `everything-claude-code`、`superpowers` 主要把质量能力写成可读 prompt；`oh-my-opencode` 则更多把质量约束写进 hooks、提醒模板和 orchestration 文档。两者价值不同，吸收方式也不同。
