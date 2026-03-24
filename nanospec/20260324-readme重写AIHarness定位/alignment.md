# 对齐记录

- [变更] 用户追加要求：README 需要在前部先写清“成熟 harness 已经做了哪些而我们一般还没有系统化的能力”，并按类别清晰组织，同时适当引用具体资产示例，例如 `superpowers` 的 `brainstorming`、`writing-plans`、`subagent-driven-development` 等。
  - 影响范围：`README.md`、`brief.md`、`outputs/1-spec.md`、`outputs/2-plan.md`、`outputs/3-tasks.md`
  - 处理方式：补充一节分类能力对照，明确外部成熟 harness 的代表能力、当前仓库已沉淀的 package，以及仍未系统化覆盖的部分。

- [歧义] 用户补充说明：这里的“我们”不是指当前仓库维护者，而是指日常开发者、普通 AI Coding 使用者，尤其是裸用 Claude Code 这类工具的人。
  - 影响范围：`README.md`、`brief.md`、`outputs/1-spec.md`
  - 处理方式：把 README 中“我们一般还没有做完”的表述改成“普通开发者 / 裸用 Claude Code 的使用者通常还没有系统化做到的部分”，避免读者误解为只在对比当前仓库作者团队。
