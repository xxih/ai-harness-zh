# Rules

## 2026-03-18 skill 正文边界

### Rule: 通用 skill 要保留分类默认落点，但不能泄露仓库实现结构

- 规则：编写可分发的通用 skill 时，如果这个 skill 天然需要默认记录落点，就应在正文里直接给出，例如 research 类用 `.research/`，quality 类用 `.quality/`，learning 类用 `.learned/`。这些目录是 skill 设计的一部分；当前仓库出现这些目录，是因为真实在使用这些 skill，而不是反过来因为仓库先有这些目录才写进 skill。与此同时，不要把 `src/...`、`targets/...`、`nanospec`、领域分层、分发快照路径等仓库实现细节写成默认前提。
- 证据：用户在“写 skill 的 skill”任务中的连续纠偏；`nanospec/20260318-写skill的skill/alignment.md`
- 落点：`AGENTS.md`
- 下一步：`propose-agents-update`
