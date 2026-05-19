# Revision Loop 模式

带反馈的 agent 迭代修订标准模式。用于 checker/validator 发现问题后，让产出方 agent 修订其输出。

---

## 模式：Check-Revise-Escalate（最多 3 次迭代）

该模式适用于以下场景：
1. 某个 agent 产出了结果（plans、imports、gap-closure plans）
2. 某个 checker/validator 对该结果进行评估
3. 发现了需要修订的问题

### 流程

```
prev_issue_count = Infinity
iteration = 0

LOOP:
  1. Run checker/validator on current output
  2. Read checker results
  3. If PASSED or only INFO-level issues:
     -> Accept output, exit loop
  4. If BLOCKER or WARNING issues found:
     a. iteration += 1
     b. If iteration > 3:
        -> Escalate to user (see "After 3 Iterations" below)
     c. Parse issue count from checker output
     d. If issue_count >= prev_issue_count:
        -> Escalate to user: "Revision loop stalled (issue count not decreasing)"
     e. prev_issue_count = issue_count
     f. Re-spawn the producing agent with checker feedback appended
     g. After revision completes, go to LOOP
```

### 问题数量跟踪

跟踪每轮 checker 返回的 `BLOCKER + WARNING` 问题总数。如果连续两轮之间该数字没有下降，就说明 producing agent 卡住了，再继续迭代也不会有帮助。应提前中断并升级给用户。

在每次启动 revision 之前展示迭代进度：
`Revision iteration {N}/3 -- {blocker_count} blockers, {warning_count} warnings`

### Re-spawn Prompt 结构

在重新启动产出方 agent 进行 revision 时，把 checker 的 YAML 格式 issues 传进去。checker 输出中会有一个 `## Issues` 标题，后面跟着一段 YAML block。解析这段 block，并原样传给 revision agent。

```
<checker_issues>
The issues below are in YAML format. Each has: dimension, severity, finding,
affected_field, suggested_fix. Address ALL BLOCKER issues. Address WARNING
issues where feasible.

{YAML issues block from checker output -- passed verbatim}
</checker_issues>

<revision_instructions>
Address ALL BLOCKER and WARNING issues identified above.
- For each BLOCKER: make the required change
- For each WARNING: address or explain why it's acceptable
- Do NOT introduce new issues while fixing existing ones
- Preserve all content not flagged by the checker
This is revision iteration {N} of max 3. Previous iteration had {prev_count}
issues. You must reduce the count or the loop will terminate.
</revision_instructions>
```

### 3 次迭代之后

如果 3 轮修订后问题仍然存在：

1. 向用户展示剩余问题
2. 使用 gate prompt（模式：来自 `references/gate-prompts.md` 的 yes-no）：
   question: `Issues remain after 3 revision attempts. Proceed with current output?`
   header: `Proceed?`
   options:
     - label: `Proceed anyway`   description: `Accept output with remaining issues`
     - label: `Adjust approach`  description: `Discuss a different approach`
3. 如果用户选择 `Proceed anyway`：接受当前输出并继续
4. 如果用户选择 `Adjust approach` 或 `Other`：先与用户讨论，再带着更新后的上下文重新进入产出步骤

### 各 Workflow 的变体

| Workflow | Producer Agent | Checker Agent | 说明 |
|----------|----------------|---------------|------|
| plan-phase | gsd-planner | gsd-plan-checker | revision prompt 见 `planner-revision.md` |
| execute-phase | gsd-executor | gsd-verifier | 执行后的验证 |
| discuss-phase | orchestrator | gsd-plan-checker | 由 orchestrator 内联完成 revision |

---

## 重要说明

- **INFO 级问题始终可接受**，不会触发 revision
- **每次迭代都要重新启动一个新的 agent**，不要试图在同一个上下文里继续
- **必须内联 checker 反馈**，revision agent 需要准确看到失败原因
- **不要静默吞掉问题**，退出 loop 后始终要向用户展示最终状态
