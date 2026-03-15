# 质量相关 Agent 盘点

## 1. 研究目的

回答一个很具体的问题：

当前仓库为了配合 `quality-*` skill 家族，一度尝试新建 4 个 `src/agents/` 资产。这个数量是否合理，还是应该继续精简？

为了避免主观判断，这份文档只看几个参考对象里“质量相关 agent”到底定义了几个、怎么分工：

- `references/repos/everything-claude-code`
- `references/repos/superpowers`
- `references/repos/oh-my-opencode`
- 当前仓库

## 2. 统计口径

这里区分三种东西，不混在一起算：

1. 根目录或注册表中的独立 agent
   - 明确以 `src/agents/*.md` 或 agent registry 形式存在
2. skill 内部附带的 subagent prompt 模板
   - 例如 reviewer template、spec reviewer prompt
   - 它们会影响“实际用了多少 subagent 角色”，但不算独立 agent 资产数量
3. 写进主 agent / orchestrator prompt 的质量约束
   - 例如 verification loop、completion gate
   - 这是质量机制，不算单独 agent

因此，这里默认先回答：

- “定义了几个独立质量 agent”

然后再补一句：

- “虽然独立 agent 不多，但还有多少质量角色被埋在 skill 模板或 orchestrator 里”

## 3. 结论先行

先给结果：

1. `superpowers` 的独立质量 agent 其实非常少，核心只有 1 个：`code-reviewer`。
2. `everything-claude-code` 的独立质量 agent 最多，核心 4 个，若加语言分支会更高。
3. `oh-my-opencode` 没有一排细碎质量 agent，而是把质量控制集中在少数 reviewer / orchestrator 角色里，核心可视为 2 个：`Momus`、`Atlas`。
4. 当前仓库若保留 4 个质量 agent，粒度已经接近 `everything-claude-code`，明显比 `superpowers` 和 `oh-my-opencode` 更细。
5. 如果目标更接近 `superpowers`，那最合理的落点不是 4 个，也不是 3 个，而是 1 个 reviewer 角色。

推荐保留：

- `quality-code-reviewer`

推荐降级为 skill / reference 内流程：

- `quality-tdd-guide`
- `quality-verifier`
- `quality-review-feedback-handler`

也就是说，独立 agent 只保留 reviewer，其他质量动作留在 skill 内部。

## 4. 分仓库盘点

## 4.1 everything-claude-code

### 4.1.1 核心质量 agent

直接定义在 `agents/` 下、且明显与质量有关的核心 agent 有 4 个：

1. `agents/tdd-guide.md`
2. `agents/code-reviewer.md`
3. `agents/build-error-resolver.md`
4. `agents/security-reviewer.md`

这 4 个分别对应：

- 测试先行
- 代码评审
- 构建 / 类型修复
- 安全审查

### 4.1.2 语言分支

另外还有若干语言特化分支：

- `agents/python-reviewer.md`
- `agents/go-reviewer.md`
- `agents/kotlin-reviewer.md`
- `agents/go-build-resolver.md`
- `agents/kotlin-build-resolver.md`

如果把这些也算进质量相关 agent，总数会到 9 个。

### 4.1.3 这个仓库的特点

- 它把质量能力尽量拆成单独角色
- 适合大型资产库
- 但对我们这种正在沉淀“最小可复用质量资产”的仓库来说，偏细

结论：

- `everything-claude-code` 的质量 agent 数量最多
- 它代表的是“模块化极强”的路线

## 4.2 superpowers

### 4.2.1 独立质量 agent

`superpowers` 根目录 `agents/` 下真正独立的质量 agent，核心只有 1 个：

1. `agents/code-reviewer.md`

### 4.2.2 但它并不只有一个质量角色

虽然独立 agent 只有 1 个，但还有几类质量角色被写进 skill 模板里：

- `skills/requesting-code-review/code-reviewer.md`
- `skills/subagent-driven-development/spec-reviewer-prompt.md`
- `skills/subagent-driven-development/code-quality-reviewer-prompt.md`

