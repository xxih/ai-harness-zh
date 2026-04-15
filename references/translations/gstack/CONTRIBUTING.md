# Contributing to gstack

感谢你愿意把 gstack 做得更好。无论你只是修一个 skill prompt 里的错字，还是准备加一整套新 workflow，这份指南都会帮你尽快进入状态。

## Quick start

gstack 的 skills 本质上是 Markdown 文件，Claude Code 会从 `skills/` 目录里发现它们。正常情况下，它们放在 `~/.claude/skills/gstack/`（你的全局安装目录）。但如果你正在开发 gstack 自己，你真正想要的是让 Claude Code 直接读取**你当前工作树里**的 skills，这样改完就能立即生效，不需要复制，也不需要部署。

这就是 dev mode 的作用。它会把你的 repo 用 symlink 接进本地 `.claude/skills/` 目录，让 Claude Code 直接从你的 checkout 里读技能文件。

```bash
git clone <repo> && cd gstack
bun install                    # 安装依赖
bin/dev-setup                  # 激活 dev mode
```

现在你可以改任意 `SKILL.md`，然后在 Claude Code 里直接调用它（例如 `/review`），马上看到变化。开发结束后：

```bash
bin/dev-teardown               # 停用，回到全局安装版本
```

## Contributor mode

Contributor mode 会把 gstack 变成一个自我改进工具。开启后，Claude Code 会定期回顾自己这次使用 gstack 的体验，在每个 major workflow step 结束时打 0-10 分。如果不是 10 分，它会继续想：问题在哪里，如何复现，怎样才能更好，然后把报告写到 `~/.gstack/contributor-logs/`。

```bash
~/.claude/skills/gstack/bin/gstack-config set gstack_contributor true
```

这些日志是写给**你自己**看的。哪天某个问题烦到你想修了，报告已经帮你写好了。fork gstack，把自己的 fork symlink 到出问题的项目里，修掉它，再开 PR。

### Contributor workflow

1. **像平时一样使用 gstack**，contributor mode 会自动反思并记录问题
2. **查看日志：** `ls ~/.gstack/contributor-logs/`
3. **Fork 并 clone gstack**（如果你还没做）
4. **把你的 fork symlink 到出 bug 的项目里：**
   ```bash
   # 在你的核心项目中（就是 gstack 惹你烦的那个项目）
   ln -sfn /path/to/your/gstack-fork .claude/skills/gstack
   cd .claude/skills/gstack && bun install && bun run build && ./setup
   ```
   `setup` 会创建逐 skill 的 symlinks（`qa -> gstack/qa` 之类），并询问你要不要带前缀。传 `--no-prefix` 可以跳过提示，直接用短名。
5. **修问题**，你的改动会在这个项目里即时生效
6. **用真实使用场景验证**，去做那个刚才让你不爽的动作，确认问题已消失
7. **从你的 fork 开 PR**

这是最好的贡献方式：在你做真实工作的时候顺手修 gstack，而且就在你真正感受到痛点的那个项目里完成。

### Session awareness

当你同时打开 3+ 个 gstack sessions 时，每一个问题都会告诉你当前是哪个项目、哪个 branch、现在发生了什么。这样你就不会再盯着一个问题发愣：“等等，这是哪个窗口？” 这个格式在所有 skills 里是一致的。

## 在 gstack repo 里开发 gstack

如果你正在编辑 gstack 的 skills，并且想直接在同一个 repo 里用 gstack 自己来测试它，`bin/dev-setup` 就是为这个场景准备的。它会创建 `.claude/skills/` symlinks（被 gitignore），把它们指回当前工作树，让 Claude Code 用你的本地修改，而不是全局安装版本。

```text
gstack/                          <- 你的工作树
├── .claude/skills/              <- dev-setup 创建（gitignored）
│   ├── gstack -> ../../         <- 指回 repo 根目录的 symlink
│   ├── review -> gstack/review  <- 短名（默认）
│   ├── ship -> gstack/ship      <- 或者用 gstack-review、gstack-ship（如果 --prefix）
│   └── ...                      <- 每个 skill 一个 symlink
├── review/
│   └── SKILL.md                 <- 改这个，然后用 /review 测
├── ship/
│   └── SKILL.md
├── browse/
│   ├── src/                     <- TypeScript 源码
│   └── dist/                    <- 编译后二进制（gitignored）
└── ...
```

