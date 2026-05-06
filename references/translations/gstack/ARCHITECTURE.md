# Architecture

这份文档解释 gstack **为什么** 会被设计成现在这样。安装和命令看 `CLAUDE.md`，贡献方式看 `CONTRIBUTING.md`。

## 核心思路

gstack 给 Claude Code 提供了一个持久化浏览器，以及一组带强主张的 workflow skills。真正难的是浏览器，其余大部分都是 Markdown。

关键洞察是：AI agent 与浏览器交互时，需要 **亚秒级延迟** 和 **持久状态**。如果每条命令都得冷启动浏览器，你每次 tool call 都得等 3-5 秒。如果浏览器在命令之间死掉，你会丢 cookies、tabs 和登录会话。所以 gstack 运行的是一个长生命周期的 Chromium daemon，而 CLI 通过 localhost HTTP 跟它对话。

```text
Claude Code                     gstack
─────────                      ──────
                               ┌──────────────────────┐
  Tool call: $B snapshot -i    │  CLI（编译后二进制）   │
  ─────────────────────────→   │  • 读取 state file     │
                               │  • POST /command      │
                               │    到 localhost:PORT   │
                               └──────────┬───────────┘
                                          │ HTTP
                               ┌──────────▼───────────┐
                               │  Server (Bun.serve)   │
                               │  • 派发命令            │
                               │  • 与 Chromium 通信    │
                               │  • 返回纯文本          │
                               └──────────┬───────────┘
                                          │ CDP
                               ┌──────────▼───────────┐
                               │  Chromium（headless） │
                               │  • 持久 tabs          │
                               │  • cookies 连续保留   │
                               │  • 30 分钟空闲超时     │
                               └───────────────────────┘
```

第一次调用会拉起整套链路，约 3 秒。之后每次调用约 100-200ms。

## 为什么选 Bun

Node.js 也能做，但 Bun 在这里更合适，原因有四个：

1. **可编译成单文件二进制。** `bun build --compile` 能产出一个约 58MB 的单文件可执行文件。运行时不需要 `node_modules`，不需要 `npx`，也不需要用户配置 PATH。二进制拿来就能跑。这点很重要，因为 gstack 是装在 `~/.claude/skills/` 里的，用户并不期待在那里管理一个 Node.js 工程。

2. **原生 SQLite。** Cookie 解密需要直接读取 Chromium 的 SQLite cookie 数据库。Bun 自带 `new Database()`，不需要 `better-sqlite3`、不需要 native addon 编译、也不需要 gyp。少一个跨机器崩掉的点。

3. **原生 TypeScript。** 开发时服务器直接以 `bun run server.ts` 启动。没有额外编译步骤，不需要 `ts-node`，也不用为了 debug source maps 绕路。编译后的二进制用于分发，源码用于开发。

4. **内建 HTTP server。** `Bun.serve()` 足够快，也足够简单，不需要 Express 或 Fastify。这个 server 只处理约 10 条 routes，引入一个框架反而是纯额外开销。

真正的瓶颈永远是 Chromium，不是 CLI，也不是 server。Bun 启动快（编译后二进制约 1ms，对比 Node 约 100ms）固然不错，但这不是选择它的根本原因。真正重要的是可编译二进制和原生 SQLite。

## Daemon model

### 为什么不每条命令启动一次浏览器？

Playwright 大概 2-3 秒能拉起 Chromium。只截一张图时这不算什么；但如果是一次有 20+ 条命令的 QA session，就会白白多出 40+ 秒浏览器启动开销。更糟的是，你会在命令之间丢失所有状态：cookies、localStorage、登录会话、已打开 tabs，全没了。

daemon model 带来的好处：

- **持久状态。** 登录一次后一直保持登录。打开的 tab 会留着。localStorage 会跨命令保留。
- **亚秒级命令。** 除第一次启动外，后面每次都只是一次 HTTP POST，往返约 100-200ms。
- **自动生命周期。** 第一次使用自动启动，空闲 30 分钟后自动关闭。不需要用户自己管理进程。

