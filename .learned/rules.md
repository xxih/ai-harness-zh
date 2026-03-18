# Rules

## 2026-03-18 skill 正文边界

### Rule: 通用 skill 要保留分类默认落点，但不能泄露仓库实现结构

- 规则：编写可分发的通用 skill 时，如果这个 skill 天然需要默认记录落点，就应在正文里直接给出，例如 research 类用 `.research/`，quality 类用 `.quality/`，learning 类用 `.learned/`。这些目录是 skill 设计的一部分；当前仓库出现这些目录，是因为真实在使用这些 skill，而不是反过来因为仓库先有这些目录才写进 skill。与此同时，不要把 `src/...`、`targets/...`、`nanospec`、领域分层、分发快照路径等仓库实现细节写成默认前提。
- 证据：用户在“写 skill 的 skill”任务中的连续纠偏；`nanospec/20260318-写skill的skill/alignment.md`
- 落点：`AGENTS.md`
- 下一步：`propose-agents-update`

## 2026-03-19 _AGENTS 载体与命名

### Rule: 领域 `_AGENTS.md` 只是搭配上下文载体文件，不是领域总说明

- 规则：`src/domains/<domain>/_AGENTS.md` 只用来存放某些 skill / command 需要默认注入的搭配上下文，不能写成领域通用上下文总说明，也不要加标题壳子、`## 通用规则` 之类的额外层级。块边界统一用 XML 注释标签包裹：`<!-- skill: <name> --> ... <!-- /skill: <name> -->`，command 同理。
- 证据：用户在 `20260318-learning-capture补充AGENTS联动` 任务中的连续纠偏；`nanospec/20260318-learning-capture补充AGENTS联动/alignment.md`
- 落点：`AGENTS.md`、`src/README.md`
- 下一步：`keep-local`

### Rule: 当前仓库仅根目录与 `.nanospec/` 保留 `AGENTS.md` 原名，targets 统一使用 `_AGENTS.md`

- 规则：当前仓库自有资产中，仅允许保留根目录 `AGENTS.md` 与 `.nanospec/AGENTS.md`；其他位置禁止新增或保留 `AGENTS.md`，避免污染开发时上下文。`targets/` 下如果需要承载这类分发内容，统一命名为 `_AGENTS.md`，后续若要真正生成运行时 `AGENTS.md`，再交给工具化分发处理。
- 证据：用户在 `20260318-learning-capture补充AGENTS联动` 任务中的明确规则修正；`nanospec/20260318-learning-capture补充AGENTS联动/alignment.md`
- 落点：`AGENTS.md`、`README.md`、`targets/codex/README.md`
- 下一步：`keep-local`
