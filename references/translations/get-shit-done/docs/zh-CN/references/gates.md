# Gate 分类

GSD workflows 中使用的标准 gate 类型。每一个验证检查点都应映射到以下四种类型之一。

---

## Gate 类型

### Pre-flight Gate
**目的：** 在操作开始前验证前置条件。  
**行为：** 条件不满足时阻止进入，不产生任何部分结果。  
**恢复方式：** 补齐缺失的前置条件后重试。  
**示例：**
- plan-phase 在规划前检查 `REQUIREMENTS.md`
- execute-phase 在执行前验证 `PLAN.md` 是否存在
- discuss-phase 确认 `ROADMAP.md` 中存在对应 phase

### Revision Gate
**目的：** 评估输出质量；若质量不足则路由到 revision。  
**行为：** 带着明确反馈回到生产者，且受迭代上限约束。  
**恢复方式：** 生产者处理反馈后，由 checker 重新评估。若连续两次迭代之间问题数没有下降，也会提前升级（stall detection）。达到最大迭代次数后，无条件升级。  
**示例：**
- plan-checker 审查 `PLAN.md`（最多 3 次迭代）
- verifier 根据成功标准检查 phase 交付物

### Escalation Gate
**目的：** 把无法自动解决的问题上升给开发者决策。  
**行为：** 暂停 workflow，呈现选项，并等待人工输入。  
**恢复方式：** 开发者选择动作后，workflow 按所选路径恢复。  
**示例：**
- revision loop 在 3 次迭代后耗尽
- worktree 清理时出现 merge conflict
- 需求含糊，需要进一步澄清

### Abort Gate
**目的：** 为防止损害或浪费而终止操作。  
**行为：** 立即停止，保留状态，并报告原因。  
**恢复方式：** 开发者调查根因、修复后，再从 checkpoint 重新开始。  
**示例：**
- 执行期间 context window 严重不足
- `STATE.md` 处于 error 状态，阻塞 `/gsd-next`
- verification 发现关键交付物缺失

---

## Gate 矩阵

| Workflow | Phase | Gate Type | 检查的工件 | 失败行为 |
|----------|-------|-----------|------------|----------|
| plan-phase | Entry | Pre-flight | `REQUIREMENTS.md`、`ROADMAP.md` | 用缺失文件消息阻断 |
| plan-phase | Step 12 | Revision | `PLAN.md` 质量 | 回到 planner（最多 3 次） |
| plan-phase | Post-revision | Escalation | 未解决问题 | 上升给开发者 |
| execute-phase | Entry | Pre-flight | `PLAN.md` | 用缺失 plan 消息阻断 |
| execute-phase | Completion | Revision | `SUMMARY.md` 完整性 | 重新执行未完成任务 |
| verify-work | Entry | Pre-flight | `SUMMARY.md` | 用缺失 summary 消息阻断 |
| verify-work | Evaluation | Escalation | 失败的标准 | 向开发者暴露缺口 |
| next | Entry | Abort | error 状态、checkpoints | 带诊断信息停止 |

---

## 如何实现 Gate

在设计或审计 workflow 的验证点时，使用这套分类：

- **Pre-flight** gate 应放在 workflow 入口。它们是廉价、确定性的检查，可防止无效工作。如果你能通过检查文件是否存在或读取配置来验证某个前提条件，就应使用 pre-flight gate
- **Revision** gate 应放在生产者步骤之后，因为该处输出质量存在波动。必须与迭代上限配对，防止无限循环。上限应反映每次迭代的成本，代价越高，可重试次数越少
- **Escalation** gate 应放在无法自动解决或存在歧义的地方。它是 revision loop 与 abort 之间的安全阀。应给开发者清晰选项，并提供足够上下文以做决定
- **Abort** gate 应放在继续执行会造成损害、浪费大量资源或产出失去意义的位置。它们应保留状态，以便修复根因后继续工作

**选择启发式：** 先从 pre-flight 开始。如果检查发生在产物产生之后，它就是 revision gate。如果 revision loop 无法解决问题，就升级。如果继续执行有危险，就 abort。
