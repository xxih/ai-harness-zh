# gstack development

## Commands

```bash
bun install          # 安装依赖
bun test             # 跑免费测试（browse + snapshot + skill validation）
bun run test:evals   # 跑付费 evals：LLM judge + E2E（按 diff 选测，单次最多约 $4）
bun run test:evals:all  # 无视 diff，跑全部付费 evals
bun run test:gate    # 只跑 gate-tier 测试（CI 默认，阻塞合并）
bun run test:periodic  # 只跑 periodic-tier 测试（每周 cron / 手动）
bun run test:e2e     # 只跑 E2E（按 diff 选测，单次最多约 $3.85）
bun run test:e2e:all # 无视 diff，跑全部 E2E
bun run eval:select  # 查看当前 diff 下会选中哪些测试
bun run dev <cmd>    # 以 dev 模式运行 CLI，例如 bun run dev goto https://example.com
bun run build        # 生成文档并编译二进制
bun run gen:skill-docs  # 从模板重新生成 SKILL.md 文件
bun run skill:check  # 查看所有 skills 的健康面板
bun run dev:skill    # watch 模式：变更后自动重新生成并校验
bun run eval:list    # 列出 ~/.gstack-dev/evals/ 下所有 eval runs
bun run eval:compare # 比较两次 eval runs（默认自动挑最近两次）
bun run eval:summary # 汇总所有 eval runs 的统计
```

`test:evals` 需要 `ANTHROPIC_API_KEY`。Codex E2E 测试（`test/codex-e2e.test.ts`）使用 `~/.codex/` 下 Codex 自己的认证配置，不需要 `OPENAI_API_KEY` 环境变量。E2E 测试会实时输出进度（按 tool-by-tool，使用 `--output-format stream-json --verbose`）。结果会持久化到 `~/.gstack-dev/evals/`，并自动与上一次运行做对比。

**按 diff 选测：** `test:evals` 和 `test:e2e` 会基于相对 base branch 的 `git diff` 自动挑测试。每个测试在 `test/helpers/touchfiles.ts` 中声明自己的文件依赖。只要改动碰到全局 touchfiles（session-runner、eval-store、touchfiles.ts 本身），就会触发全部测试。要强制跑全量，使用 `EVALS_ALL=1` 或对应的 `:all` 脚本。先看会跑哪些，可用 `eval:select`。

**双层测试体系：** 测试在 `E2E_TIERS`（位于 `test/helpers/touchfiles.ts`）里被分为 `gate` 或 `periodic`。CI 只跑 gate tests（`EVALS_TIER=gate`）；periodic tests 每周通过 cron 或手动触发。可用 `EVALS_TIER=gate` 或 `EVALS_TIER=periodic` 做过滤。新增 E2E tests 时，按下面分类：
1. Safety guardrail 或确定性功能测试？→ `gate`
2. 质量基准、Opus 模型测试、或非确定性测试？→ `periodic`
3. 依赖外部服务（Codex、Gemini）？→ `periodic`

## Testing

```bash
bun test             # 每次 commit 前都跑，免费，<2s
bun run test:evals   # ship 前跑，付费，按 diff 选测（单次最多约 $4）
```

`bun test` 会跑 skill validation、gen-skill-docs 质量检查，以及 browse integration tests。`bun run test:evals` 会通过 `claude -p` 跑 LLM-judge 质量评估和 E2E tests。创建 PR 前两者都必须通过。

## Project structure