skill symlink 的命名由 prefix setting（`~/.gstack/config.yaml`）决定。默认是短名（`/review`、`/ship`）。如果你偏好 namespaced names（`/gstack-review`、`/gstack-ship`），运行 `./setup --prefix` 即可。

## Day-to-day workflow

```bash
# 1. 进入 dev mode
bin/dev-setup

# 2. 改一个 skill
vim review/SKILL.md

# 3. 在 Claude Code 中测试，改动是 live 的
#    > /review

# 4. 如果改了 browse 源码，记得重建二进制
bun run build

# 5. 今天结束了？清理 dev mode
bin/dev-teardown
```

## Testing & evals

### Setup

```bash
# 1. 复制 .env.example 并填上你的 API key
cp .env.example .env
# 编辑 .env → 设置 ANTHROPIC_API_KEY=sk-ant-...

# 2. 安装依赖（如果你还没装）
bun install
```

Bun 会自动加载 `.env`，不需要额外配置。Conductor workspaces 也会自动继承主 worktree 的 `.env`（见后文 “Conductor workspaces”）。

### Test tiers

| Tier | Command | Cost | 它测什么 |
|------|---------|------|----------|
| 1 — Static | `bun test` | 免费 | 命令校验、snapshot flags、SKILL.md 正确性、`TODOS-format.md` refs、observability 单测 |
| 2 — E2E | `bun run test:e2e` | ~\$3.85 | 通过 `claude -p` 完整跑 skill |
| 3 — LLM eval | `bun run test:evals` | 单独看约 \$0.15 | 对生成的 SKILL.md 文档做 LLM-as-judge 评分 |
| 2+3 | `bun run test:evals` | 合并约 \$4 | 同时跑 E2E + LLM-as-judge |

```bash
bun test                     # 只跑 Tier 1（每次 commit 都跑，<5s）
bun run test:e2e             # Tier 2：仅 E2E（需要 EVALS=1，不能嵌套在 Claude Code 里）
bun run test:evals           # Tier 2 + 3 一起跑（约 $4/次）
```

### Tier 1：静态校验（免费）

自动包含在 `bun test` 中，不需要 API keys。

- **Skill parser tests**（`test/skill-parser.test.ts`）：提取 `SKILL.md` 里 bash 代码块中的每一个 `$B` 命令，并与 `browse/src/commands.ts` 中的命令注册表比对。能抓命令拼写错误、已删除命令、无效 snapshot flags。
- **Skill validation tests**（`test/skill-validation.test.ts`）：校验 `SKILL.md` 只引用真实存在的命令与 flags，同时检查命令描述是否达到质量阈值。
- **Generator tests**（`test/gen-skill-docs.test.ts`）：验证模板系统本身，确认 placeholders 被正确展开，flags 带上值提示（例如 `-d <N>` 而不是裸 `-d`），关键命令的描述足够丰富（例如 `is` 要列出合法 states，`press` 要列出按键示例）。

### Tier 2：通过 `claude -p` 跑 E2E（约 \$3.85/次）

测试会拉起 `claude -p` 子进程，并使用 `--output-format stream-json --verbose`，实时流式读取 NDJSON，再扫描 browse 侧错误。这基本就是离“这个 skill 到底能不能端到端跑通”最近的验证方式。

```bash
# 必须在普通终端里跑，不能嵌套在 Claude Code 或 Conductor 里
EVALS=1 bun test test/skill-e2e-*.test.ts
```

- 通过 `EVALS=1` 环境变量显式开启，避免误触发昂贵测试
- 如果当前运行环境就是 Claude Code，会自动 skip（`claude -p` 无法嵌套）
- 先做 API connectivity pre-check，若 `ConnectionRefused` 则立刻失败，不烧预算
- 进度会实时打到 stderr：`[Ns] turn T tool #C: Name(...)`
- 会保存完整 NDJSON transcripts 和 failure JSON，便于排障
- 测试文件在 `test/skill-e2e-*.test.ts`，runner 逻辑在 `test/helpers/session-runner.ts`

