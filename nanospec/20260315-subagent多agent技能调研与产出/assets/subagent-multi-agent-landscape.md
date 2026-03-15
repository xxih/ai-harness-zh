# subagent / 多 agent 研究地图

## 研究范围

本轮只聚焦 `references/repos/` 下三个参考仓库中与以下主题直接相关的资产：

- subagent / multi-agent
- delegation / orchestration
- parallel agents / background agents
- review gate / verification gate
- 计划到执行的多角色协作

不把纯运行时代码、平台 UI 集成、插件装配代码当作核心资产候选，只把它们作为“平台适配层约束”的参考证据。

## 当前仓库语境

当前仓库已有：

- `src/skills/search-first/`
- `src/skills/quality-*`
- `src/agents/quality-code-reviewer.md`

当前缺口主要在四类能力：

1. 主控 agent 如何决定何时委派、何时并行、何时顺序推进。
2. 给 subagent 的任务说明应该如何写，才能减少误解和重复劳动。
3. 多 agent 输出如何经过 spec / quality / verification gate 收敛。
4. 哪些能力应保留在核心 prompt 资产层，哪些必须下沉到 `targets/`。

## 仓库一：everything-claude-code

### 强项

- 强调 `Agent-First`，把委派和并行执行写成全局规则，而不是会话技巧。
- 有较成熟的 agent 文件格式、handoff/report 契约，以及外部 orchestrate 命令。
- 明确讨论了 `sub-agent context problem`，并给出 `iterative retrieval` 这类解决模式。
- 在外部 orchestrator 层面，已经形成了 `task.md / handoff.md / status.md / session snapshot` 这类显式控制平面。

### 最值得吸收的模式

- `iterative-retrieval`
  - 主控不要直接信第一次子代理返回。
  - 需要根据结果继续追问、补上下文、再收敛。
- `workflow-type -> agent sequence`
  - 把“先 research、再 plan、再 implement、再 review、再 verify”写成稳定路由。
- `handoff / report contract`
  - 子代理输出应有稳定格式，便于主控判断下一步。
- 外部编排的显式状态文件
  - 适合作为未来 `targets/` 或脚本层的参考，不适合作为核心 skill 本体。

### 不建议直接吸收的部分

- `tmux-worktree-orchestrator.js` 这类真实运行时编排实现。
- 强绑定 Claude/Codex/Gemini wrapper 的 `multi-*` commands。
- `Task(subagent_type=...)`、`/clear`、`~/.claude/agents/` 这类平台专属语义。

## 仓库二：superpowers

### 强项

- 在 prompt 资产层把工作流写得最清楚，尤其是 `subagent-driven-development`。
- 明确区分 implementer、spec reviewer、code quality reviewer。
- 有很强的“控制器负责提取任务全文，不让子代理自己回去读 plan”的意识。
- 对并行派发有清晰前置判断，知道什么时候该并行、什么时候不该并行。

### 最值得吸收的模式

- `fresh subagent per task`
  - 每个任务都用新上下文，减少污染。
- `controller owns context extraction`
  - 由主控提炼完整任务上下文，再交给子代理。
- `spec gate` 和 `quality gate` 分离
  - 先看有没有按要求做，再看代码质量。
- `implementer status protocol`
  - `DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED` 很适合沉淀成通用协议。
- `parallel dispatch independence test`
  - 只有问题域独立、无共享状态时才并行。
- `<SUBAGENT-STOP>`
  - 防止子代理再次触发整套 skill，造成递归污染。

### 不建议直接吸收的部分

- 以 Claude Code 为中心的 `Task / TodoWrite / Skill` 工具语义。
- 平台 bootstrap 文档和 OpenCode 插件实现。
- 大量与真实 CLI、录制日志、权限绕过相关的测试脚本。

## 仓库三：oh-my-opencode

### 强项

- 角色分层最完整：`planner / orchestrator / worker / reviewer / explore`。
- `task` 工具的抽象更细：支持 `category`、`subagent_type`、同步/后台模式、续跑、并发和深度限制。
- 非常强调 orchestrator 不应直接实现，而应负责协调、验证、继续推进。
- 后台 agent、并发控制、tmux 可视化、失败重试、空结果检测等运行时细节做得很完整。

### 最值得吸收的模式

- `planning / execution / workers` 三层分离。
- `category` 是“任务类型 -> 模型/提示规约”的抽象，不只是模型选择。
- `single-task directive`
  - 一次只交给 subagent 一个明确单任务。
- `verification gate`
  - 子代理输出默认不可信，主控必须重新读代码、跑检查、做 gate decision。
