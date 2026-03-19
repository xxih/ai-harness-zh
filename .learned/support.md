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