### E2E observability

E2E tests 运行时，会在 `~/.gstack-dev/` 下生成机器可读 artifacts：

| Artifact | Path | 用途 |
|----------|------|------|
| Heartbeat | `e2e-live.json` | 当前测试状态（每次 tool call 更新） |
| Partial results | `evals/_partial-e2e.json` | 已完成测试结果（即使进程被杀也保留） |
| Progress log | `e2e-runs/{runId}/progress.log` | append-only 文本日志 |
| NDJSON transcripts | `e2e-runs/{runId}/{test}.ndjson` | 每个测试的原始 `claude -p` 输出 |
| Failure JSON | `e2e-runs/{runId}/{test}-failure.json` | 失败时的诊断数据 |

**Live dashboard：** 在另一个终端里运行 `bun run eval:watch`，就能看到正在运行的 live dashboard，包括已完成测试、当前测试和成本。传 `--tail` 还能额外显示 `progress.log` 的最后 10 行。

**Eval history tools：**

```bash
bun run eval:list            # 列出所有 eval runs（turns、duration、cost）
bun run eval:compare         # 比较两次 runs，显示逐测试差异与 Takeaway commentary
bun run eval:summary         # 汇总统计，并给出逐测试效率均值
```

**Eval comparison commentary：** `eval:compare` 会自动生成自然语言 Takeaway，解释两次运行之间发生了什么，例如：是否出现回退、哪里变好了、是否更省 turns、速度和成本是否有改善，以及最终的整体总结。这部分由 `eval-store.ts` 里的 `generateCommentary()` 负责。

这些 artifacts 不会被自动清理。它们会持续积累在 `~/.gstack-dev/` 里，供你做 post-mortem debugging 和长期趋势分析。

### Tier 3：LLM-as-judge（约 \$0.15/次）

使用 Claude Sonnet 对生成后的 `SKILL.md` 文档从三个维度打分：

- **Clarity**：AI agent 是否能无歧义地理解说明
- **Completeness**：所有命令、flags、用法模式是否都被覆盖
- **Actionability**：仅靠文档本身，agent 是否能把任务跑起来

每个维度 1-5 分。阈值要求是：每个维度都必须 **≥ 4**。此外，还有一项回归测试，会把当前生成文档和 `origin/main` 上人工维护的 baseline 做比较，要求当前分数不能更差。

```bash
# 需要 .env 里的 ANTHROPIC_API_KEY，通常随 bun run test:evals 一起跑
```

- 使用 `claude-sonnet-4-6`，保证评分稳定
- 测试位于 `test/skill-llm-eval.test.ts`
- 直接调用 Anthropic API，而不是 `claude -p`，因此在任何地方都能跑，包括 Claude Code 内部

### CI

GitHub Action（`.github/workflows/skill-docs.yml`）会在每次 push 和 PR 时运行 `bun run gen:skill-docs --dry-run`。只要生成出来的 `SKILL.md` 和 repo 中提交的不一致，CI 就会失败。这样就能在 merge 之前抓出陈旧文档。

测试都是直接针对 browse binary 本身跑的，不依赖 dev mode。

## Editing SKILL.md files

`SKILL.md` 文件是从 `.tmpl` 模板**生成**的。不要直接改 `.md`，下一次 build 就会覆盖掉。

```bash
# 1. 先改模板
vim SKILL.md.tmpl              # 或 browse/SKILL.md.tmpl

# 2. 为两个 host 重新生成
bun run gen:skill-docs
bun run gen:skill-docs --host codex

# 3. 跑健康检查（Claude 和 Codex 都会报告）
bun run skill:check

# 或者直接开 watch 模式，保存后自动重新生成
bun run dev:skill
```

模板编写最佳实践（自然语言优先于 bash-isms、动态 base branch 探测、`{{BASE_BRANCH_DETECT}}` 的使用），见 `CLAUDE.md` 中的 “Writing SKILL templates”。