### State file

server 会写 `.gstack/browse.json`（通过临时文件 + rename 原子写入，权限 mode 0o600）：

```json
{ "pid": 12345, "port": 34567, "token": "uuid-v4", "startedAt": "...", "binaryVersion": "abc123" }
```

CLI 通过这个文件找到 server。如果文件不存在，或者 server 的 HTTP health check 失败，CLI 就会拉起一个新的 server。Windows 上，基于 PID 的进程存活判断在 Bun 二进制里不稳定，所以所有平台都以 health check（`GET /health`）作为主要的存活信号。

### Port selection

随机从 10000-60000 里挑端口，冲突时最多重试 5 次。这意味着 10 个 Conductor workspaces 可以零配置地各自跑自己的 browse daemon，互不抢端口。旧方案（扫描 9400-9409）在多 workspace 场景里经常坏。

### Version auto-restart

构建时会把 `git rev-parse HEAD` 写进 `browse/dist/.version`。每次 CLI 调用时，只要当前二进制版本和运行中 server 的 `binaryVersion` 不一致，CLI 就会杀掉旧 server，重启一个新的。这样“二进制陈旧”这一类 bug 会被彻底消掉：你只要重建了二进制，下一条命令就会自动用上新版本。

## Security model

### 只绑定 localhost

HTTP server 只绑定 `localhost`，不绑定 `0.0.0.0`，外部网络访问不到。

### Bearer token auth

每个 server session 都会生成一个随机 UUID token，并以 0o600 权限写进 state file（只有 owner 能读）。每个 HTTP 请求都必须带 `Authorization: Bearer <token>`。只要 token 不对，server 就返回 401。

这能防止同一台机器上的其他进程随便接管你的 browse server。只有 cookie picker UI（`/cookie-picker`）和 health check（`/health`）例外，它们只暴露在 localhost，且不执行命令。

### Cookie security

cookies 是 gstack 处理过的最敏感数据。设计原则如下：

1. **访问 Keychain 必须经过用户批准。** 每个浏览器的第一次 cookie import 都会触发 macOS Keychain 对话框，用户必须点击 “Allow” 或 “Always Allow”。gstack 不会静默读取凭据。

2. **解密全在进程内完成。** cookie 值只会在内存中解密（PBKDF2 + AES-128-CBC），然后加载进 Playwright context，永远不会把明文写盘。cookie picker UI 也不会展示 cookie 值，只会显示域名和数量。

3. **数据库只读。** gstack 会先把 Chromium cookie DB 复制到临时文件（避免和正在运行的浏览器争 SQLite 锁），再用只读方式打开。它不会修改你真实浏览器的 cookie 数据库。

4. **密钥缓存只在本次 session 内有效。** Keychain 密码和派生 AES key 都只缓存在当前 server 的内存里。server 一旦关闭（空闲超时或显式 stop），缓存就消失。

5. **日志里不出现 cookie 明文。** console、network、dialog logs 都不包含 cookie 值。`cookies` 命令只输出 cookie 元数据（domain、name、expiry），value 会被截断。

### 防止 shell injection

浏览器注册表（Comet、Chrome、Arc、Brave、Edge）是硬编码的。数据库路径也只由已知常量拼出来，不接受用户输入。访问 Keychain 时统一使用 `Bun.spawn()` 和显式参数数组，不走 shell 字符串插值。

## Ref system

refs（`@e1`、`@e2`、`@c1`）是 agent 在页面上点名元素的方式，不需要自己写 CSS selector 或 XPath。

### 工作机制

```text
1. Agent 运行：$B snapshot -i
2. Server 调用 Playwright 的 page.accessibility.snapshot()
3. 解析器遍历 ARIA tree，依次分配 refs：@e1、@e2、@e3...
4. 对每个 ref，构建一个 Playwright Locator：getByRole(role, { name }).nth(index)
5. 在 BrowserManager 实例上保存 Map<string, RefEntry>（含 role、name、Locator）
6. 把带注释的树作为纯文本返回

之后：
7. Agent 运行：$B click @e3
8. Server 把 @e3 解析成 Locator，然后执行 locator.click()
```