```text
gstack/
├── browse/          # 无头浏览器 CLI（Playwright）
│   ├── src/         # CLI + server + commands
│   │   ├── commands.ts  # 命令注册表（单一事实来源）
│   │   └── snapshot.ts  # SNAPSHOT_FLAGS 元数据数组
│   ├── test/        # 集成测试 + fixtures
│   └── dist/        # 编译后的二进制
├── scripts/         # 构建与开发体验工具
│   ├── gen-skill-docs.ts  # 模板 → SKILL.md 生成器
│   ├── resolvers/   # 模板解析模块（preamble、design、review 等）
│   ├── skill-check.ts     # 健康面板
│   └── dev-skill.ts       # watch 模式
├── test/            # Skill validation + eval tests
│   ├── helpers/     # skill-parser.ts, session-runner.ts, llm-judge.ts, eval-store.ts
│   ├── fixtures/    # ground truth JSON、planted-bug fixtures、eval baselines
│   ├── skill-validation.test.ts  # Tier 1：静态校验（免费，<1s）
│   ├── gen-skill-docs.test.ts    # Tier 1：生成器质量（免费，<1s）
│   ├── skill-llm-eval.test.ts    # Tier 3：LLM-as-judge（约 $0.15/次）
│   └── skill-e2e-*.test.ts       # Tier 2：通过 claude -p 的 E2E（约 $3.85/次，按类别拆分）
├── qa-only/         # /qa-only skill（只报告 QA，不修复）
├── plan-design-review/  # /plan-design-review skill（只报告的设计审计）
├── design-review/    # /design-review skill（设计审计 + 修复循环）
├── ship/            # Ship workflow skill
├── review/          # PR review skill
├── plan-ceo-review/ # /plan-ceo-review skill
├── plan-eng-review/ # /plan-eng-review skill
├── autoplan/        # /autoplan skill（自动评审流水线：CEO → design → eng）
├── benchmark/       # /benchmark skill（性能回退检测）
├── canary/          # /canary skill（部署后监控循环）
├── codex/           # /codex skill（通过 OpenAI Codex CLI 获取第二模型意见）
├── land-and-deploy/ # /land-and-deploy skill（合并 → 部署 → canary 验证）
├── office-hours/    # /office-hours skill（YC Office Hours：startup 诊断 + builder brainstorm）
├── investigate/     # /investigate skill（系统化 root-cause debugging）
├── retro/           # 复盘 skill（含 /retro global 跨项目模式）
├── bin/             # CLI 工具（gstack-repo-mode、gstack-slug、gstack-config 等）
├── document-release/ # /document-release skill（ship 后文档更新）
├── cso/             # /cso skill（OWASP Top 10 + STRIDE 安全审计）
├── design-consultation/ # /design-consultation skill（从零建立 design system）
├── design-shotgun/  # /design-shotgun skill（视觉方案探索）
├── connect-chrome/  # /connect-chrome skill（带 side panel 的 headed Chrome）
├── design/          # Design binary CLI（GPT Image API）
│   ├── src/         # CLI + commands（generate、variants、compare、serve 等）
│   ├── test/        # 集成测试
│   └── dist/        # 编译后的二进制
├── extension/       # Chrome extension（side panel + activity feed + CSS inspector）
├── lib/             # 共享库（worktree.ts）
├── docs/designs/    # 设计文档
├── setup-deploy/    # /setup-deploy skill（一次性部署配置）
├── .github/         # CI workflows + Docker image
│   ├── workflows/   # evals.yml（在 Ubicloud 上跑 E2E）、skill-docs.yml、actionlint.yml
│   └── docker/      # Dockerfile.ci（预烘焙工具链 + Playwright/Chromium）
├── setup            # 一次性 setup：构建二进制并创建 skill symlinks
├── SKILL.md         # 从 SKILL.md.tmpl 生成（不要直接改）
├── SKILL.md.tmpl    # 模板：改这个，再跑 gen:skill-docs
├── ETHOS.md         # Builder 哲学（Boil the Lake、Search Before Building）
└── package.json     # browse 的构建脚本
```

## SKILL.md workflow

`SKILL.md` 文件是从 `.tmpl` 模板**生成**出来的。要更新文档：

1. 修改 `.tmpl` 文件（例如 `SKILL.md.tmpl` 或 `browse/SKILL.md.tmpl`）
2. 运行 `bun run gen:skill-docs`（或者直接 `bun run build`，它会自动做）
3. 同时提交 `.tmpl` 文件和生成后的 `.md` 文件

要新增一个 browse command，就去改 `browse/src/commands.ts` 然后重建。
要新增 snapshot flag，就去改 `browse/src/snapshot.ts` 里的 `SNAPSHOT_FLAGS` 然后重建。

**SKILL.md 冲突处理：** 生成出来的 `SKILL.md` 文件发生 merge conflicts 时，**绝不要**直接选某一边。正确做法是：1）先解决 `.tmpl` 模板和 `scripts/gen-skill-docs.ts`（它们才是 source of truth）的冲突；2）运行 `bun run gen:skill-docs` 重新生成全部 `SKILL.md`；3）提交重新生成后的文件。直接接受某一边的生成物，会静默吞掉另一边模板里的变更。

## Platform-agnostic design

skills **绝不能**写死 framework-specific commands、文件模式或目录结构。相反：

1. **先读 `CLAUDE.md`**，拿项目自己的配置（测试命令、eval 命令等）
2. **如果没有，就 AskUserQuestion**，让用户告诉你，或让 gstack 去搜 repo
3. **把答案写回 `CLAUDE.md`**，以后就不需要再问第二次

这适用于测试命令、eval 命令、部署命令，以及其他所有 project-specific behavior。配置的所有权属于项目，gstack 只负责读取。