- `parallel explore`
  - 先并行探索，再集中执行，再强验证。
- `spawn depth / budget guardrail`
  - 多 agent 必须限制递归深度和总代数。

### 不建议直接吸收的部分

- `BackgroundManager`、`TmuxSessionManager`、session API、轮询与通知实现。
- OpenCode 专属 hooks 与插件装配代码。
- `.sisyphus/` 工作流运行时本身。

## 跨仓库稳定模式

### 1. 角色分层是稳定内核

三仓库都在不同程度上收敛到这几类角色：

- planner
- orchestrator / controller
- implementer / worker
- explore / research
- reviewer / spec-reviewer / quality-reviewer

这说明“角色分层”适合成为核心 prompt 资产，而不是平台专属偶然产物。

### 2. 主控必须掌握上下文，不应把理解责任甩给子代理

稳定共识包括：

- 任务全文应由主控提炼后下发。
- 子代理应拿到清晰边界、预期产物和验证方式。
- 主控要对返回结果继续追问、补检索、做 gate，而不是直接采信。

### 3. 并行不是默认越多越好，而是先做独立性判定

三仓库都没有鼓励“为并行而并行”。更稳定的规则是：

- 只有独立问题域才并行。
- 子代理之间尽量无共享写集。
- 主控在等待子代理时，只能做不重叠工作。
- 需要防止重复检索和重复实现。

### 4. 验证必须和实现解耦

比较稳定的做法是：

- implementer 自审不等于验收通过。
- spec review 和 code quality review 最好拆开。
- 主控必须有 fresh verification evidence。
- review 的输入应尽量结构化，例如 task text、plan、git diff range、文件列表。

### 5. 核心资产与平台适配必须分层

适合进 `src/` 的是：

- 角色约束
- 委派协议
- 并行判定规则
- review / verification gate
- handoff / report 模板

不适合直接进 `src/` 的是：

- tmux pane 管理
- session polling
- hook 注册代码
- 插件注入逻辑
- 平台专属工具映射

## 对当前仓库的候选资产建议

### 候选 `skill`

优先级最高：

- `orchestration-playbook`
  - 复杂任务如何做角色分层、顺序阶段、委派与验证。
- `single-task-delegation`
  - 如何给 subagent 写单任务、低歧义、可验证的 prompt。
- `parallel-delegation`
  - 并行前的独立性判定、反重复规则、结果回收约束。

可并入现有资产或作为第二批：

- `iterative-retrieval`
  - 需要评估是独立 skill，还是并入 `search-first`。
- `verification-gate`
  - 可能与现有 `quality-verify` 对齐，而不是独立重造。

### 候选 `agent`

优先级最高：

- `spec-reviewer`
  - 当前仓库已有 `quality-code-reviewer`，但还缺一个“只看规格符合性”的 reviewer。

第二批可考虑：

- `planner`
- `orchestrator`
- `explore`

这些 agent 很有价值，但要先想清楚和 `targets/codex/.codex/agents/` 的边界，避免重复定义。

### 候选 `command`

优先级较高：

- `parallel-explore`
  - 面向“先并行探索、后集中判断”的工作。
- `start-work` 或 `orchestrate-plan`
  - 从 plan 进入执行态的薄路由命令。

但这类 command 更依赖具体平台能力，建议在 `skill` 明确后再决定是否进入第一波。

### 候选 `eval`

无论最终落哪个资产，都建议先补这些回归约束：

- 委派 prompt 必须是一项明确单任务，而不是模糊大包。
- 并行派发前必须先声明独立性判断。
- 子代理产出不能被直接信任，必须经过 gate。
- 核心资产不得写死 Claude / Codex / OpenCode 的工具名与 API。
- 平台术语与工具映射应放到 `targets/` 或适配文档。

## 建议的首批方向

如果只选一批最小闭环，我建议是：

1. `single-task-delegation` skill
2. `parallel-delegation` skill
3. `spec-reviewer` agent
4. 为以上 2 个 skill + 1 个 agent 先补 eval

理由：

- 这三者最贴近当前主题。
- 与现有 `quality-*`、`search-first` 能形成互补，而不是明显重叠。
- 对运行时依赖最小，更适合先沉淀为核心 prompt 资产。

## 明确延后项

以下内容保留为参考，不进入第一波核心资产：

- tmux / worktree / pane / session 管理
- 背景轮询、通知、失败重试的代码实现
- 平台 bootstrap 与插件注入
- 特定模型/提供商/category 的运行时路由实现
- 大而全的一体化 harness