### 为什么用 Locator，而不是改 DOM？

一个看起来很直接的办法，是给 DOM 注入 `data-ref="@e1"` 这样的属性。但这会在以下场景坏掉：

- **CSP（Content Security Policy）。** 很多线上站点会阻止脚本修改 DOM。
- **React / Vue / Svelte hydration。** 框架的 reconciliation 可能把你注入的属性清掉。
- **Shadow DOM。** 外部脚本无法直接深入 shadow roots。

Playwright Locator 不依赖 DOM 注入。它走的是 accessibility tree（Chromium 自己维护）和 `getByRole()` 查询。没有 DOM mutation、没有 CSP 问题、没有框架冲突。

### Ref lifecycle

发生导航时，refs 会被清空（监听主 frame 的 `framenavigated` 事件）。这是正确行为，因为导航之后旧 locators 必然都失效了。agent 必须重新跑 `snapshot` 拿新 refs。这是故意设计成这样的：宁可让 stale refs 明确失败，也不能悄悄点错元素。

### Ref staleness detection

SPA 经常在不触发 `framenavigated` 的情况下直接改 DOM，例如 React router 跳转、tab 切换、modal 打开。这会导致 refs 失效，但 URL 不变。为了解决这个问题，`resolveRef()` 在使用任何 ref 前都会先异步做一次 `count()` 检查：

```text
resolveRef(@e3) → entry = refMap.get("e3")
                → count = await entry.locator.count()
                → if count === 0: throw "Ref @e3 is stale — element no longer exists. Run 'snapshot' to get fresh refs."
                → if count > 0: return { locator }
```

这样会在约 5ms 内快速失败，而不是等 Playwright 的 30 秒 action timeout。`RefEntry` 会把 `role` 和 `name` 元数据和 Locator 一起保存，因此错误消息还能告诉 agent 它失效的到底是什么元素。

### Cursor-interactive refs（`@c`）

`-C` flag 会找出那些可点击但不在 ARIA tree 里的元素，例如被设置了 `cursor: pointer` 的元素、带 `onclick` 的元素、或自定义 `tabindex` 元素。这些元素会拿到单独命名空间下的 `@c1`、`@c2` refs。这样就能覆盖很多框架把按钮渲染成 `<div>` 的自定义组件。

## Logging architecture

三组 ring buffers（每组 50,000 条，`O(1)` push）：

```text
Browser events → CircularBuffer（内存）→ 异步刷入 .gstack/*.log
```

console messages、network requests 和 dialog events 各自有自己的 buffer。每 1 秒 flush 一次，只把自上次以来新增的条目 append 到文件里。这带来的效果是：

- HTTP 请求处理永远不会被磁盘 I/O 阻塞
- 即使 server crash，日志也最多丢 1 秒
- 内存有上界（50K × 3 buffers）
- 磁盘文件是 append-only，外部工具也容易读

`console`、`network`、`dialog` 这些命令读的是内存 buffer，不是磁盘。磁盘文件主要用于 post-mortem debugging。

## SKILL.md 模板系统

### 问题

`SKILL.md` 文件负责告诉 Claude 如何使用 browse commands。如果文档里写了一个根本不存在的 flag，或者遗漏了刚新增的命令，agent 就会直接撞错误。纯手工维护的文档，迟早会和代码漂移。

### 方案

```text
SKILL.md.tmpl          （人工写的 prose + placeholders）
       ↓
gen-skill-docs.ts      （读取源码里的元数据）
       ↓
SKILL.md               （提交入库，自动生成的段落）
```

模板里保留那些需要人类判断的 workflows、tips 和 examples。真正容易漂移的部分，则在构建时从源码里填进去：