## Writing SKILL templates

`SKILL.md.tmpl` 文件是**给 Claude 读的 prompt templates**，不是 bash 脚本。每个 bash 代码块都在独立 shell 中运行，变量不会跨代码块持久化。

规则：
- **逻辑和状态用自然语言表达。** 不要靠 shell 变量在代码块之间传递状态。直接告诉 Claude 该记住什么，并在 prose 里引用它，例如 “the base branch detected in Step 0”。
- **不要写死分支名。** 通过 `gh pr view` 或 `gh repo view` 动态识别 `main` / `master` 等。面向 PR 的 skills 用 `{{BASE_BRANCH_DETECT}}`。在 prose 中说 “the base branch”，在代码块占位符里写 `<base>`。
- **保持 bash blocks 自洽。** 每个代码块都应该能独立工作。如果它依赖前一步上下文，就在上面的 prose 里把上下文重新说清楚。
- **条件判断写成英文步骤。** 不要在 bash 里写层层嵌套的 `if/elif/else`，直接写成编号流程：“1. 如果 X，做 Y。2. 否则，做 Z。”

## Browser interaction

只要需要和浏览器交互（QA、dogfooding、cookie setup），统一使用 `/browse` skill，或者直接用 `$B <command>` 跑 browse binary。**绝不要**使用 `mcp__claude-in-chrome__*` 工具，它们又慢又不稳定，也不是这个项目使用的路径。

## Vendored symlink awareness

开发 gstack 时，`.claude/skills/gstack` 可能是一个指回当前工作目录的 symlink（被 gitignore）。这意味着 skill 改动会**立即生效**。这对快速迭代很好，但在大改时也有风险，因为你写到一半的 skills 可能会直接影响到其他同时在使用 gstack 的 Claude Code sessions。

**每个 session 至少检查一次：** 跑 `ls -la .claude/skills/gstack`，看它是 symlink 还是实拷贝。如果它是指向你当前工作目录的 symlink，需要知道：
- 模板改动 + `bun run gen:skill-docs` 会立刻影响所有 gstack 调用
- 对 `SKILL.md.tmpl` 的破坏性修改可能会让并发 gstack sessions 一起坏掉
- 做大重构时，应移除 symlink（`rm .claude/skills/gstack`），让系统退回全局安装 `~/.claude/skills/gstack/`

**Prefix setting：** skill symlinks 可以是短名（`qa -> gstack/qa`），也可以是 namespaced（`gstack-qa -> gstack/qa`），由 `~/.gstack/config.yaml` 里的 `skill_prefix` 控制。把 gstack vendoring 到项目里时，symlink 完要再跑一次 `./setup`，它会按你偏好的命名方式创建逐 skill 的 symlinks。传 `--no-prefix` 或 `--prefix` 可以跳过交互式提示。

**For plan reviews：** 如果你在 review 的 plan 会改动 skill templates 或 gen-skill-docs pipeline，要考虑这些改动是否应该先在隔离环境里验证，再让它们 live，尤其是在用户其他窗口里也正在使用 gstack 时。

## Compiled binaries — 绝不要提交 browse/dist/ 或 design/dist/

`browse/dist/` 和 `design/dist/` 目录里是编译后的 Bun binaries（`browse`、`find-browse`、`design`，每个约 58MB）。这些文件只适用于 Mach-O arm64，不适用于 Linux、Windows 或 Intel Mac。`./setup` 脚本本来就会在每个平台从源码构建，所以把二进制提交进 repo 本身就是多余的。它们之所以还在 git 里，是历史遗留错误，以后应该通过 `git rm --cached` 移除。

**绝不要 stage 或 commit 这些文件。** 由于它们被 git 跟踪，即使 `.gitignore` 已经写了，它们仍会在 `git status` 里显示成 modified。忽略即可。需要 stage 文件时，永远用具体文件名（`git add file1 file2`），**不要**用 `git add .` 或 `git add -A`，不然很容易把这些二进制误加进去。

## Commit style

**始终把 commits 拆开。** 每个 commit 都应该只表达一个逻辑改动。如果你这轮同时做了多个变化（例如一次 rename + 一次 rewrite + 新测试），在 push 前把它们拆成多个独立 commits。每个 commit 都应该能单独理解，也能单独回滚。

好的拆分示例：
- rename / move 和行为变化分开
- 测试基础设施（touchfiles、helpers）和测试实现分开
- 模板改动和生成文件重新生成分开
- 机械式重构和新功能分开

