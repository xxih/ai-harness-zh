# gstack x OpenClaw 集成

gstack 集成 OpenClaw 的方式是“提供方法论来源”，而不是“移植一套代码库”。
OpenClaw 的 ACP runtime 会原生拉起 Claude Code sessions。gstack 提供的是
planning discipline 和 methodology，让这些 sessions 运行得更好。

这是一套编码在 prompt text 里的轻量协议。没有 daemon。没有 JSON-RPC。
没有 compatibility matrix。prompt 本身就是桥。

## 架构

```
  OpenClaw                               gstack repo
  ─────────────────────                    ──────────────
  Orchestrator: messaging,                 Source of truth for
  calendar, memory, EA                     methodology + planning
       │                                        │
       ├── Native skills (conversational)       ├── Generates native skills
       │   office-hours, ceo-review,            │   via gen-skill-docs pipeline
       │   investigate, retro                   │
       │                                        ├── Generates gstack-lite
       ├── sessions_spawn(runtime: "acp")       │   (planning discipline)
       │       │                                │
       │       └── Claude Code                  ├── Generates gstack-full
       │           └── gstack installed at      │   (complete pipeline)
       │               ~/.claude/skills/gstack  │
       │                                        └── docs/OPENCLAW.md (this file)
       └── Dispatch routing (AGENTS.md)
```

## Dispatch Routing

OpenClaw 会在 spawn 时决定使用哪一层 gstack 支持：

| Tier | 何时使用 | Prompt prefix |
|------|----------|---------------|
| **Simple** | 单文件修改、typo、config changes | 不注入 gstack context |
| **Medium** | 多文件 feature、refactor | 追加 `gstack-lite CLAUDE.md` |
| **Heavy** | 需要特定 gstack skill | `"Load gstack. Run /X"` |
| **Full** | 完整 feature、objective 或 project | 追加 `gstack-full pipeline` |
| **Plan** | “帮我规划一个 Claude Code project” | 追加 `gstack-plan pipeline` |

### 决策启发式

- 能否在不到 10 行代码内完成？ -> **Simple**
- 会改多个文件，但路径很明确？ -> **Medium**
- 用户是否点名具体 skill（`/cso`、`/review`、`/qa`）？ -> **Heavy**
- 这是一个 feature、project 或 objective（而不是单个 task）？ -> **Full**
- 用户是否只想先规划 Claude Code project，而不是立刻实现？ -> **Plan**

### Dispatch routing 指南（给 AGENTS.md 用）

完整、可直接粘贴的 section 在 `openclaw/agents-gstack-section.md`。
把它复制进你的 OpenClaw `AGENTS.md`。

关键行为规则（这些要放在 dispatch tiers 之前）：

1. **Always spawn, never redirect.** 当用户要求使用任意 gstack skill 时，
   一律直接 spawn Claude Code session。不要让用户自己去打开 Claude Code。
2. **Resolve the repo.** 如果用户指定 repo，就设置 working directory。
   如果 repo 不明确，就追问仓库名。
3. **Autoplan runs end-to-end.** 对 `/autoplan` 来说，要直接 spawn，并让它跑完整条
   pipeline，然后在 chat 里把结果报告回来。用户不应为了这件事离开 Telegram。

### 处理 CLAUDE.md 冲突

如果 spawn Claude Code 的 repo 本身已经有 `CLAUDE.md`，请把 gstack-lite/full
作为新 section **追加**进去，而不是覆盖仓库原有说明。

## gstack 为 OpenClaw 生成什么

所有产物都放在 `openclaw/` 目录，由下面的命令生成：

`bun run gen:skill-docs --host openclaw`

### gstack-lite（Medium tier）

`openclaw/gstack-lite-CLAUDE.md`：约 15 行的 planning discipline：

1. 修改前先读完相关文件
2. 先写一份 5 行计划：做什么、为什么、改哪些文件、测试用例、风险
3. 有歧义时用决策原则收敛
4. 汇报完成前先 self-review
5. 完成汇报包含：交付内容、做过的决策、仍不确定的点

A/B 测试结果：耗时约 2x，但输出质量明显更好。

### gstack-full（Full tier）

`openclaw/gstack-full-CLAUDE.md`：串起已有 gstack skills：

1. 阅读 `CLAUDE.md`，理解项目
2. 运行 `/autoplan`（CEO + eng + design review）
3. 实现被批准的计划
4. 运行 `/ship` 创建 PR
5. 报告 PR URL 和关键决策

### gstack-plan（Plan tier）

`openclaw/gstack-plan-CLAUDE.md`：完整评审链路，但不做实现：

1. 运行 `/office-hours` 产出 design doc
2. 运行 `/autoplan`（CEO + eng + design + DX reviews + codex adversarial）
3. 把审阅后的 plan 保存到 `plans/<project-slug>-plan-<date>.md`
4. 汇报：plan 路径、摘要、关键决策、推荐下一步

orchestrator 会把 plan 链接持久化到自己的 memory store（brain repo、
knowledge base，或你在 `AGENTS.md` 里配置的其他位置）。当用户准备开始构建时，
再 spawn 一个引用该 plan 的 FULL session。

### 原生 methodology skills

发布到 ClawHub。使用 `clawhub install` 安装：

- `gstack-openclaw-office-hours` — 产品盘问（6 个 forcing questions）
- `gstack-openclaw-ceo-review` — 战略挑战（10-section review，4 modes）
- `gstack-openclaw-investigate` — 运维式排障（4-phase methodology）
- `gstack-openclaw-retro` — 运维式复盘（weekly review）

源码位于 gstack repo 的 `openclaw/skills/`。这些是针对 OpenClaw
conversational context 手工改写的方法论 skills。
不携带 gstack 基础设施（没有 browse、没有 telemetry、没有 preamble）。

## Spawned session detection

当 Claude Code 运行在 OpenClaw spawn 出来的 session 中时，
`OPENCLAW_SESSION` environment variable 应该被设置。gstack 会据此调整行为：

- 跳过 interactive prompts（自动选择推荐项）
- 跳过 upgrade checks 与 telemetry prompts
- 更聚焦任务完成与 prose reporting

在 `sessions_spawn` 中这样设置 env var：

`env: { OPENCLAW_SESSION: "1" }`

## 安装

对 OpenClaw 用户来说：直接告诉 OpenClaw agent，`install gstack for openclaw.`

agent 应当：

1. 把 gstack-lite `CLAUDE.md` 安装进 coding session templates
2. 安装 4 个原生 methodology skills
3. 把 dispatch routing 加进 `AGENTS.md`
4. 用一次 test spawn 验证

对 gstack 开发者来说：`./setup --host openclaw` 会生成这份文档。
真正的产物由 `bun run gen:skill-docs --host openclaw` 生成。

## 我们不做什么

- 不做 dispatch daemon（ACP 已负责 session spawning）
- 不做 Clawvisor relay（不需要额外 security layer）
- 不做双向 learnings bridge（brain repo 就是 knowledge store）
- 不做 JSON schemas 或 protocol versioning
- 不把 gstack 的 `SOUL.md` 带过来（OpenClaw 有自己的）
- 不做完整 skill porting（coding skills 仍保持 Claude Code 原生）
