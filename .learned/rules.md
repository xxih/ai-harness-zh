# Rules

## 2026-03-18 skill 正文边界

### Rule: 通用 skill 要保留分类默认落点，但不能泄露仓库实现结构

- 规则：编写可分发的通用 skill 时，如果这个 skill 天然需要默认记录落点，就应在正文里直接给出，例如 research 类用 `.research/`，quality 类用 `.quality/`，learning 类用 `.learned/`。这些目录是 skill 设计的一部分；当前仓库出现这些目录，是因为真实在使用这些 skill，而不是反过来因为仓库先有这些目录才写进 skill。与此同时，不要把 `src/...`、`targets/...`、`nanospec`、领域分层、分发快照路径等仓库实现细节写成默认前提。
- 证据：用户在“写 skill 的 skill”任务中的连续纠偏；`nanospec/20260318-写skill的skill/alignment.md`
- 落点：`AGENTS.md`
- 下一步：`propose-agents-update`

## 2026-03-19 _AGENTS 载体与命名

### Rule: `_AGENTS.md` 只是搭配上下文载体文件，不是总说明

- 规则：在当前 package-first 结构下，`_AGENTS.md` 只用来存放某些 skill / command 需要默认注入的搭配上下文，不能写成包或领域的通用总说明，也不要加标题壳子、`## 通用规则` 之类的额外层级。块边界统一用 XML 注释标签包裹：`<!-- skill: <name> --> ... <!-- /skill: <name> -->`，command 同理。
- 证据：用户在 `20260318-learning-capture补充AGENTS联动` 任务中的连续纠偏；`nanospec/20260318-learning-capture补充AGENTS联动/alignment.md`
- 落点：`AGENTS.md`、`README.md`、`packages/*/README.md`
- 下一步：`keep-local`

### Rule: 当前仓库仅根目录与 `.nanospec/` 保留 `AGENTS.md` 原名，package target 统一使用 `_AGENTS.md`

- 规则：当前仓库自有资产中，仅允许保留根目录 `AGENTS.md` 与 `.nanospec/AGENTS.md`；其他位置禁止新增或保留 `AGENTS.md`，避免污染开发时上下文。`packages/*/targets/` 下如果需要承载这类分发内容，统一命名为 `_AGENTS.md`，后续若要真正生成运行时 `AGENTS.md`，再交给工具化分发处理。
- 证据：用户在 `20260318-learning-capture补充AGENTS联动` 任务中的明确规则修正；`nanospec/20260318-learning-capture补充AGENTS联动/alignment.md`
- 落点：`AGENTS.md`、`README.md`、`packages/*/targets/*/README.md`
- 下一步：`keep-local`

### Rule: 不要把用户对 agent 的纠正原样写回 prompt

- 规则：编写或更新 prompt、`AGENTS.md`、`_AGENTS.md` 正文时，不要把用户对 agent 的当场纠正原样写回正文；应提炼为稳定、可复用、面向未来执行的规则，只保留“以后应怎样做”，不保留“这次哪里做错了”这类过程性表述。
- 证据：用户在 `20260318-learning-capture补充AGENTS联动` 任务中的明确纠正；`nanospec/20260318-learning-capture补充AGENTS联动/alignment.md`
- 落点：`AGENTS.md`、`packages/*/_AGENTS.md`
- 下一步：`applied-in-docs`

### Rule: 正式文档只写读者需要知道的稳定事实，不泄露任务过程口径

- 规则：编写或更新 `README`、说明文档、prompt 正文时，默认只保留面向读者的当前事实、稳定约定和使用方式，不把“这次为什么这么改”“原来从哪里迁过来”“不是为了避免什么旧分层”这类任务过程中的对比性表述直接写进正文；只有当旧结构、旧路径或迁移关系仍会实际影响读者理解、兼容或迁移时，才保留必要说明。
- 证据：用户在 2026-03-19 以 `domains` 迁移到 `packages` 的 README 示例明确纠正“不要把任务过程里的对比口径泄露给文档读者”。
- 落点：`AGENTS.md`、`README.md`、`packages/*/README.md`
- 下一步：`applied-in-docs`

### Rule: 除明确指定外，prompt 默认保持独立，不互相呼应