当用户说 “bisect commit” 或 “bisect and push” 时，把 staged / unstaged changes 拆成逻辑清晰的 commits 再 push。

## Community PR guardrails

在 review 或 merge 社区 PR 时，以下三类改动**必须**先 AskUserQuestion，再决定是否接受：

1. **碰 `ETHOS.md`**，这份文件代表 Garry 个人的 builder philosophy。外部贡献者或 AI agents 都不允许直接改。
2. **删除或弱化宣传性内容**，YC 相关表述、founder perspective、产品语气都是有意设计的。任何把这些内容描述成“不必要”或“太宣传”的 PR，都应该拒绝。
3. **改 Garry 的 voice**，skill templates、CHANGELOG、docs 里的语气、幽默感、直接程度和视角都不是通用写法。任何把它重写得更“中性”或更“专业”的 PR，都应该拒绝。

即使 agent 坚信某个改动对项目更好，这三类也都必须先 AskUserQuestion，拿到用户明确批准。没有例外。不能自动合并。不能“我先顺手清一下”。

## CHANGELOG + VERSION style

**VERSION 和 CHANGELOG 都是 branch-scoped 的。** 每个最终 ship 的 feature branch，都必须有它自己的版本 bump 和 CHANGELOG entry。entry 说的是**这个分支**新增了什么，而不是 main 上原本已经有的东西。

**什么时候写 CHANGELOG entry：**
- 在 `/ship` 时（Step 5），不是在开发中途，也不是中间提交阶段
- entry 要覆盖这个分支相对于 base branch 的**全部** commits
- 绝不能把新工作塞进一个已经在 main 落地的旧版本 entry 里。如果 main 已经是 v0.10.0.0，而你的分支新增了功能，那就 bump 到 v0.10.1.0 并写一条新 entry，不要去改 v0.10.0.0 那条

**写之前先问自己：**
1. 我现在在哪个 branch？这个 branch 到底改了什么？
2. base branch 上的那个版本是不是已经发布了？（如果是，就 bump 并新建 entry。）
3. 这个 branch 上是否已经有一条旧 entry 覆盖了之前的工作？（如果有，就替换成一条统一的最终版本 entry。）

**合并 main，不等于采用 main 的版本号。** 当你把 `origin/main` 合进 feature branch 时，main 可能带来了更高的 VERSION 和更多 CHANGELOG entries，但你的 branch 仍然需要它自己的 bump。如果 main 是 v0.13.8.0，而你的 branch 新增了功能，那你就应该 bump 到 v0.13.9.0 并写自己的 entry。绝不要把自己的变化硬塞进 main 上已经发布的那条 entry 里。你的 entry 应该排在最上面，因为你的 branch 才是下一个落地的。

**每次合并 main 之后，永远检查：**
- CHANGELOG 里是否有你这个 branch 自己的独立 entry，而不是混进 main 的 entries 里？
- VERSION 是否高于 main 当前的 VERSION？
- 你的 entry 是否在 CHANGELOG 顶部，位于 main 最新 entry 之上？
如果任一答案是否，就先修正，再继续。

**每次只要 CHANGELOG 做了会移动、增加、删除 entries 的编辑，** 立刻运行 `grep "^## \[" CHANGELOG.md`，核对整个版本序列是否连续，没有缺口也没有重复，再提交。如果丢了某个版本号，说明这次编辑弄坏了结构，先修再说。

CHANGELOG.md 是**给用户看的**，不是给贡献者看的。写法要像产品 release notes：

- 先讲用户现在**能做什么**，而不是实现细节
- 用平实语言，不用实现术语。写 “You can now...” 而不是 “Refactored the...”
- **绝不要提到 `TODOS.md`、内部 tracking、eval 基础设施，或任何 contributor-facing 细节。** 用户看不见这些，也不关心这些。
- 内部改动统一放在底部单独的 “For contributors” 区块
- 每一条 entry 都应该让人读完觉得：“哦，这个我想试试”
- 不要用术语黑话。写 “every question now tells you which project and branch you're in”，而不是 “AskUserQuestion format standardized across skill templates via preamble resolver.”

## AI effort compression

在估算或讨论工作量时，始终同时给出 human-team 时间和 CC+gstack 时间：

| Task type | Human team | CC+gstack | Compression |
|-----------|------------|-----------|-------------|
| Boilerplate / scaffolding | 2 天 | 15 分钟 | ~100x |
| Test writing | 1 天 | 15 分钟 | ~50x |
| Feature implementation | 1 周 | 30 分钟 | ~30x |
| Bug fix + regression test | 4 小时 | 15 分钟 | ~20x |
| Architecture / design | 2 天 | 4 小时 | ~5x |
| Research / exploration | 1 天 | 3 小时 | ~3x |

