# Notes

## 2026-03-18 skill 分发与默认落点

### Note: 区分默认记录目录与仓库实现细节

- 内容：在收敛通用 skill 的仓库强绑定表述时，不能把所有路径都一刀切删掉。像 `.research/`、`.quality/`、`.learned/` 这类目录不是“因为当前仓库先约定了才顺手保留”，而是这些 research / quality / learning skill 本来就需要有默认记录落点；当前仓库之所以有这些目录，是因为真实在使用这些 skill。真正该去掉的是 `src/...`、`targets/...`、`nanospec`、领域分层、分发副本路径等实现层细节。
- 证据：`nanospec/20260318-写skill的skill/alignment.md` 中 2026-03-18 的三次对齐记录；提交 `92a6ad0` 与后续修正提交 `6eb4429`
- 下一步：`promote-later`

## 2026-03-19 内容写作 skills 分层

### Note: 内容写作内核与平台适配层应拆开沉淀

- 内容：调研 `article-writing`、`content-engine`、`wechat-article-writer`、`xhs-publisher`、`content-production`、`content-strategy`、`social-content` 后，可以先形成一个稳定分层：`article-writing` 适合做长文写作内核，`content-engine` 适合做多平台改写内核；公众号、小红书这类中文平台能力更适合作为平台适配层，其中 `wechat-article-writer` 偏公众号 workflow，`xhs-publisher` 本质上更偏发布自动化而不是写作内核。后续若沉淀正式 package，应避免把平台发布细节直接混进通用写作 skill。
- 证据：`nanospec/20260319-内容写作平台skills调研/assets/research/候选skills调研.md`；`nanospec/20260319-内容写作平台skills调研/outputs/summary.md`
- 下一步：`promote-later`
