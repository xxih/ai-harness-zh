# Support

## 2026-03-18 skill 分发与默认落点

### Support: 区分默认记录目录与仓库实现细节

- 类型：`doc`
- 作用域：`cross-project`
- 触发：编写或重写可分发 skill，收敛默认落点与仓库实现细节边界时
- 重复信号：用户在“写 skill 的 skill”任务中连续多次纠偏同一类问题；该问题已影响多个 package 的 skill 正文
- 证据：`nanospec/20260318-写skill的skill/alignment.md` 中 2026-03-18 的三次对齐记录；提交 `92a6ad0` 与后续修正提交 `6eb4429`
- 原料：可直接复用的判断是“保留 `.research/`、`.quality/`、`.learned/` 这类能力默认落点，但移除 `src/...`、`targets/...`、`nanospec`、领域分层与分发副本路径等仓库实现细节”
- 建议落点：`AGENTS.md`
- 建议动作：`update-existing`

## 2026-03-19 内容写作 skills 分层

### Support: 内容写作内核与平台适配层应拆开沉淀

- 类型：`skill`
- 作用域：`project`
- 触发：整理中文内容写作相关 package，判断哪些应做通用写作内核，哪些应做平台适配层时
- 重复信号：同一轮调研覆盖 `article-writing`、`content-engine`、`wechat-article-writer`、`xhs-publisher` 等多个候选后，稳定收敛出同一分层结论
- 证据：`nanospec/20260319-内容写作平台skills调研/assets/research/候选skills调研.md`；`nanospec/20260319-内容写作平台skills调研/outputs/summary.md`
- 原料：可直接复用的分层判断是“`article-writing` 适合长文写作内核，`content-engine` 适合多平台改写内核；公众号、小红书更适合作为平台适配层；发布自动化不要混进通用写作 skill”
- 建议落点：`packages/content-writing/README.md`
- 建议动作：`queue-support`

## 2026-03-24 AI Harness 总览文案

### Support: AI Harness 总览文档应先给能力分类对照，再给仓库定位

- 类型：`doc`
- 作用域：`project`
- 触发：重写仓库根 `README.md` 或其他 AI Harness 总览文档，需要解释成熟 harness 做到什么、当前仓库做到什么、普通开发者通常缺什么时
- 重复信号：用户连续两次纠正同一段 README 结构，先要求“前面就写出各种 harness 做了哪些一般开发者还没做的能力，并分类清晰地写”，后又要求在每类里适当引用具体例子，例如 `superpowers` 的 `brainstorming`、`writing-plans`
- 证据：`nanospec/20260324-readme重写AIHarness定位/alignment.md`；当前对话中的连续纠正
- 原料：可直接复用的结构是“按 `需求澄清与方案化`、`执行编排与隔离`、`质量门禁与验收`、`搜索 / 上下文治理`、`学习沉淀与上下文压缩`、`平台适配 / 规则 / 运行时治理` 分类；每类同时写成熟 harness 例子、当前仓库已有 package、普通开发者通常尚未系统化补齐的部分”
- 建议落点：`README.md`
- 建议动作：`update-existing`
