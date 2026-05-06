# workbench

个人日常使用的 Claude Code plugin。把自己最常用的 skill / command / agent 沉淀在这里，按需扩充。

## 目录结构

```
workbench/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── commands/
│   ├── align.md
│   ├── apply.md
│   ├── plan.md
│   ├── propose.md
│   └── run.md
└── skills/
    ├── architecture-decision-records/
    │   └── SKILL.md
    ├── nanospec/
    │   └── SKILL.md
    ├── quality-tdd/
    │   ├── SKILL.md
    │   └── references/
    │       └── testing-anti-patterns.md
    └── verification-before-completion/
        └── SKILL.md
```

## 当前内容

| 类型 | 名称 | 来源 | 说明 |
|------|------|------|------|
| skill | `nanospec` | openspec + nanospec | 串起 propose → plan → apply，配 align 纠偏与 run 一键跑完，产物落到 `nanospec/<name>/` |
| skill | `architecture-decision-records` | everything-claude-code | 在编码会话中捕捉架构决策，生成 ADR 文档 |
| skill | `quality-tdd` | packages/quality-workflows | 测试先行硬约束：没看到测试先失败就不算完成 TDD |
| skill | `verification-before-completion` | superpowers | 声明完成前必须跑验证命令并确认输出，证据先于结论 |
| command | `/propose` | — | 路由到 nanospec skill 的 propose 段 |
| command | `/plan` | — | 路由到 nanospec skill 的 plan 段 |
| command | `/apply` | — | 路由到 nanospec skill 的 apply 段 |
| command | `/align` | — | 路由到 nanospec skill 的 align 段 |
| command | `/run` | — | 路由到 nanospec skill 的 run 段（一键跑完） |

### nanospec 工作流约定

所有产物落到 `nanospec/<YYYYMMDD-task-name>/`：

```
nanospec/<name>/
├── brief.md          # 用户原始需求（run 场景 A 自动写入）
├── proposal.md       # propose 阶段产物：Why / What / Impact
├── design.md         # plan 阶段产物：Decisions / Goals / Trade-offs
├── tasks.md          # plan 阶段产物：可勾选任务清单
└── alignment.md      # align 阶段产物：偏差日志（按需创建）
```

阶段之间的接力：

```
propose ──► plan ──► apply
   │         │         │
   └─────────┴────► align ─► (回写 proposal / design / tasks)

run ：检测进度，从缺口处接力跑 propose → plan → apply
```

`nanospec/` 是项目级目录，建议加到 `.gitignore`，或按需选择性提交。

## 使用

### 方式 A：临时加载（单次会话）

直接在启动 Claude Code 时通过 `--plugin-dir` 指向本目录：

```bash
claude --plugin-dir /Users/xxih/workspace/ai-harness-zh/plugins/workbench
```

`--plugin-dir` 可以重复传，加载多个本地 plugin：

```bash
claude --plugin-dir ./plugins/workbench --plugin-dir ./plugins/another
```

仅对本次会话生效，不会写入任何配置。

### 方式 B：持久安装（通过本地 marketplace）

如果想长期启用、并能 `/plugin` 管理，需要先在某个目录建立 `marketplace.json` 把 workbench 注册进去，然后：

```bash
# 把 marketplace 加进来（user 作用域，仅本机）
claude plugin marketplace add /path/to/marketplace-dir

# 安装 workbench
claude plugin install workbench@<marketplace-name>
```

> 当前仓库还没有配 marketplace。要走这条路就再告诉我，我把 `.claude-plugin/marketplace.json` 也建出来。

### 验证 plugin 合法性

```bash
claude plugin validate /Users/xxih/workspace/ai-harness-zh/plugins/workbench
```

加载成功后，`architecture-decision-records` skill 会在检测到决策时刻时被激活，详见 `skills/architecture-decision-records/SKILL.md`。

## 添加新内容

* skill：在 `skills/<skill-name>/SKILL.md` 创建，frontmatter 至少包含 `name`、`description`
* command：在 `commands/<name>.md` 创建，frontmatter 包含 `description`
* agent：在 `agents/<name>.md` 创建，frontmatter 包含 `name`、`description`、`tools`、`model`
* hook：在 `hooks/` 内放置 JSON 配置

新增内容后，记得更新本 README 的"当前内容"表格。