| Placeholder | 来源 | 生成内容 |
|-------------|------|----------|
| `{{COMMAND_REFERENCE}}` | `commands.ts` | 按类别整理的命令表 |
| `{{SNAPSHOT_FLAGS}}` | `snapshot.ts` | 带示例的 flag 参考 |
| `{{PREAMBLE}}` | `gen-skill-docs.ts` | 启动块：update check、session tracking、operational self-improvement、AskUserQuestion 格式 |
| `{{BROWSE_SETUP}}` | `gen-skill-docs.ts` | 二进制发现与 setup 说明 |
| `{{BASE_BRANCH_DETECT}}` | `gen-skill-docs.ts` | 面向 PR 的 skills 动态识别 base branch |
| `{{QA_METHODOLOGY}}` | `gen-skill-docs.ts` | `/qa` 与 `/qa-only` 共用的 QA 方法块 |
| `{{DESIGN_METHODOLOGY}}` | `gen-skill-docs.ts` | `/plan-design-review` 与 `/design-review` 共用的设计审计方法块 |
| `{{REVIEW_DASHBOARD}}` | `gen-skill-docs.ts` | `/ship` pre-flight 用的 Review Readiness Dashboard |
| `{{TEST_BOOTSTRAP}}` | `gen-skill-docs.ts` | `/qa`、`/ship`、`/design-review` 共用的测试框架发现、bootstrap 与 CI/CD 设置 |
| `{{CODEX_PLAN_REVIEW}}` | `gen-skill-docs.ts` | `/plan-ceo-review` 与 `/plan-eng-review` 的可选跨模型 plan review |
| `{{DESIGN_SETUP}}` | `resolvers/design.ts` | `$D` design binary 的发现逻辑，和 `{{BROWSE_SETUP}}` 对称 |
| `{{DESIGN_SHOTGUN_LOOP}}` | `resolvers/design.ts` | `/design-shotgun`、`/plan-design-review`、`/design-consultation` 共用的 comparison board 反馈循环 |

这个结构本身就能防漂移。如果命令存在于代码里，它就会出现在文档中；如果代码里不存在，它就不可能平白出现在文档中。

### preamble

每个 skill 都会先跑一个 `{{PREAMBLE}}` 块，再进入 skill 自己的逻辑。这个 preamble 通过一条 bash 命令同时处理五件事：

1. **Update check**，调用 `gstack-update-check`，告诉用户是否有可用升级
2. **Session tracking**，touch `~/.gstack/sessions/$PPID`，并统计过去两小时内活跃的 sessions。若同时有 3+ 个 sessions，所有 skills 都会进入 “ELI16 mode”，每次提问都要重新锚定上下文，因为用户此时在多窗口切换。
3. **Operational self-improvement**，每次 skill session 结束时，agent 都会回顾这次失败点，例如 CLI 报错、错误路径选择、项目特有怪癖，并把这些 operational learnings 记到项目级 JSONL 文件，供后续 session 复用。
4. **AskUserQuestion format**，统一提问格式：先给 context，再给 question，再给 `RECOMMENDATION: Choose X because ___`，最后给字母选项。全 skill 统一。
5. **Search Before Building**，在动手做基础设施或陌生模式前先搜索。三层知识：tried-and-true（Layer 1）、new-and-popular（Layer 2）、first-principles（Layer 3）。一旦 first-principles reasoning 证明 conventional wisdom 是错的，agent 会把这个时刻命名为 “eureka moment” 并记录下来。完整哲学见 `ETHOS.md`。

### 为什么是提交生成物，而不是运行时现生成？

原因有三个：

1. **Claude 在 skill load 时就会读 `SKILL.md`。** 用户调用 `/browse` 时，不存在额外 build step，所以文件必须预先存在且正确。
2. **CI 可以校验新鲜度。** `gen:skill-docs --dry-run` + `git diff --exit-code` 能在 merge 前抓出陈旧文档。
3. **Git blame 可用。** 你可以直接看出某条命令是在哪次 commit 里进入文档的。