要新增 browse command，就去改 `browse/src/commands.ts`。要新增 snapshot flag，就改 `browse/src/snapshot.ts` 里的 `SNAPSHOT_FLAGS`。然后重建。

## Dual-host development（Claude + Codex）

gstack 会为两个 host 生成 `SKILL.md`：**Claude**（`.claude/skills/`）和 **Codex**（`.agents/skills/`）。任何模板改动，都必须同时为两个 host 生成输出。

### 为两个 host 生成

```bash
# 生成 Claude 输出（默认）
bun run gen:skill-docs

# 生成 Codex 输出
bun run gen:skill-docs --host codex
# --host agents 也是 --host codex 的别名

# 或者直接用 build，它会顺便做双端生成 + 编译二进制
bun run build
```

### 两个 host 的差异

| Aspect | Claude | Codex |
|--------|--------|-------|
| 输出目录 | `{skill}/SKILL.md` | `.agents/skills/gstack-{skill}/SKILL.md`（在 setup 时生成，gitignored） |
| Frontmatter | 完整（name、description、allowed-tools、hooks、version） | 极简（只有 name + description） |
| 路径 | `~/.claude/skills/gstack` | `$GSTACK_ROOT`（repo 内是 `.agents/skills/gstack`，否则是 `~/.codex/skills/gstack`） |
| Hook skills | 通过 `hooks:` frontmatter 强制执行（由 Claude 生效） | 退化成 inline safety advisory prose（仅 advisory） |
| `/codex` skill | 包含（Claude 会包一层 codex exec） | 不包含（避免自指） |

### 测试 Codex 输出

```bash
# 跑全部静态测试（包含 Codex 校验）
bun test

# 检查两个 host 的生成物是否新鲜
bun run gen:skill-docs --dry-run
bun run gen:skill-docs --host codex --dry-run

# 健康面板会同时覆盖两端
bun run skill:check
```

### .agents/ 的 dev setup

运行 `bin/dev-setup` 时，它会在 `.claude/skills/` 和 `.agents/skills/`（如果适用）两边同时创建 symlinks，这样 Codex-compatible agents 也能发现你的开发版本 skills。`.agents/` 是在 setup 阶段由 `.tmpl` 模板生成出来的，默认 gitignored，不会被提交。

### Adding a new skill

新增 skill template 时，两端都会自动得到：

1. 创建 `{skill}/SKILL.md.tmpl`
2. 运行 `bun run gen:skill-docs`（Claude 输出）和 `bun run gen:skill-docs --host codex`（Codex 输出）
3. 动态模板发现机制会自动把它纳入，无需更新静态列表
4. 提交 `{skill}/SKILL.md`。`.agents/` 里的产物会在 setup 时生成，不提交

## Conductor workspaces