完整性现在很便宜。如果完整实现只是一个可以煮掉的 “lake”，不是需要多季度迁移的 “ocean”，那就不要推荐捷径。完整哲学见 skill preamble 里的 Completeness Principle。

## Search before building

在设计任何涉及并发、陌生模式、基础设施，或者运行时 / 框架可能已有内建能力的方案之前：

1. 搜 `{runtime} {thing} built-in`
2. 搜 `{thing} best practice {current year}`
3. 查官方 runtime / framework 文档

三层知识模型：tried-and-true（Layer 1）、new-and-popular（Layer 2）、first-principles（Layer 3）。其中 Layer 3 的价值最高。完整 builder philosophy 见 `ETHOS.md`。

## Local plans

贡献者可以把长程 vision docs 和 design documents 放在 `~/.gstack-dev/plans/`。这些文件只存在本地，不提交进 repo。review `TODOS.md` 时，也要顺手看一眼 `plans/`，看看有没有内容已经适合升级成 TODOs 或直接实现。

## E2E eval failure blame protocol

当 `/ship` 或其他 workflow 中的 E2E eval 失败时，**绝不要在没有证据的情况下说 “not related to our changes”**。这类系统里有很多看不见的耦合：preamble 文案变化会影响 agent 行为，一个 helper 改动会改时序，重新生成过的 `SKILL.md` 会改 prompt 上下文。

**只有满足下面条件，才允许把失败归因为 “pre-existing”：**
1. 在 main（或 base branch）上跑同一个 eval，并证明它在那里也失败
2. 如果 main 上通过，而你的 branch 上失败，那就是你的改动导致的，继续追责
3. 如果你没法在 main 上跑，就写明 “unverified — may or may not be related”，并在 PR body 里把它标成风险

没有凭据的 “pre-existing” 是偷懒。能证明再说，证明不了就别说。

## Long-running tasks: don't give up

跑 evals、E2E tests 或任何长时间后台任务时，**要持续轮询直到结束**。用 `sleep 180 && echo "ready"` + `TaskOutput` 每 3 分钟轮询一次。不要切到阻塞模式然后超时就放弃。也不要说 “完成了会通知我” 然后停止检查，要一直轮询到任务结束，或者用户明确让你停。

完整 E2E suite 可能要 30-45 分钟，也就是 10-15 轮轮询。都要做。每轮都汇报进度：哪些测试过了，哪些还在跑，目前有哪些失败。用户要看到的是完整结果，而不是“我之后再看”的承诺。

## E2E test fixtures: extract, don't copy

**绝不要把整份 `SKILL.md` 直接复制进 E2E test fixture。** 一份 `SKILL.md` 通常有 1500-2000 行。`claude -p` 读这么大的文件时，会因为 context 膨胀而超时、turn limit 变脆、测试耗时比必要值高 5-10 倍。

正确做法是，只抽出测试真正需要的那一段：

```typescript
// BAD — agent 读了 1900 行，token 都烧在无关内容上
fs.copyFileSync(path.join(ROOT, 'ship', 'SKILL.md'), path.join(dir, 'ship-SKILL.md'));

// GOOD — agent 只读约 60 行，38 秒结束，而不是卡到超时
const full = fs.readFileSync(path.join(ROOT, 'ship', 'SKILL.md'), 'utf-8');
const start = full.indexOf('## Review Readiness Dashboard');
const end = full.indexOf('\n---\n', start);
fs.writeFileSync(path.join(dir, 'ship-SKILL.md'), full.slice(start, end > start ? end : undefined));
```

另外，针对性调试 E2E failures 时：
- 要在**前台**跑（`bun test ...`），不要后台挂 `&` 再配 `tee`
- 不要 `pkill` 正在跑的 eval 进程然后重启，这会丢结果、还浪费钱
- 一次干净完整的运行，胜过三次被杀掉重来的运行

## Deploying to the active skill

active skill 位于 `~/.claude/skills/gstack/`。完成改动后：

1. Push 你的 branch
2. 在 skill 目录里 fetch 并 reset：`cd ~/.claude/skills/gstack && git fetch origin && git reset --hard origin/main`
3. 重建：`cd ~/.claude/skills/gstack && bun run build`

或者直接复制二进制：
- `cp browse/dist/browse ~/.claude/skills/gstack/browse/dist/browse`
- `cp design/dist/design ~/.claude/skills/gstack/design/dist/design`
