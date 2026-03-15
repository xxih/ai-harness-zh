# 方案：subagent多agent技能调研与产出

## 总体判断

三个参考仓库都证明了一件事：`subagent` / `multi-agent` 的核心价值，不在于“开更多 agent”，而在于把以下几件事写成稳定协议：

1. 角色分层
2. 单任务委派
3. 并行前的独立性判定
4. 主控对结果的验证门禁
5. 核心资产与平台运行时的分层

因此，这轮工作不应按仓库逐个“搬运 multi-agent 功能”，而应按能力内核吸收。

## 三仓库分工启发

### everything-claude-code

最强的是“委派规则 + handoff/report 契约 + 外部控制平面”。

它提供的价值主要是：

- 何时该分 agent、何时并行、何时顺序 handoff。
- `iterative-retrieval` 这种解决 subagent context problem 的方法。
- 外部 orchestrate 的状态文件约定。

适合吸收：

- 委派协议
- `iterative-retrieval` 思路
- handoff / report 模板

不适合直接吸收：

- worktree / tmux / wrapper 运行时实现
- 强绑定 Claude/Codex/Gemini 的命令体系

### superpowers

最强的是“任务级 fresh subagent + review gate + 并行判定规则”。

它提供的价值主要是：

- `controller owns context extraction`
- `implementer status protocol`
- `spec review` 与 `quality review` 分离
- `<SUBAGENT-STOP>` 这类递归防护

适合吸收：

- 单任务委派 skill
- 并行委派 skill
- `spec-reviewer` agent

不适合直接吸收：

- 依赖 Claude Code 原生工具语义的 skill 文案
- 平台 bootstrap 与测试脚本

### oh-my-opencode

最强的是“角色分层 + 委派抽象 + orchestrator 纪律 + 并行 runtime 经验”。

它提供的价值主要是：

- `planner / orchestrator / worker / reviewer / explore` 五类角色分层
- `category` 作为任务类型抽象
- `single-task directive`
- `verification gate`
- `parallel explore`

适合吸收：

- 复杂任务编排 skill
- 并行探索 command 思路
- orchestrator / explore / planner 角色约束

不适合直接吸收：

- session API、后台轮询、tmux pane 管理
- hook 级恢复、注入与插件装配代码

## 提炼后的能力内核

### 内核 1：复杂任务编排

定义：主控如何决定何时先计划、何时委派、何时顺序推进、何时做 gate。

建议形态：

- `skill`: `orchestration-playbook`

核心约束：

- planner / orchestrator / worker / reviewer 分层
- orchestrator 默认不直接落地复杂实现
- 中间产物和 handoff 结构化

### 内核 2：单任务委派协议

定义：如何给 subagent 写一个清晰、可验证、低歧义的任务说明。

建议形态：

- `skill`: `single-task-delegation`

核心约束：

- 主控负责提炼任务全文和上下文
- 一次只交给一个明确任务
- 明确产物、验证方式和阻塞升级协议
- 返回状态应包含 `DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED`

### 内核 3：并行委派协议

定义：什么时候适合并行、并行后主控能做什么、如何防止重复劳动和冲突。

建议形态：

- `skill`: `parallel-delegation`
- 可能补一个 `command`: `parallel-explore`

核心约束：

- 并行前先做 independence test
- 并行任务写集尽量不重叠
- 主控等待期间只能做不重叠工作
- 明确 anti-duplication 规则

### 内核 4：规格符合性 gate

定义：把“有没有按要求做”从一般代码质量里拆出来，作为独立角色执行。

建议形态：

- `agent`: `spec-reviewer`

核心约束：

- 不信实现者报告
- 独立读代码对照任务要求
- 输出缺失、额外实现、误解点

## 与现有资产的关系

### `search-first`

需要判断 `iterative-retrieval` 是独立 skill，还是并入 `search-first` 的进阶委派检索模式。当前不建议立即重复新增同质检索 skill。

### `quality-*`

- `quality-verify` 已承担 fresh verification evidence 的一部分职责。
- `quality-code-reviewer` 已承担一般代码质量审查。

因此更缺的是：

- `single-task-delegation`
- `parallel-delegation`
- `spec-reviewer`

也就是说，第一波更适合补 orchestration 和 spec gate，而不是再补一个泛化 code reviewer。

## 首批优先方向

### P0

- 一个聚合型 `agent-orchestration` skill
- 先为这个 skill 补 eval，再落地实现
- skill 内同时覆盖：
  - 角色分层与顺序阶段
  - 单任务委派协议
  - 并行独立性判定与反重复规则
  - 结果回收与验证门禁

### P1

- `iterative-retrieval` 是否并入 `search-first`
- `spec-reviewer` 是否独立成 agent
- `parallel-explore` command
- `planner` / `explore` / `orchestrator` agent 角色

### P2

- `start-work` / `orchestrate-plan` 这类平台命令
- target 层工具映射与运行时适配
- worktree / tmux / background runtime 参考实现

## 落地顺序

1. 确认 P0 资产命名与边界，避免和现有 `search-first`、`quality-*` 重叠。
2. 先写 `evals/`，明确角色分层、委派协议、并行判定、反重复规则和验证门禁的最小回归约束。
3. 再新增 `src/skills/agent-orchestration/` 资产，并按需补 `references/`。
4. 更新 `README.md`、`scripts/validate_assets.py`。
5. 同步 `targets/codex`。
6. 运行 `python3 scripts/validate_assets.py`。

## 风险与收口

### 风险 1：把 prompt 资产做成运行时框架

收口：

- 核心资产只沉淀方法、协议和角色边界。
- session/tmux/hook/runtime 代码保留在参考层或 `targets/`。

### 风险 2：新增资产与现有 skill 重叠

收口：

- 先明确和 `search-first`、`quality-*` 的边界。
- 对重叠项优先并入，而不是无差别新增。

### 风险 3：把平台术语写进通用资产

收口：

- `Task`、`spawn_agent`、`@mention`、`collab=true` 这类术语只放在适配层。

### 风险 4：并行委派规则流于口号

收口：

- eval 必须检查是否先做独立性判断、是否限制主控不做重复劳动、是否要求主控做最终 gate。