### 模板测试分层

| Tier | 内容 | 成本 | 速度 |
|------|------|------|------|
| 1 — Static validation | 解析 `SKILL.md` 中每个 `$B` 命令，并校验是否在 registry 中 | 免费 | <2s |
| 2 — E2E via `claude -p` | 启真实 Claude session 跑每个 skill，检查错误 | 约 $3.85 | ~20 分钟 |
| 3 — LLM-as-judge | 用 Sonnet 评文档的清晰度 / 完整性 / 可执行性 | 约 $0.15 | ~30 秒 |

Tier 1 会在每次 `bun test` 时运行。Tier 2 和 3 通过 `EVALS=1` 控制。思路是：95% 的问题都应免费抓掉，只有真正需要判断的部分才用 LLM。

## Command dispatch

命令按 side effects 分三类：

- **READ**（`text`、`html`、`links`、`console`、`cookies` 等）：不修改状态，可安全重试，返回页面状态
- **WRITE**（`goto`、`click`、`fill`、`press` 等）：会改页面状态，不是幂等的
- **META**（`snapshot`、`screenshot`、`tabs`、`chain` 等）：偏 server-level 的操作，不太适合归进 read/write

这不只是组织方式。server dispatch 逻辑本身就依赖这个分类：

```typescript
if (READ_COMMANDS.has(cmd))  → handleReadCommand(cmd, args, bm)
if (WRITE_COMMANDS.has(cmd)) → handleWriteCommand(cmd, args, bm)
if (META_COMMANDS.has(cmd))  → handleMetaCommand(cmd, args, bm, shutdown)
```

`help` 命令会把三类命令全部列出来，方便 agents 自发现。

## Error philosophy

错误消息是写给 AI agents 看的，不是写给人看的。所以每一条都必须是可执行的：

- “Element not found” → “Element not found or not interactable. Run `snapshot -i` to see available elements.”
- “Selector matched multiple elements” → “Selector matched multiple elements. Use @refs from `snapshot` instead.”
- Timeout → “Navigation timed out after 30s. The page may be slow or the URL may be wrong.”

Playwright 原生错误会通过 `wrapError()` 重写：去掉内部堆栈噪音，补上下一步该做什么。agent 读完就该知道如何继续，而不需要人类介入。

### Crash recovery

server 不会尝试自愈。只要 Chromium crash（`browser.on('disconnected')`），server 就立刻退出。下一条命令时，CLI 会检测到 server 已死，然后自动重启。相比对着一个半死不活的浏览器进程尝试重连，这种做法更简单，也更可靠。

## E2E 测试基础设施

### Session runner（`test/helpers/session-runner.ts`）

E2E tests 通过完全独立的子进程拉起 `claude -p`，而不是走 Agent SDK，因为后者不能嵌套在 Claude Code sessions 里。runner 的流程是：

1. 把 prompt 写入临时文件（避免 shell escaping 问题）
2. 运行 `sh -c 'cat prompt | claude -p --output-format stream-json --verbose'`
3. 从 stdout 持续读取 NDJSON，实现实时进度
4. 和可配置 timeout 并行竞速
5. 把完整 NDJSON transcript 解析成结构化结果

`parseNDJSON()` 是纯函数，没有 I/O，也没有 side effects，因此可以单独测试。

### Observability 数据流

