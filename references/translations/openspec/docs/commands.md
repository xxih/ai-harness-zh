# Commands

这是 OpenSpec slash commands 的参考手册。这些命令会在你的 AI coding assistant 聊天界面中调用（例如 Claude Code、Cursor、Windsurf）。

关于常见 workflow 模式与各命令的适用时机，请见 [Workflows](workflows.md)。CLI 命令请见 [CLI](cli.md)。

## Quick Reference

### Default Quick Path (`core` profile)

| Command | Purpose |
|---------|---------|
| `/opsx:propose` | 一步创建 change 并生成规划工件 |
| `/opsx:explore` | 在提交 change 前先梳理想法 |
| `/opsx:apply` | 按 change 中的 tasks 执行实现 |
| `/opsx:sync` | 将 delta specs 合并回主 specs |
| `/opsx:archive` | 归档已完成的 change |

### Expanded Workflow Commands（自定义 workflow 选择）

| Command | Purpose |
|---------|---------|
| `/opsx:new` | 创建新的 change scaffold |
| `/opsx:continue` | 基于依赖创建下一个工件 |
| `/opsx:ff` | Fast-forward：一次创建全部规划工件 |
| `/opsx:verify` | 验证实现是否与工件一致 |
| `/opsx:bulk-archive` | 一次归档多个 change |
| `/opsx:onboard` | 引导式走完整个 workflow |

默认全局 profile 是 `core`。如果你想启用 expanded workflow 命令，运行 `openspec config profile`，选择 workflows，再在项目内执行 `openspec update`。

---

## Command Reference

### `/opsx:propose`

一步创建新的 change，并生成实现前需要的规划工件。这是 `core` profile 下默认的起始命令。

**Syntax:**
```text
/opsx:propose [change-name-or-description]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name-or-description` | 否 | kebab-case 的 change 名称，或自然语言描述 |

**What it does:**
- 创建 `openspec/changes/<change-name>/`
- 生成实现前需要的工件（对 `spec-driven` 来说即 proposal、specs、design、tasks）
- 在 change 已准备好交给 `/opsx:apply` 时停下

**Example:**
```text
你：/opsx:propose add-dark-mode

AI：已创建 openspec/changes/add-dark-mode/
    ✓ proposal.md
    ✓ specs/ui/spec.md
    ✓ design.md
    ✓ tasks.md
    已准备进入实现。运行 /opsx:apply。
```

**Tips:**
- 这是最快的端到端路径
- 如果你想逐步控制工件创建，启用 expanded workflows 后可以改用 `/opsx:new` + `/opsx:continue`

---

### `/opsx:explore`

在正式提交 change 之前，先思考想法、调查问题、澄清需求。

**Syntax:**
```
/opsx:explore [topic]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `topic` | 否 | 你想探索或调查的话题 |

**What it does:**
- 打开一个不要求固定结构的探索式对话
- 调查代码库，回答问题
- 比较不同方案与路径
- 用可视化图示帮助理清思路
- 当结论足够明确时，可切换到 `/opsx:propose`（默认）或 `/opsx:new`（expanded workflow）

**Example:**
```text
你：/opsx:explore

AI：你想探索什么？

你：移动端的认证应该怎么做比较好？

AI：我先看看你当前的认证方案...
    [分析代码库]

    我看到你当前在 Web 端使用的是 session-based auth。
    对移动端来说，主要有三种选择：

    1. JWT tokens（无状态，支持离线）
    2. OAuth2（如果需要第三方登录）
    3. 继续扩展现有 session（更简单，但依赖连接）

    你的 API 已经配好了 CORS。你想往哪个方向走？

你：先走 JWT。能开始一个 change 吗？

AI：可以。运行 /opsx:propose add-jwt-auth 开始。
```

**Tips:**
- 当需求不清晰或需要调查时使用
- 探索阶段不会创建任何工件
- 很适合在定方案前比较多个方向
- 可以直接读取文件、搜索代码库

---

### `/opsx:new`

创建新的 change scaffold。它会先建好 change 目录，然后等待你通过 `/opsx:continue` 或 `/opsx:ff` 生成工件。

这个命令属于 expanded workflow 集合，不包含在默认 `core` profile 里。

**Syntax:**
```
/opsx:new [change-name] [--schema <schema-name>]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | 否 | change 目录名称，未提供时会提示输入 |
| `--schema` | 否 | 要使用的 workflow schema（默认来自 config 或 `spec-driven`） |