也就是说：

- 独立 agent 数量少
- 但 subagent 角色并不少
- 它更倾向把质量角色写成 workflow 内模板，而不是都升格为根目录 agent

### 4.2.3 这个仓库的特点

- 强依赖工作流纪律
- 不靠很多独立 agent 文件取胜
- 真正需要“独立人格”的地方，主要是 reviewer

结论：

- `superpowers` 的独立质量 agent 数量最少
- 它更像“1 个 reviewer agent + 多个 workflow prompt 模板”

## 4.3 oh-my-opencode

### 4.3.1 独立质量相关角色

`oh-my-opencode` 的质量控制并没有拆成一排细小 agent。

如果只看“明显承担质量门禁 / reviewer 职责”的角色，核心可视为 2 个：

1. `Momus`
   - 计划 reviewer
2. `Atlas`
   - 执行期 orchestrator + completion gate + verification enforcer

### 4.3.2 为什么不是更多

因为它的质量逻辑大量写在：

- `Atlas` prompt
- `Momus` review loop
- 其他主 agent 的 verification rules
- hooks / reminders / orchestration

所以它的思路是：

- 少数高杠杆 agent
- 质量机制嵌进主流程
- 不把每个质量阶段都单独做成一个根目录 agent

结论：

- `oh-my-opencode` 的独立质量 agent 也不多
- 但质量控制非常强，因为它依赖 orchestrator 体系而不是 agent 数量

## 4.4 当前仓库

当前仓库最终更适合只保留 1 个独立质量 agent：

1. `src/agents/quality-code-reviewer.md`

它承担的是：

- 独立代码评审
- 关键节点 second opinion
- 与实现者分离的质量把关

而 TDD、验证门禁、评审反馈处理都继续留在 skill 内部。

## 5. 横向比较

| 仓库 | 独立质量 agent 数 | 若计入模板/内嵌角色 | 风格 |
| --- | --- | --- | --- |
| `everything-claude-code` | 4 个核心，最多可到 9 个 | 还会更多 | 模块化、细粒度 |
| `superpowers` | 1 个 | 3 个以上质量 subagent 模板 | 少量独立 agent，更多 workflow 模板 |
| `oh-my-opencode` | 2 个核心角色 | 很多质量机制内嵌在 orchestrator | 少数强角色 + 系统门禁 |
| 当前仓库 | 1 个 | 其余质量动作留在 skill 内 | reviewer 单角色 |

## 6. 对当前仓库的判断

### 6.1 为什么一角色更合适

因为当前仓库并不是在做一个完整 orchestration harness，而是在沉淀可复用 prompt 资产。

在这种目标下：

- 太多 agent 会抬高选择成本
- skill 和 agent 会更容易一一对应，产生平铺重复
- `superpowers` 的真实做法，本来就更偏向“一个 reviewer agent + 多个 workflow 模板”
- reviewer 是最天然适合 subagent 的角色；TDD、verify、review-feedback 都可以在 skill 内完成

## 7. 推荐收敛方案

推荐把当前质量 agents 收敛为 1 个：

### A. 保留

- `quality-code-reviewer`

### B. 降级

- `quality-tdd-guide`
- `quality-verifier`
- `quality-review-feedback-handler`

降级方式：

1. 保留 `src/skills/quality-tdd/`
2. 保留 `src/skills/quality-verify/`
3. 保留 `src/skills/quality-review-feedback/`
4. 删除对应根目录 agent
5. 只在 `quality-review` 里保留独立 reviewer 角色

## 8. 最终建议

最终建议是：

1. 用 agent，但只保留一个 reviewer 角色。
2. 对当前仓库，最合适的是单一 `quality-code-reviewer`。
3. TDD、验证门禁、反馈处理继续作为 skill 内部规则存在。
4. 这最接近 `superpowers` 的做法：独立 reviewer 很重要，但没必要把每个质量阶段都升格成 agent。