```text
  skill-e2e-*.test.ts
        │
        │ 生成 runId，把 testName + runId 传给每次调用
        │
  ┌─────┼──────────────────────────────┐
  │     │                              │
  │  runSkillTest()              evalCollector
  │  (session-runner.ts)         (eval-store.ts)
  │     │                              │
  │  每次 tool call：            每次 addTest()：
  │  ┌──┼──────────┐              savePartial()
  │  │  │          │                   │
  │  ▼  ▼          ▼                   ▼
  │ [HB] [PL]    [NJ]          _partial-e2e.json
  │  │    │        │             （原子覆盖）
  │  │    │        │
  │  ▼    ▼        ▼
  │ e2e-  prog-  {name}
  │ live  ress   .ndjson
  │ .json .log
  │
  │  on failure:
  │  {name}-failure.json
  │
  │  所有文件都在 ~/.gstack-dev/
  │  Run 目录：e2e-runs/{runId}/
  │
  │         eval-watch.ts
  │              │
  │        ┌─────┴─────┐
  │     read HB     read partial
  │        └─────┬─────┘
  │              ▼
  │        render dashboard
  │        （超过 10 分钟 stale 就警告）
```

**职责拆分：** session-runner 负责 heartbeat（当前测试运行状态），eval-store 负责 partial results（已完成测试状态）。watcher 两边都读。两者互相不知道彼此的存在，只通过文件系统共享数据。

**一切 observability 都是 non-fatal。** 所有 observability I/O 都包在 try/catch 里。即使写失败了，也绝不能让测试本身失败。真正的 source of truth 是测试结果本身，observability 只是 best-effort。

**机器可读的诊断字段：** 每个测试结果都包含 `exit_reason`（success、timeout、error_max_turns、error_api、exit_code_N）、`timeout_at_turn` 和 `last_tool_call`。这样你就能直接用 `jq` 查询：

```bash
jq '.tests[] | select(.exit_reason == "timeout") | .last_tool_call' ~/.gstack-dev/evals/_partial-e2e.json
```

### Eval 持久化（`test/helpers/eval-store.ts`）

`EvalCollector` 会积累测试结果，并用两种方式落盘：

1. **增量写入：** `savePartial()` 会在每个测试后写 `_partial-e2e.json`（原子方式：先写 `.tmp`，再 `fs.renameSync`）。即使进程被杀也能留下结果。
2. **最终写入：** `finalize()` 会写一个带时间戳的最终 eval 文件，例如 `e2e-20260314-143022.json`。partial 文件不会被清理，会和 final 文件一起保留，便于观测。

`eval:compare` 用于比较两次 eval runs。`eval:summary` 会汇总 `~/.gstack-dev/evals/` 里所有 runs 的统计。

### 测试分层

| Tier | 内容 | 成本 | 速度 |
|------|------|------|------|
| 1 — Static validation | 解析 `$B` 命令、校验 registry、observability 单测 | 免费 | <5s |
| 2 — E2E via `claude -p` | 拉起真实 Claude session，跑各个 skill，扫描错误 | 约 $3.85 | ~20 分钟 |
| 3 — LLM-as-judge | 用 Sonnet 评文档清晰度 / 完整性 / 可执行性 | 约 $0.15 | ~30 秒 |

Tier 1 会在每次 `bun test` 时运行。Tier 2 和 3 由 `EVALS=1` 控制。思路仍然一样：95% 问题免费抓，只有 judgment calls 和 integration testing 才用 LLM。

## 有意不放进来的内容

- **不做 WebSocket streaming。** HTTP request/response 更简单，可直接用 curl 调试，而且已经足够快。流式协议只会用复杂度换来边际收益。
- **不做 MCP protocol。** MCP 每个请求都有 JSON schema 和协议框架开销，还要求持久连接。纯 HTTP + 纯文本输出更省 tokens，也更好调试。
- **不做 multi-user support。** 每个 workspace 一个 server、一个用户。token auth 是 defense-in-depth，不是为了多租户。
- **暂不支持 Windows / Linux cookie decryption。** 当前只支持 macOS Keychain。Linux（GNOME Keyring / kwallet）和 Windows（DPAPI）在架构上可行，但还没实现。
- **不做 iframe 自动发现。** `$B frame` 已经支持跨 frame 交互（CSS selector、@ref、`--name`、`--url` 匹配），但 `snapshot` 时 ref system 不会自动爬所有 iframes。你必须先显式进入某个 frame context。
