<!-- AGENTS: user-feedback-capture -->
- 记录用户明确给出的长期规则、接受 / 拒绝标准和稳定偏好。
- 只记录用户明确表达的内容；不根据语气、情绪或一次性抱怨自行推断。
- 本块默认独立成立；除用户明确要求协作型工作面外，不主动引用其他 skill、command、任务容器或对齐机制。
- 先判断出口，再决定写入位置：`keep-task-local` | `rules` | `support` | `codify-now`。
- 写入位置：
  - 项目级 / 团队级 / 分发级规则 -> `.learned/rules.md`
  - 支持后续 skill / command / eval / doc 的长期候选 -> `.learned/support.md`
  - 只服务当前工作的 learnings -> 当前上下文已有记录位置
- `support.md` 只承接明确在支持某个正式资产的长期候选；回答不了“它支持什么资产”的内容，不要写进 `support.md`。
- 写入内容：至少包含内容本身、证据来源、建议落点、下一步动作。
- 没有明确演化或 codify 指令时，默认只做 observation / selection / representation，不自动把候选升级为正式资产。
- 若证据与目标资产已经足够明确，不要只留候选，应继续 codify 到对应正式资产。
<!-- /AGENTS: user-feedback-capture -->