**What it does:**
- 创建 `openspec/changes/<change-name>/` 目录
- 在 change 目录里创建 `.openspec.yaml` 元数据文件
- 显示当前最先可创建的工件模板
- 如未提供 change 名称或 schema，会提示你补全

**What it creates:**
```
openspec/changes/<change-name>/
└── .openspec.yaml    # Change metadata（schema、创建时间）
```

**Example:**
```
你：/opsx:new add-dark-mode

AI：已创建 openspec/changes/add-dark-mode/
    Schema: spec-driven

    已准备创建：proposal
    使用 /opsx:continue 创建，或用 /opsx:ff 一次创建全部工件。
```

**Tips:**
- 使用清晰的名称：`add-feature`、`fix-bug`、`refactor-module`
- 避免过于泛的名字，如 `update`、`changes`、`wip`
- schema 也可以预先在项目配置中设定（`openspec/config.yaml`）

---

### `/opsx:continue`

沿着依赖链创建下一个工件。每次只创建一个，适合增量推进。

**Syntax:**
```
/opsx:continue [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | 否 | 要继续推进哪个 change（若上下文足够，系统会自动推断） |

**What it does:**
- 查询工件依赖图
- 显示哪些工件已 ready、哪些还被阻塞
- 创建第一个可创建的工件
- 为获取上下文读取它依赖的文件
- 告诉你创建完成后又有哪些工件被解锁

**Example:**
```
你：/opsx:continue

AI：Change: add-dark-mode

    Artifact status:
    ✓ proposal    （已完成）
    ◆ specs       （可创建）
    ◆ design      （可创建）
    ○ tasks       （被阻塞，需要：specs）

    正在创建 specs...

    [读取 proposal.md，并据此创建 specs]

    ✓ 已创建 openspec/changes/add-dark-mode/specs/ui/spec.md

    现在可创建：tasks
    运行 /opsx:continue 创建下一个工件。
