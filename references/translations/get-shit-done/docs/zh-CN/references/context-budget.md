# Context Budget 规则

保持 orchestrator 上下文精简的标准规则。凡是会启动 subagent 或读取大量内容的 workflow，都应引用本文。

另见：`references/universal-anti-patterns.md`，其中包含完整的通用规则集。

---

## 通用规则

所有会启动 agent 或读取大量内容的 workflow，都必须遵守以下规则：

1. **绝不要**读取 agent 定义文件（`agents/*.md`）`subagent_type` 会自动加载它们
2. **绝不要**把大文件内容内联进 subagent prompt，应让 agent 自己从磁盘读取文件
3. **读取深度要随 context window 缩放**：检查 `.planning/config.json` 中的 `context_window_tokens`
   - 小于 500000 tokens（默认 200k）时：只读取 `frontmatter`、状态字段或摘要。绝不要完整读取 `SUMMARY.md`、`VERIFICATION.md` 或 `RESEARCH.md` 的正文
   - 大于等于 500000 tokens（1M 模型）时：当确实需要内联展示或据此决策时，**可以**读取完整的 subagent 输出正文；仍要避免不必要的读取
4. **委派**重活给 subagent，orchestrator 负责路由，不负责执行
5. **主动预警**：如果你已经消耗了大量上下文（大文件读取、多个 subagent 结果），提醒用户：`Context budget is getting heavy. Consider checkpointing progress.`

## 按 Context Window 控制读取深度

| Context Window | Subagent 输出读取 | SUMMARY.md | VERIFICATION.md | PLAN.md（其他 phase） |
|---------------|------------------|------------|-----------------|----------------------|
| < 500k（200k 模型） | 只读 `frontmatter` | 只读 `frontmatter` | 只读 `frontmatter` | 只读当前 phase |
| >= 500k（1M 模型） | 可读完整正文 | 可读完整正文 | 可读完整正文 | 只读当前 phase |

**如何检查：** 读取 `.planning/config.json` 并查看 `context_window_tokens`。若该字段缺失，按 200k 处理（保守默认值）。

## 上下文退化分层

监控上下文使用量，并据此调整行为：

| 层级 | 使用量 | 行为 |
|------|--------|------|
| PEAK | 0-30% | 完整操作。可读取正文、启动多个 agent、内联结果 |
| GOOD | 30-50% | 正常操作。优先读取 `frontmatter`，积极委派 |
| DEGRADING | 50-70% | 节省使用。只读 `frontmatter`、尽量少内联，并提醒用户预算在变重 |
| POOR | 70%+ | 紧急模式。立即 checkpoint，除非关键，不再新增读取 |

## 上下文退化的预警信号

质量会在触发 panic 阈值前逐步下降。注意以下早期信号：

- **静默式部分完成**：agent 声称任务已完成，但实现并不完整。自检能发现文件存在，却未必能发现语义上是否完整。始终要验证 agent 输出是否满足 plan 的 `must_haves`，而不只是确认文件存在
- **措辞越来越空泛**：agent 开始使用 “appropriate handling” 或 “standard patterns” 之类的表述，而不再给出具体代码。这说明即便尚未出现预算告警，也已经承受上下文压力
- **跳步骤**：agent 省略它平时会执行的协议步骤。如果一个 agent 的成功标准有 8 条，但它只汇报了 5 条，要怀疑存在上下文压力

在委派给 agent 时，orchestrator 无法验证 agent 输出在语义上是否正确，只能验证结构是否完整。这是一个根本限制。可通过 `must_haves.truths` 和抽样验证来缓解。
