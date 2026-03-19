<!-- AGENTS: user-feedback-capture -->
- 记录用户明确给出的长期规则、接受 / 拒绝标准和稳定偏好。
- 只记录用户明确表达的内容；不根据语气、情绪或一次性抱怨自行推断。
- 写入位置：
  - 项目级 / 团队级 / 分发级规则 -> `.learned/rules.md`
  - 支持后续 skill / command / eval / doc 的长期候选 -> `.learned/support.md`
  - 只服务当前任务的 learnings -> 当前任务容器已有文件
- 写入内容：至少包含内容本身、证据来源、建议落点、下一步动作。
- 若证据与目标资产已经足够明确，不要只留候选，应继续 codify 到对应正式资产。
<!-- /AGENTS: user-feedback-capture -->