```

**Tips:**
- 当你想逐个审阅工件时使用
- 适合复杂 change，需要更强过程控制时
- 可能会一次解锁多个工件
- 你可以先手动编辑已创建工件，再继续下一步

---

### `/opsx:ff`

Fast-forward 创建工件。一次生成全部规划工件。

**Syntax:**
```
/opsx:ff [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | 否 | 要 fast-forward 的 change（若上下文足够，系统会自动推断） |

**What it does:**
- 按依赖顺序一次创建全部工件
- 用 todo list 跟踪进度
- 在所有 `apply-required` 工件完成后停止
- 创建每个工件前都会先读取其依赖

**Example:**
```
你：/opsx:ff add-dark-mode

AI：正在 fast-forward add-dark-mode...

    ✓ 创建 proposal.md
    ✓ 创建 specs/ui/spec.md
    ✓ 创建 design.md
    ✓ 创建 tasks.md

    所有规划工件已完成！
    已准备进入实现。运行 /opsx:apply 开始。
```

**Tips:**
- 当你对目标已有清晰认知时使用
- 对直接明确的改动，比 `/opsx:continue` 更快
- 即使一口气生成完，也仍然可以回头编辑工件
- 适合小到中型功能

---

### `/opsx:apply`

按 change 中的任务执行实现。它会逐项处理 task list、写代码，并勾掉已完成项。

**Syntax:**
```
/opsx:apply [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | 否 | 要实现哪个 change（若上下文足够，系统会自动推断） |

**What it does:**
- 读取 `tasks.md` 并识别未完成任务
- 逐项执行任务
- 需要时写代码、创建文件、运行测试
- 用 `[x]` 勾选已完成任务

**Example:**
```
你：/opsx:apply

AI：正在实现 add-dark-mode...

    读取 tasks.md：
    - [ ] 1.1 Create ThemeContext
    - [ ] 1.2 Add CSS custom properties
    - [ ] 1.3 Implement localStorage persistence

    正在处理 1.1：Create ThemeContext...
    [创建 src/context/ThemeContext.tsx]

    ✓ 1.1 完成

    正在处理 1.2：Add CSS custom properties...
    [更新 src/styles/globals.css]

    ✓ 1.2 完成
    ...
```

**Tips:**
- 中途被打断后可以从上次停下的地方继续
- 并行处理多个 change 时，可以显式指定 change 名称
- 完成状态以 `tasks.md` 中的 checkbox 为准

---

### `/opsx:verify`

验证实现是否与 change 工件一致。它会检查完整性、正确性与一致性。

**Syntax:**
```
/opsx:verify [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | 否 | 要验证哪个 change（若上下文足够，系统会自动推断） |

**What it does:**
- 从三个维度检查实现质量
- 在代码库中搜索实现证据
- 将问题按 CRITICAL、WARNING、SUGGESTION 分类汇报
- 不阻止 archive，但会把问题提前暴露出来

**Verification dimensions:**

| Dimension | What it validates |
|-----------|-------------------|
| **Completeness** | 所有任务完成、所有 requirement 已实现、场景有覆盖 |
| **Correctness** | 实现符合 spec 意图，边界条件已处理 |
| **Coherence** | 设计决策已体现在代码中，模式保持一致 |

**Example:**
```
你：/opsx:verify

AI：正在验证 add-dark-mode...

    COMPLETENESS
    ✓ tasks.md 中 8 个任务全部勾选
    ✓ specs 中所有 requirement 都能在代码里找到对应实现
    ⚠ “System preference detection” 场景没有测试覆盖

    CORRECTNESS
    ✓ 实现符合 spec 意图
    ✓ 场景里的边界条件已处理
    ✓ 错误状态与 spec 定义一致

    COHERENCE
    ✓ 设计决策已反映在代码结构中
    ✓ 命名与 design.md 保持一致
    ⚠ design 提到 “CSS variables”，但实现使用了 Tailwind classes

    SUMMARY
    ─────────────────────────────
    Critical issues: 0
    Warnings: 2
    Ready to archive: Yes (with warnings)

    Recommendations:
    1. 为 system preference detection 补一条测试
    2. 让 design.md 反映 Tailwind 的实现，或重构回 CSS variables
```

**Tips:**
- 归档前运行，能更早发现偏差
- Warning 不会阻止归档，但说明仍有风险
- 适合在提交前复审 AI 的工作
- 能帮助你发现工件与实现之间的 drift

---

### `/opsx:sync`

**可选命令。** 将 change 中的 delta specs 合并进主 specs。`archive` 会在需要时主动提示 sync，所以通常不需要手动执行。

**Syntax:**
```
/opsx:sync [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | 否 | 要 sync 哪个 change（若上下文足够，系统会自动推断） |

**What it does:**
- 读取 change 目录中的 delta specs
- 解析 ADDED/MODIFIED/REMOVED/RENAMED 区块
- 将改动合并进主 `openspec/specs/` 目录
- 保留 delta 中未提及的原有内容
- 不归档 change（change 仍保持 active）

**Example:**
```text
你：/opsx:sync

AI：正在同步 add-dark-mode 的 delta specs...

    读取：openspec/changes/add-dark-mode/specs/ui/spec.md
    目标：openspec/specs/ui/spec.md

    待应用变更：
    ✓ ADDED：Theme Selection requirement（2 个 scenario）
    ✓ ADDED：Accessibility requirement（1 个 scenario）

    正在合并...
    ✓ openspec/specs/ui/spec.md 已更新

    Change 仍保持 active。准备完成时运行 /opsx:archive。
```

**When to use manually:**

| Scenario | Use sync? |
|----------|-----------|
| change 会持续较长时间，希望先把 specs 同步回 main | Yes |
| 多个并行 change 需要以更新后的 specs 为基础 | Yes |
| 想单独预览或审查这次 merge | Yes |
| 这是一次快速 change，准备直接 archive | No（archive 会处理） |

**Tips:**
- sync 是智能合并，不是简单 copy-paste
- 可以把 scenario 加进已有 requirement，而不产生重复
- sync 后 change 仍保持 active，不会自动归档
- 大多数用户不会直接调用它，archive 在需要时会主动提示

---

### `/opsx:archive`

归档已完成的 change。它会完成收尾，并将 change 移动到 archive 目录。

**Syntax:**
```
/opsx:archive [change-name]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-name` | 否 | 要归档哪个 change（若上下文足够，系统会自动推断） |

**What it does:**
- 检查工件是否齐全
- 检查 tasks 完成度（如未完成会警告）
- 如果 delta specs 还没 sync，会提供同步选项
- 将 change 目录移动到 `openspec/changes/archive/YYYY-MM-DD-<name>/`
- 保留全部工件，方便之后审计

**Example:**
```text
你：/opsx:archive

AI：正在归档 add-dark-mode...

    Artifact status:
    ✓ proposal.md 已存在
    ✓ specs/ 已存在
    ✓ design.md 已存在
    ✓ tasks.md 已存在（8/8 任务已完成）

    Delta specs：尚未 sync
    → 现在要 sync 吗？（推荐）

你：是

AI：✓ 已将 specs 同步到 openspec/specs/ui/spec.md
    ✓ 已移动到 openspec/changes/archive/2025-01-24-add-dark-mode/

    Change 归档成功。
```

**Tips:**
- 即使 tasks 未完成，archive 也不会硬性阻止，但会给出警告
- delta specs 可以在 archive 时同步，也可以提前 sync
- 已归档的 change 会被保留，方便追溯历史
- 先运行 `/opsx:verify`，能更早发现问题

---

### `/opsx:bulk-archive`

一次归档多个已完成的 change。它会处理 change 之间的 spec 冲突。

**Syntax:**
```
/opsx:bulk-archive [change-names...]
```

**Arguments:**
| Argument | Required | Description |
|----------|----------|-------------|
| `change-names` | 否 | 指定要归档的 change；未提供时会提示选择 |

**What it does:**
- 列出所有已完成的 change
- 归档前逐个验证
- 检测多个 change 之间的 spec 冲突
- 通过检查真实实现来决定冲突如何解决
- 按时间顺序归档

**Example:**
```
你：/opsx:bulk-archive

AI：发现 3 个已完成的 change：
    - add-dark-mode（8/8 任务完成）
    - fix-login-bug（3/3 任务完成）
    - update-footer（2/2 任务完成）

    正在检查 spec 冲突...
    ⚠ add-dark-mode 和 update-footer 都修改了 specs/ui/

    正在检查代码库以解决冲突...
    两个 change 都已实现。将按时间顺序合并：
    1. add-dark-mode（创建于 1 月 20 日）
    2. update-footer（创建于 1 月 22 日）

    要归档全部 3 个 change 吗？

你：是

AI：✓ 已归档 add-dark-mode
    ✓ 已归档 fix-login-bug
    ✓ 已归档 update-footer
    Specs 合并顺序：add-dark-mode → update-footer
```

**Tips:**
- 适合并行工作流
- 冲突解决是 agentic 的，会检查代码库
- change 会按创建顺序归档
- 在覆盖 spec 内容前会先提示确认

---

### `/opsx:onboard`

通过一次引导式流程带你走完整个 OpenSpec workflow。它会直接基于你的真实代码库做交互式教程。

**Syntax:**
```
/opsx:onboard
```

**What it does:**
- 以带讲解的方式走完一整个 workflow cycle
- 扫描你的代码库，寻找真实可做的改进点
- 创建一个真实 change，并生成真实工件
- 实施一小段真实、低风险的修改
- 完成后归档这个 change
- 每一步都会解释当前在做什么

**Phases:**
1. 欢迎与代码库分析
2. 寻找一个值得改进的点
3. 创建 change（`/opsx:new`）
4. 编写 proposal
5. 创建 specs
6. 编写 design
7. 创建 tasks
8. 执行 tasks（`/opsx:apply`）
9. 验证实现
10. 归档 change
11. 总结与下一步

**Example:**
```
你：/opsx:onboard

AI：欢迎使用 OpenSpec！

    我会基于你的真实代码库，带你走一遍完整 workflow。
    我们会找一件小事来改进，为它创建正式 change，
    完成实现，然后归档。

    我先扫描一下你的代码库，看看有什么机会...

    [分析代码库]

    我找到几个可做的方向：
    1. 给 contact form 添加输入校验
    2. 改善 auth flow 里的错误提示
    3. 给异步按钮补 loading state

    你对哪个更感兴趣？或者你也可以提出别的方向。
```

**Tips:**
- 很适合第一次接触 OpenSpec 的用户
- 用的是真实代码，不是玩具示例
- 创建出的 change 可以保留，也可以丢弃
- 完整走一遍通常需要 15-30 分钟

---

## Command Syntax by AI Tool

不同 AI 工具对命令语法会有轻微差异。请选择与你所用工具一致的格式：

| Tool | Syntax Example |
|------|----------------|
| Claude Code | `/opsx:propose`、`/opsx:apply` |
| Cursor | `/opsx-propose`、`/opsx-apply` |
| Windsurf | `/opsx-propose`、`/opsx-apply` |
| Copilot (IDE) | `/opsx-propose`、`/opsx-apply` |
| Kimi CLI | 基于 skill 的调用，例如 `/skill:openspec-propose`、`/skill:openspec-apply-change`（不会生成 `opsx-*` 命令文件） |
| Trae | 基于 skill 的调用，例如 `/openspec-propose`、`/openspec-apply-change`（不会生成 `opsx-*` 命令文件） |

不同工具只是命令暴露方式不同，背后的意图是一致的。

> **Note：** GitHub Copilot 命令（`.github/prompts/*.prompt.md`）目前只在 IDE 扩展里可用（VS Code、JetBrains、Visual Studio）。GitHub Copilot CLI 目前还不支持自定义 prompt 文件。详细情况与替代方案见 [Supported Tools](supported-tools.md)。

---

## Legacy Commands

这些命令使用的是较早的 “一次做完” workflow。它们仍然可用，但更推荐使用 OPSX 命令。

| Command | What it does |
|---------|--------------|
| `/openspec:proposal` | 一次创建全部工件（proposal、specs、design、tasks） |
| `/openspec:apply` | 实现 change |
| `/openspec:archive` | 归档 change |

**When to use legacy commands：**
- 现有项目仍在沿用旧 workflow
- 改动很简单，不需要逐步创建工件
- 你就是偏好 all-or-nothing 的方式

**Migrating to OPSX：**
旧 change 仍可继续用 OPSX 命令推进，底层工件结构是兼容的。

---

## Troubleshooting

### “Change not found”

命令无法判断你要处理哪个 change。

**Solutions:**
- 显式指定 change 名称：`/opsx:apply add-dark-mode`
- 检查 change 目录是否存在：`openspec list`
- 确认你当前位于正确的项目目录

### “No artifacts ready”

所有工件要么已完成，要么仍被缺失依赖阻塞。

**Solutions:**
- 运行 `openspec status --change <name>` 查看阻塞原因
- 检查依赖工件是否存在
- 先补齐缺失的依赖工件

### “Schema not found”

指定的 schema 不存在。

**Solutions:**
- 列出可用 schema：`openspec schemas`
- 检查 schema 名称拼写
- 如果是自定义 schema，先创建它：`openspec schema init <name>`

### Commands not recognized

AI 工具无法识别 OpenSpec 命令。

**Solutions:**
- 确认 OpenSpec 已初始化：`openspec init`
- 重新生成 skills：`openspec update`
- 检查 `.claude/skills/` 目录是否存在（针对 Claude Code）
- 重启 AI 工具，让它重新加载新命令

### Artifacts not generating properly

AI 生成出的工件不完整或不正确。

**Solutions:**
- 在 `openspec/config.yaml` 中加入项目上下文
- 为具体工件添加更细的规则
- 在 change 描述里提供更多背景信息
- 若想更细粒度控制，优先用 `/opsx:continue` 而不是 `/opsx:ff`

---

## Next Steps

- [Workflows](workflows.md) - 常见模式与各命令的适用时机
- [CLI](cli.md) - 用于管理与校验的终端命令
- [Customization](customization.md) - 创建自定义 schema 与 workflows