如果你用 [Conductor](https://conductor.build) 并行跑多个 Claude Code sessions，`conductor.json` 已经把 workspace 生命周期接好了：

| Hook | Script | 它做什么 |
|------|--------|----------|
| `setup` | `bin/dev-setup` | 从主 worktree 复制 `.env`、安装依赖、创建 skill symlinks |
| `archive` | `bin/dev-teardown` | 移除 skill symlinks，清理 `.claude/` 目录 |

每当 Conductor 创建一个新 workspace，`bin/dev-setup` 都会自动执行。它会通过 `git worktree list` 检测主 worktree，把你的 `.env` 复制过去，让 API keys 一起继承，并自动进入 dev mode，不需要你额外手动做任何事情。

**首次配置：** 把 `ANTHROPIC_API_KEY` 写进主 repo 的 `.env`（参考 `.env.example`），所有 Conductor workspaces 都会自动继承。

## Things to know

- **`SKILL.md` 是生成物。** 改 `.tmpl`，不要改 `.md`。改完运行 `bun run gen:skill-docs`。
- **`TODOS.md` 是统一 backlog。** 它按 skill / component 组织，并带有 P0-P4 优先级。`/ship` 会自动识别已完成项。所有 planning / review / retro skills 都会拿它做上下文。
- **改 browse 源码要重建。** 只要碰了 `browse/src/*.ts`，就运行 `bun run build`。
- **Dev mode 会遮蔽全局安装。** 项目内 skills 的优先级高于 `~/.claude/skills/gstack`。运行 `bin/dev-teardown` 才会恢复到全局版本。
- **Conductor workspaces 彼此独立。** 每个 workspace 都是独立 git worktree。`bin/dev-setup` 通过 `conductor.json` 自动执行。
- **`.env` 会跨 worktrees 传播。** 主 repo 配一次，Conductor workspaces 全都有。
- **`.claude/skills/` 是 gitignored。** 这些 symlinks 不会被 commit。

## 在真实项目里测试你的改动

**这是推荐的 gstack 开发方式。** 把你当前 checkout 的 gstack symlink 到你真正使用它的项目里。这样你一边做真实工作，一边就能即时验证改动。

### 第 1 步：给 checkout 建 symlink

```bash
# 在你的核心项目里（不是 gstack repo）
ln -sfn /path/to/your/gstack-checkout .claude/skills/gstack
```

### 第 2 步：运行 setup，创建逐 skill symlinks

仅仅有一个 `gstack` symlink 还不够。Claude Code 发现 skills 的方式，是逐个 skill 的 symlink（例如 `qa -> gstack/qa`、`ship -> gstack/ship`），而不是单看 `gstack/` 目录。因此还需要跑一次 `./setup`：

```bash
cd .claude/skills/gstack && bun install && bun run build && ./setup
```

setup 会问你要短名（`/qa`）还是 namespaced（`/gstack-qa`）。你的选择会保存在 `~/.gstack/config.yaml`，下次自动记住。想跳过提问，可传 `--no-prefix`（短名）或 `--prefix`（带前缀）。

### 第 3 步：开发

改模板，运行 `bun run gen:skill-docs`，下一次 `/review` 或 `/qa` 调用就会直接读到新版本。不需要重启。

### 切回稳定的全局安装

把项目内 symlink 删掉即可。Claude Code 会自动回退到 `~/.claude/skills/gstack/`：

```bash
rm .claude/skills/gstack
```

逐 skill 的 symlinks（`qa`、`ship` 等）仍然指向 `gstack/...`，因此会自动解析到全局安装版本。

### 切换 prefix mode

如果你第一次 vendoring gstack 时选了某种 prefix 方式，后来又想切换：

```bash
cd .claude/skills/gstack && ./setup --no-prefix   # 切换到 /qa、/ship
cd .claude/skills/gstack && ./setup --prefix      # 切换到 /gstack-qa、/gstack-ship
```

setup 会自动清理旧 symlinks，不需要手工打扫。

### 另一种做法：让全局安装直接指向某个 branch

如果你不想做 per-project symlink，也可以直接切全局安装：

```bash
cd ~/.claude/skills/gstack
git fetch origin
git checkout origin/<branch>
bun install && bun run build && ./setup
```

这会影响所有项目。要回到稳定版：`git checkout main && git pull && bun run build && ./setup`。

## Community PR triage（wave process）

当社区 PR 积累到一定数量时，按 wave 批量处理：

1. **Categorize**，按主题分组（security、features、infra、docs）
2. **Deduplicate**，若两条 PR 修的是同一件事，就选改动行数更少的那条，另一条关掉，并留言说明被谁替代
3. **Collector branch**，建一个 `pr-wave-N` 分支，把干净 PR merge 进去，脏 PR 手动解冲突，然后用 `bun test && bun run build` 验证
4. **Close with context**，每条被关闭的 PR 都要给评论，解释为什么关闭、是否被别的改动取代。贡献者是真的做了工作，必须用清晰沟通来尊重这点
5. **Ship as one PR**，把这一整波以一个 PR 合到 main，同时保留 merge commits 中的 attribution。PR 描述里附一张 summary table，说明哪些合了，哪些关了

第一轮 wave 的例子可见 [PR #205](../../pull/205)（v0.8.3）。

## Shipping your changes

当你对 skill 改动满意后：

```bash
/ship
```

它会跑测试、review diff、分层处理 Greptile comments（2-tier escalation）、管理 `TODOS.md`、升级版本号，并打开 PR。完整流程见 `ship/SKILL.md`。
