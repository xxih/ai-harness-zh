# gstack

> “我大概从去年 12 月开始，就几乎没有自己敲过哪怕一行代码了，这个变化非常大。” — [Andrej Karpathy](https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/)，No Priors 播客，2026 年 3 月

当我听到 Karpathy 这么说时，我想知道他到底是怎么做到的。一个人怎么能像二十人团队那样交付？Peter Steinberger 基本靠自己和 AI agents，就做出了 [OpenClaw](https://github.com/openclaw/openclaw) 这个拿到 247K GitHub stars 的项目。变革已经来了。只要工具对，一个 builder 单兵就能比传统团队推进得更快。

我是 [Garry Tan](https://x.com/garrytan)，[Y Combinator](https://www.ycombinator.com/) 的 President & CEO。我和成千上万家创业公司共事过，像 Coinbase、Instacart、Rippling，在它们还只是车库里一两个人的时候就见过。我加入 YC 之前，是 Palantir 最早的一批 eng / PM / designers 之一，也联合创办了 Posterous（后来卖给 Twitter），还做了 YC 内部社交网络 Bookface。

**gstack 就是我的答案。** 我做产品已经二十年了，而现在我写出来的代码比过去任何时候都多。最近 60 天里，我一边全职运营 YC，一边兼职写出了 **60 万+ 行 production code**（其中 35% 是测试），**每天 1 万到 2 万行**。这是我最近一次横跨 3 个项目的 `/retro`：一周内 **新增 140,751 行、362 次 commits、净增约 11.5 万 LOC**。

**2026 年，1,237 次 contributions，还在继续：**

![GitHub contributions 2026 — 1,237 contributions, massive acceleration in Jan-Mar](docs/images/github-2026.png)

**2013 年，我在 YC 做 Bookface 的时候（772 次 contributions）：**

![GitHub contributions 2013 — 772 contributions building Bookface at YC](docs/images/github-2013.png)

还是同一个人，不同的时代。差别就在工具。

**gstack 就是我现在的做法。** 它把 Claude Code 变成一个虚拟工程团队：会重新定义产品问题的 CEO、会锁架构的 eng manager、能看出 AI slop 的 designer、能找出生产级 bug 的 reviewer、会打开真实浏览器的 QA lead、会跑 OWASP + STRIDE 审计的 security officer、以及负责把 PR 发出去的 release engineer。23 个 specialist，8 个 power tools，全是 slash commands，全是 Markdown，全都免费，MIT license。

这是我的开源软件工厂。我每天都在用。之所以分享出来，是因为这些工具应该让所有人都能用到。

Fork 它，改进它，变成你自己的东西。如果你就是想喷免费开源软件，也可以，但我更希望你先试一下。

**这套东西适合谁：**
- **Founders 和 CEOs**，尤其是还想亲自 ship 的技术型创始人
- **第一次用 Claude Code 的人**，你拿到的是结构化角色，而不是一块空白 prompt
- **Tech leads 和 staff engineers**，希望每个 PR 都带着严格 review、QA 和 release automation

## 快速开始

1. 安装 gstack（30 秒，见下文）
2. 跑 `/office-hours`，描述你正在做什么
3. 对任意功能想法跑 `/plan-ceo-review`
4. 对任意有改动的分支跑 `/review`
5. 对你的 staging URL 跑 `/qa`
6. 到这里先停。你会知道这套东西是不是适合你。

## 安装，30 秒

**Requirements：** [Claude Code](https://docs.anthropic.com/en/docs/claude-code)、[Git](https://git-scm.com/)、[Bun](https://bun.sh/) v1.0+、[Node.js](https://nodejs.org/)（仅 Windows）

### 第 1 步：装到你的机器上

打开 Claude Code，直接粘贴下面这段。剩下的让 Claude 去做。

> Install gstack: run **`git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`** then add a "gstack" section to CLAUDE.md that says to use the /browse skill from gstack for all web browsing, never use mcp\_\_claude-in-chrome\_\_\* tools, and lists the available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review, /design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy, /canary, /benchmark, /browse, /connect-chrome, /qa, /qa-only, /design-review, /setup-browser-cookies, /setup-deploy, /retro, /investigate, /document-release, /codex, /cso, /autoplan, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn. Then ask the user if they also want to add gstack to the current project so teammates get it.

### 第 2 步：加进你的 repo，让队友也能直接用（可选）

> Add gstack to this project: run **`cp -Rf ~/.claude/skills/gstack .claude/skills/gstack && rm -rf .claude/skills/gstack/.git && cd .claude/skills/gstack && ./setup`** then add a "gstack" section to this project's CLAUDE.md that says to use the /browse skill from gstack for all web browsing, never use mcp\_\_claude-in-chrome\_\_\* tools, lists the available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review, /design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy, /canary, /benchmark, /browse, /connect-chrome, /qa, /qa-only, /design-review, /setup-browser-cookies, /setup-deploy, /retro, /investigate, /document-release, /codex, /cso, /autoplan, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn, and tells Claude that if gstack skills aren't working, run `cd .claude/skills/gstack && ./setup` to build the binary and register skills.

真实文件会直接 commit 到你的 repo 里，不是 submodule，所以 `git clone` 下来就能用。所有内容都待在 `.claude/` 里，不会去碰你的 PATH，也不会在后台常驻运行。

> **要贡献代码，或者需要完整历史？** 上面的命令用了 `--depth 1`，为了装得更快。如果你准备参与贡献，或者需要完整 git history，就改成完整 clone：
> ```bash
> git clone https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
> ```

### Codex、Gemini CLI 或 Cursor

gstack 适用于任何支持 [SKILL.md standard](https://github.com/anthropics/claude-code) 的 agent。skills 放在 `.agents/skills/` 里，会自动被发现。

安装到单个 repo：

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git .agents/skills/gstack
cd .agents/skills/gstack && ./setup --host codex
```

当 setup 从 `.agents/skills/gstack` 运行时，它会把生成后的 Codex skills 安装到同一个 repo 旁边，不会写入 `~/.codex/skills`。

也可以只给当前用户装一次：

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host codex
```

`setup --host codex` 会在 `~/.codex/skills/gstack` 下创建 runtime root，并把生成后的 Codex skills 链接到顶层。这样可以避免 source repo checkout 和实际运行时重复被发现。

或者也可以让 setup 自动探测你机器上已经装了哪些 agents：

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host auto
```

对于兼容 Codex 的 hosts，setup 现在同时支持两种方式：从 `.agents/skills/gstack` 做 repo-local install，或者从 `~/.codex/skills/gstack` 做 user-global install。31 个 skills 都能在所有支持的 agents 上工作。基于 hooks 的 safety skills（`careful`、`freeze`、`guard`）在非 Claude hosts 上会退化成 inline safety advisory prose。

### Factory Droid

gstack 也支持 [Factory Droid](https://factory.ai)。skills 会安装到 `.factory/skills/`，并自动被发现。敏感技能（`ship`、`land-and-deploy`、`guard`）会使用 `disable-model-invocation: true`，避免 Droids 自动调用它们。

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host factory
```

skills 会装到 `~/.factory/skills/gstack-*/`。重启 `droid` 让它重新扫描 skills，然后输入 `/qa` 开始。

## 看看它怎么工作

```
You:    I want to build a daily briefing app for my calendar.
You:    /office-hours
Claude: [asks about the pain — specific examples, not hypotheticals]

You:    Multiple Google calendars, events with stale info, wrong locations.
        Prep takes forever and the results aren't good enough...

Claude: I'm going to push back on the framing. You said "daily briefing
        app." But what you actually described is a personal chief of
        staff AI.
        [extracts 5 capabilities you didn't realize you were describing]
        [challenges 4 premises — you agree, disagree, or adjust]
        [generates 3 implementation approaches with effort estimates]
        RECOMMENDATION: Ship the narrowest wedge tomorrow, learn from
        real usage. The full vision is a 3-month project — start with
        the daily briefing that actually works.
        [writes design doc → feeds into downstream skills automatically]

You:    /plan-ceo-review
        [reads the design doc, challenges scope, runs 10-section review]

You:    /plan-eng-review
        [ASCII diagrams for data flow, state machines, error paths]
        [test matrix, failure modes, security concerns]

You:    Approve plan. Exit plan mode.
        [writes 2,400 lines across 11 files. ~8 minutes.]

You:    /review
        [AUTO-FIXED] 2 issues. [ASK] Race condition → you approve fix.

You:    /qa https://staging.myapp.com
        [opens real browser, clicks through flows, finds and fixes a bug]

You:    /ship
        Tests: 42 → 51 (+9 new). PR: github.com/you/app/pull/42
```

你说的是“daily briefing app”。agent 回给你的是“你真正要做的是 chief of staff AI”，因为它听的是你的痛点，不是你表面上的功能请求。8 个命令，从头到尾。这不是 copilot，这是团队。

## 这条 sprint 主线

gstack 不是一堆零散工具，而是一条流程。skills 会按 sprint 的顺序运行：

**Think → Plan → Build → Review → Test → Ship → Reflect**

每个 skill 都会把上下游接起来。`/office-hours` 会写 design doc，供 `/plan-ceo-review` 读取。`/plan-eng-review` 会写 test plan，供 `/qa` 承接。`/review` 抓到的 bug，会由 `/ship` 确认已经修好。因为每一步都知道前一步产出了什么，所以不会有东西掉进缝里。

| Skill | 你的 specialist | 它负责什么 |
|-------|----------------|-----------|
| `/office-hours` | **YC Office Hours** | 从这里开始。用 6 个强制问题在你写代码前重构产品理解。它会反驳你的 framing、挑战前提、产出实现路径备选。生成的 design doc 会喂给后续所有 skill。 |
| `/plan-ceo-review` | **CEO / Founder** | 重新定义问题。挖出这个需求里藏着的 10-star product。四种模式：Expansion、Selective Expansion、Hold Scope、Reduction。 |
| `/plan-eng-review` | **Eng Manager** | 锁定 architecture、data flow、diagrams、edge cases 和 tests。把隐藏假设逼出来。 |
| `/plan-design-review` | **Senior Designer** | 给每个设计维度打 0-10 分，解释 10 分长什么样，再把 plan 改到那个水平。AI Slop detection。交互式，一次设计决策对应一次 AskUserQuestion。 |
| `/design-consultation` | **Design Partner** | 从零建立完整 design system。研究竞品与语境，提出创意风险，生成逼真的产品 mockups。 |
| `/review` | **Staff Engineer** | 找出那些能过 CI、但会在生产炸掉的 bug。明显的问题自动修；完整性缺口会被标出来。 |
| `/investigate` | **Debugger** | 系统化 root-cause debugging。铁律是：先调查，后修复。追数据流，测假设，连续 3 次失败修复后就停。 |
| `/design-review` | **Designer Who Codes** | 用和 `/plan-design-review` 相同的审计方法，但会把发现的问题直接修掉。atomic commits，附前后截图。 |
| `/design-shotgun` | **Design Explorer** | 生成多版 AI 设计方案，在浏览器里开 comparison board，直到你选定方向。taste memory 会逐步向你的偏好偏置。 |
| `/design-html` | **Design Engineer** | 把 `/design-shotgun` 里批准的 mockup 生成为 production-quality 的 Pretext HTML，用计算式文本布局避免写死高度。文本会随窗口大小重新流动，内容高度也会跟着变。还会按设计类型智能路由到合适的 Pretext patterns，并识别 React / Svelte / Vue。 |
| `/qa` | **QA Lead** | 测你的 app，找 bug，用 atomic commits 修掉，然后重新验证。每个修复都会自动生成 regression test。 |
| `/qa-only` | **QA Reporter** | 和 `/qa` 用同一套方法，但只出报告，不改代码。纯 bug report。 |
| `/cso` | **Chief Security Officer** | OWASP Top 10 + STRIDE threat model。强调 zero-noise：17 条 false positive exclusions、8/10+ confidence gate、独立 finding verification。每条 finding 都给具体 exploit 场景。 |
| `/ship` | **Release Engineer** | 同步 main，跑测试，审 coverage，push，开 PR。即使你项目里还没有 test framework，它也会帮你 bootstrap。 |
| `/land-and-deploy` | **Release Engineer** | 合 PR，等 CI 和 deploy 完成，再验证 production 健康状态。一个命令，从“approved”到“verified in production”。 |
| `/canary` | **SRE** | deploy 之后的监控循环。盯 console errors、性能回退和页面失败。 |
| `/benchmark` | **Performance Engineer** | 建 page load times、Core Web Vitals 和资源体积基线。每个 PR 都能做 before / after 对比。 |
| `/document-release` | **Technical Writer** | 把项目文档更新到和你刚 ship 的内容一致。会自动抓出过期 README。 |
| `/retro` | **Eng Manager** | 团队感知的 weekly retro。有人维度拆解、shipping streaks、test health trends、成长机会都会给你。`/retro global` 还能跨你所有项目和 AI 工具（Claude Code、Codex、Gemini）一起跑。 |
| `/browse` | **QA Engineer** | 给 agent 装上眼睛。真实 Chromium，真实点击，真实截图。单条命令大约 100ms。`$B connect` 还能直接拉起你本机可见的 Chrome headed window，让你现场看它怎么操作。 |
| `/setup-browser-cookies` | **Session Manager** | 把你真实浏览器（Chrome、Arc、Brave、Edge）的 cookies 导入 headless session，测试需要登录的页面。 |
| `/autoplan` | **Review Pipeline** | 一个命令，拿到完整评审过的 plan。自动跑 CEO → design → eng review，并带着编码好的决策原则执行。只把真正需要你拍板的 taste decisions 暴露给你。 |
| `/learn` | **Memory** | 管 gstack 跨 session 学到了什么。查看、搜索、清理、导出项目特有的 patterns、pitfalls 和 preferences。learnings 会在 session 间累积，让 gstack 在你的代码库上越用越聪明。 |

### Power tools

| Skill | 它负责什么 |
|-------|-----------|
| `/codex` | **Second Opinion**，来自 OpenAI Codex CLI 的独立代码复核。三种模式：review（pass/fail gate）、adversarial challenge、open consultation。若 `/review` 和 `/codex` 都跑过，还会给 cross-model analysis。 |
| `/careful` | **Safety Guardrails**，在 destructive commands（`rm -rf`、`DROP TABLE`、force-push）之前发出警告。说一句 “be careful” 就能激活。任何警告都允许 override。 |
| `/freeze` | **Edit Lock**，把文件编辑范围限制到一个目录。debug 时防止误改范围外内容。 |
| `/guard` | **Full Safety**，把 `/careful` 和 `/freeze` 合在一起。适合最谨慎的 prod 工作。 |
| `/unfreeze` | **Unlock**，解除 `/freeze` 边界。 |
| `/connect-chrome` | **Chrome Controller**，启动带 Side Panel extension 的 Chrome。可以实时观察每一步操作、检查任意元素的 CSS、清理页面、截图。每个 tab 都有自己的 agent。 |
| `/setup-deploy` | **Deploy Configurator**，给 `/land-and-deploy` 做一次性配置。自动检测平台、production URL 和 deploy commands。 |
| `/gstack-upgrade` | **Self-Updater**，升级到最新版 gstack。能识别 global install 和 vendored install，并一起同步，顺便展示变化内容。 |

**[所有 skill 的示例、哲学和 workflow 深潜 →](docs/skills.md)**

## 并行 sprint

gstack 单跑一条 sprint 就已经很好用。十条一起跑，才是真的有意思。

**Design 是这套系统的中心。** `/design-consultation` 会从零搭你的 design system，研究这个空间，提出创意风险，并写 `DESIGN.md`。`/design-shotgun` 会生成多版视觉方案，并在浏览器里打开 comparison board，方便你选方向。`/design-html` 会把批准后的 mockup 生成为 production-quality HTML，底层用的是 Pretext，所以文本在 resize 时会真实 reflow，而不是靠硬编码高度勉强拼出来。接着 `/design-review` 和 `/plan-eng-review` 会继续读取你的设计选择。设计决策会贯穿整条系统。

**`/qa` 是一个非常大的 unlock。** 它让我能把并行 worker 数从 6 个拉到 12 个。Claude Code 会直接说出 *“I SEE THE ISSUE”*，然后真的去修、去补 regression test、再重新验证修复。这个变化改掉了我的工作方式。agent 现在真的有眼睛了。

**智能 review 路由。** 就像一个运作良好的 startup：CEO 不需要看 infra bug fixes，design review 也没必要介入纯后端改动。gstack 会记录哪些 review 已经跑过，判断当前该跑哪一种，然后直接做对的事。Review Readiness Dashboard 会在你 ship 前告诉你当前站在哪。

**全部都测。** 如果你的项目里还没有测试框架，`/ship` 会从零帮你 bootstrap。每次 `/ship` 都会产出 coverage audit。每次 `/qa` 修 bug 都会自动补 regression test。目标是 100% test coverage，让 vibe coding 变成安全的，而不是 yolo coding。

**`/document-release` 是你以前从来没有过的那种工程师。** 它会读遍项目里的每份文档，和 diff 交叉对照，把所有漂移的地方都更新掉。README、ARCHITECTURE、CONTRIBUTING、CLAUDE.md、TODOS，全都能自动保持最新。现在 `/ship` 甚至会自动调用它，所以文档不需要额外手动补。

**真实浏览器模式。** `$B connect` 会拉起你真正的 Chrome，用 Playwright 控制，但窗口是可见的。你会实时看到 Claude 点击、填写、跳转，还是同一扇窗口、同一块屏幕。窗口顶边会有一条很轻的绿色 shimmer，提示你当前哪个 Chrome 窗口归 gstack 控制。现有所有 browse commands 都不需要改。`$B disconnect` 会切回 headless。Chrome extension 的 Side Panel 会显示每条命令的实时活动流，还提供一个聊天侧栏，让你直接指挥 Claude。这个体验不是远程操控隐藏浏览器，而是共处同一个驾驶舱。

**Sidebar agent，你的 AI 浏览器助手。** 在 Chrome side panel 里输入自然语言指令，一个子 Claude 实例就会执行它们。“去 settings 页面然后截图。”“用测试数据填完这张表。”“遍历这个列表里的每个条目并提取价格。” 每个任务最多跑 5 分钟。sidebar agent 运行在隔离 session 中，不会影响你的主 Claude Code 窗口。就像浏览器里多了一双手。

**个人自动化。** sidebar agent 不只适合开发工作流。比如：“打开我孩子学校的家长门户，把其他家长的名字、手机号和照片都加进我的 Google Contacts。” 有两种方式拿到登录态：1）你在 headed browser 里手动登录一次，session 会保留；2）跑 `/setup-browser-cookies`，从你的真实 Chrome 导入 cookies。认证完成后，Claude 会自己浏览目录、提取数据、创建联系人。

**AI 卡住时的浏览器接管。** 碰到 CAPTCHA、auth wall、MFA prompt？`$B handoff` 会把完全同一个页面、同一套 cookies、同一组 tabs 用可见 Chrome 打开给你。你自己把问题处理掉，告诉 Claude 你处理完了，再用 `$B resume` 它就会从原地继续。连续 3 次失败后，agent 甚至会自动建议这么做。

**Multi-AI 第二视角。** `/codex` 会从 OpenAI 的 Codex CLI 拉来一个独立 review，完全不同的 AI，看的是同一份 diff。三种模式：带 pass/fail gate 的 code review、主动尝试把你代码打爆的 adversarial challenge、以及带 session continuity 的 open consultation。当 `/review`（Claude）和 `/codex`（OpenAI）都 review 过同一个分支时，你会拿到 cross-model analysis，看到哪些 findings 重合，哪些是某个模型独有的。

**按需开启的安全护栏。** 说一句 “be careful”，`/careful` 就会在任何 destructive command 前提醒你，像 `rm -rf`、`DROP TABLE`、force-push、`git reset --hard`。`/freeze` 会把编辑锁定到一个目录里，debug 时 Claude 就不会“顺手”修别的模块。`/guard` 把两者一起打开。`/investigate` 还会自动 freeze 到被调查的模块。

**主动技能建议。** gstack 会识别你当前处在哪个阶段，brainstorming、reviewing、debugging 还是 testing，然后建议最合适的 skill。不喜欢？说一句 “stop suggesting”，它就会跨 session 记住。

## 10 到 15 条并行 sprint

gstack 跑一条 sprint 就已经很强。十条一起跑，会发生质变。

[Conductor](https://conductor.build) 可以并行跑多个 Claude Code sessions，每个都在自己的隔离 workspace 里。一条 session 正在对新想法跑 `/office-hours`，另一条在对 PR 跑 `/review`，第三条在实现 feature，第四条在 staging 上跑 `/qa`，剩下六条分布在其他 branches 上。全部同时推进。我经常同时跑 10 到 15 条 sprint，这是目前现实可行的上限。

sprint 结构本身就是并行能成立的原因。没有流程，十个 agents 就是十个混乱源。有流程，think、plan、build、review、test、ship 每一步都有明确位置，每个 agent 都知道该做什么，也知道什么时候该停。你管理它们的方式，就像 CEO 管团队：关键决策你来盯，剩下的让系统自己跑。

---

免费，MIT license，开源。没有 premium tier，没有 waitlist。

我把自己构建软件的方式开源出来了。你可以 fork 走，做成你自己的版本。

> **我们在招人。** 想每天 ship 10K+ LOC，并帮忙把 gstack 打磨得更硬吗？
> 来 YC 吧，[ycombinator.com/software](https://ycombinator.com/software)
> 极具竞争力的薪资和股权，地点在旧金山 Dogpatch District。

## 文档

| 文档 | 覆盖内容 |
|-----|---------|
| [Skill Deep Dives](docs/skills.md) | 每个 skill 的哲学、示例和 workflow 说明（含 Greptile integration） |
| [Builder Ethos](ETHOS.md) | Builder 哲学：Boil the Lake、Search Before Building、three layers of knowledge |
| [Architecture](ARCHITECTURE.md) | 设计决策和系统内部结构 |
| [Browser Reference](BROWSER.md) | `/browse` 的完整命令参考 |
| [Contributing](CONTRIBUTING.md) | 开发环境、测试、contributor mode 和 dev mode |
| [Changelog](CHANGELOG.md) | 每个版本新增了什么 |

## 隐私与遥测

gstack 带有 **opt-in** 使用遥测，用来帮助改进项目。具体行为如下：

- **默认关闭。** 除非你明确点头，否则什么都不会发送。
- **第一次运行时，** gstack 会问你要不要分享匿名使用数据。你可以拒绝。
- **如果你选择开启，会发送什么：** skill 名称、耗时、成功 / 失败、gstack 版本、OS。就这些。
- **永远不会发送什么：** 代码、文件路径、repo 名称、branch 名称、prompts，或任何用户生成内容。
- **随时可改：** `gstack-config set telemetry off` 会立刻全部关闭。

数据存放在 [Supabase](https://supabase.com)（开源 Firebase 替代品）里。schema 放在 [`supabase/migrations/`](supabase/migrations/) 下，你可以自己核对它到底收集了什么。repo 里的 Supabase publishable key 是公开 key，类似 Firebase API key，row-level security policies 会拒绝所有直接访问。遥测统一经过带校验的 edge functions，里面会强制执行 schema checks、event type allowlists 和字段长度限制。

**本地 analytics 永远可用。** 运行 `gstack-analytics`，就能直接从本地 JSONL 文件看到你自己的使用 dashboard，不需要任何远端数据。

## 故障排查

**Skill 没显示出来？** `cd ~/.claude/skills/gstack && ./setup`

**`/browse` 挂了？** `cd ~/.claude/skills/gstack && bun install && bun run build`

**安装太旧？** 跑 `/gstack-upgrade`，或者在 `~/.gstack/config.yaml` 里设 `auto_upgrade: true`

**想要更短的命令？** `cd ~/.claude/skills/gstack && ./setup --no-prefix`，把 `/gstack-qa` 切回 `/qa`。你的选择会在后续升级里被记住。

**想要 namespaced commands？** `cd ~/.claude/skills/gstack && ./setup --prefix`，把 `/qa` 切成 `/gstack-qa`。如果你同时装了别的 skill packs，这会很有用。

**Codex 提示 “Skipped loading skill(s) due to invalid SKILL.md” ？** 你的 Codex skill descriptions 过期了。修复方式：`cd ~/.codex/skills/gstack && git pull && ./setup --host codex`。如果你装的是 repo-local 版本：`cd "$(readlink -f .agents/skills/gstack)" && git pull && ./setup --host codex`

**Windows 用户：** gstack 可以在 Windows 11 的 Git Bash 或 WSL 里运行。除了 Bun 以外，还需要 Node.js。原因是 Bun 在 Windows 下对 Playwright pipe transport 有一个已知 bug（[bun#4253](https://github.com/oven-sh/bun/issues/4253)）。browse server 会自动回退到 Node.js。确保 `bun` 和 `node` 都已经在你的 PATH 里。

**Claude 说它看不到 skills？** 确认你项目里的 `CLAUDE.md` 有一个 gstack section，内容像这样：

```
## gstack
Use /browse from gstack for all web browsing. Never use mcp__claude-in-chrome__* tools.
Available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review,
/design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy,
/canary, /benchmark, /browse, /connect-chrome, /qa, /qa-only, /design-review,
/setup-browser-cookies, /setup-deploy, /retro, /investigate, /document-release, /codex,
/cso, /autoplan, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn.
```

## License

MIT。永久免费。去做点东西出来。