- 规则：除 `nanospec` / `spec-driven` 这类本身定义协作面的资产，或用户明确要求配合的场景外，prompt 正文默认保持独立，不主动引用其他 skill、command、任务容器或对齐机制。像 `_AGENTS.md` 这类载体块，应单独写清用途、记录条件、写入位置、写入内容和默认动作。
- 证据：用户在 `20260318-learning-capture补充AGENTS联动` 任务中的明确纠正；`nanospec/20260318-learning-capture补充AGENTS联动/alignment.md`
- 落点：`AGENTS.md`、`README.md`、`packages/*/targets/*/README.md`
- 下一步：`applied-in-docs`

## 2026-03-19 references 与内部资产边界

### Rule: `references/repos/` 只放外部参考仓库，当前仓库自己的资产重组必须留在仓库内部

- 规则：`references/repos/` 只是参考仓库目录，不能承载当前仓库自己的真实资产。若当前仓库里的某个能力要做成更独立的主题单元，应在当前仓库内部重组，例如放进内部资产包，而不是挪到 `references/repos/`。
- 证据：用户在 2026-03-19 明确纠正“repos 只是参考的仓库……我要改的肯定是这个仓库里的资产”。
- 落点：`README.md`、`references/README.md`、`packages/README.md`
- 下一步：`applied-in-docs`

## 2026-03-19 package-first 重组方向

### Rule: 单独可运行 / 可分发的能力优先直接做成 package，分类交给 README

- 规则：当前仓库自有资产默认采用 package-first 组织。只要某个能力已经能单独理解、单独运行或单独分发，就优先直接放进 `packages/<package>/`，没必要再塞进 `domains` 分层；仓库级分类关系交给 `README.md` 与 `packages/README.md` 组织。例外是翻译、参考资料这类不准备分发的内容，应保留在 `references/` 或其他根级显眼入口。
- 证据：用户在“仓库重组为 packages 主组织”任务中的明确要求；`nanospec/20260319-仓库重组为packages主组织/alignment.md`
- 落点：`AGENTS.md`、`README.md`、`packages/README.md`、`references/README.md`
- 下一步：`applied-in-docs`

### Rule: Codex target 镜像默认脚本同步，不手工逐个复制

- 规则：面向 Codex 的 target 分发默认通过仓库脚本自动同步 package source 与 `packages/<package>/targets/codex/` 的镜像内容，避免每次手工复制消耗 token。脚本应只同步 source 资产，不覆盖 target 侧手写的 runtime 文件，例如 `README.md`、`.codex/`。
- 证据：用户在“仓库重组为 packages 主组织”任务中的明确要求；`nanospec/20260319-仓库重组为packages主组织/alignment.md`
- 落点：`AGENTS.md`、`README.md`、`scripts/sync_codex_targets.py`
- 下一步：`applied-in-docs`

## 2026-03-24 README 读者视角

### Rule: 在 README 中写“我们还没补齐的 harness 能力”时，默认指普通开发者而不是仓库维护者

- 规则：当仓库 README 或总览文档需要对比“成熟 harness 已做到什么”和“我们通常还没系统化补齐什么”时，默认把“我们”解释为日常开发者、普通 AI Coding 使用者，尤其是裸用 Claude Code 一类工具的人，而不是当前仓库维护者团队。若读者对象不是普通开发者，应在正文里显式改写，不要让“我们”产生歧义。
- 证据：用户在 `20260324-readme重写AIHarness定位` 任务中的明确纠正：“我刚才说的我们,是日常开发者.普通的 ai Coding 的人.往往是裸用 claude code”；`nanospec/20260324-readme重写AIHarness定位/alignment.md`
- 落点：`README.md`、仓库级说明文档
- 下一步：`applied-in-docs`

## 2026-03-25 staged wave 与 nanospec 对齐

### Rule: 提交一整波 staged 改动前，若还没有对应 nanospec 任务容器，先补齐再 commit

- 规则：当用户要求提交“这一波 staged 改动”时，不要只看当前 `.nanospec/.current` 指针；应先按 staged 文件集合判断这是不是一波独立交付。如果这波改动还没有对应的 nanospec 任务容器，就先补 `brief.md`、`outputs/1-spec.md`、`outputs/2-plan.md`、`outputs/3-tasks.md`，再执行 commit。
- 证据：用户在 2026-03-25 的明确要求：“把暂存区的改动,这一波改动,没有落 nanospec 文档的落一下. 然后 commit”；执行时发现 `.nanospec/.current` 仍指向 `20260324-readme重写AIHarness定位`，而实际 staged wave 对应的是 `20260325-github-workflows与PR生命周期补齐`。
- 落点：`AGENTS.md`、`packages/nanospec/README.md`、相关工作流说明
- 下一步：`keep-local`
