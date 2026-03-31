# GSD 命令参考

> 完整的命令语法、flag、选项和示例。功能细节请见 [Feature Reference](../FEATURES.md)。工作流 walkthrough 请见 [User Guide](USER-GUIDE.md)。

---

## 命令语法

- **Claude Code / Gemini / Copilot:** `/gsd:command-name [args]`
- **OpenCode:** `/gsd-command-name [args]`
- **Codex:** `$gsd-command-name [args]`

---

## 核心工作流命令

### `/gsd:new-project`

通过深度上下文收集初始化一个新项目。

| Flag | 说明 |
|------|------|
| `--auto @file.md` | 从文档中自动提取信息，跳过交互式提问 |

**前置条件：** 不存在 `.planning/PROJECT.md`
**产出：** `PROJECT.md`、`REQUIREMENTS.md`、`ROADMAP.md`、`STATE.md`、`config.json`、`research/`、`CLAUDE.md`

```bash
/gsd:new-project                    # 交互模式
/gsd:new-project --auto @prd.md     # 从 PRD 自动提取
```

---

### `/gsd:new-workspace`

创建一个隔离的 workspace，包含仓库副本和独立的 `.planning/` 目录。

| Flag | 说明 |
|------|------|
| `--name <name>` | Workspace 名称（必填） |
| `--repos repo1,repo2` | 逗号分隔的仓库路径或仓库名 |
| `--path /target` | 目标目录（默认：`~/gsd-workspaces/<name>`） |
| `--strategy worktree\|clone` | 复制策略（默认：`worktree`） |
| `--branch <name>` | 要切出的分支名（默认：`workspace/<name>`） |
| `--auto` | 跳过交互式提问 |

**适用场景：**
- 多仓协作：只在部分仓库上工作，并保持独立的 GSD 状态
- 功能隔离：`--repos .` 会为当前仓库创建一个 worktree

**产出：** `WORKSPACE.md`、`.planning/`、仓库副本（worktree 或 clone）

```bash
/gsd:new-workspace --name feature-b --repos hr-ui,ZeymoAPI
/gsd:new-workspace --name feature-b --repos . --strategy worktree  # 同仓隔离
/gsd:new-workspace --name spike --repos api,web --strategy clone   # 完整 clone
```

---

### `/gsd:list-workspaces`

列出当前活跃的 GSD workspace 及其状态。

**扫描：** `~/gsd-workspaces/` 中的 `WORKSPACE.md` manifest
**展示：** 名称、仓库数量、策略、GSD 项目状态

```bash
/gsd:list-workspaces
```

---

### `/gsd:remove-workspace`

删除一个 workspace，并清理 git worktree。

| Argument | 必需 | 说明 |
|----------|------|------|
| `<name>` | 是 | 要删除的 workspace 名称 |

**安全机制：** 如果任何仓库存在未提交变更则拒绝删除；要求确认名称。

```bash
/gsd:remove-workspace feature-b
```

---

### `/gsd:discuss-phase`

在规划前记录实现决策。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 阶段编号（默认当前阶段） |

| Flag | 说明 |
|------|------|
| `--auto` | 为所有问题自动选择推荐默认值 |
| `--batch` | 改为批量收集问题，而不是逐个提问 |
| `--analyze` | 在讨论中加入 trade-off 分析 |

**前置条件：** 存在 `.planning/ROADMAP.md`
**产出：** `{phase}-CONTEXT.md`、`{phase}-DISCUSSION-LOG.md`（审计轨迹）

```bash
/gsd:discuss-phase 1                # 阶段 1 的交互式讨论
/gsd:discuss-phase 3 --auto         # 阶段 3 自动选择默认值
/gsd:discuss-phase --batch          # 当前阶段批量模式
/gsd:discuss-phase 2 --analyze      # 带 trade-off 分析的讨论
```

---

### `/gsd:ui-phase`

为前端阶段生成 UI 设计契约。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 阶段编号（默认当前阶段） |

**前置条件：** 存在 `.planning/ROADMAP.md`，且该阶段包含前端 / UI 工作
**产出：** `{phase}-UI-SPEC.md`

```bash
/gsd:ui-phase 2                     # 为阶段 2 生成设计契约
```

---

### `/gsd:plan-phase`

对一个阶段执行研究、规划和验证。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 阶段编号（默认下一个未规划阶段） |

| Flag | 说明 |
|------|------|
| `--auto` | 跳过交互式确认 |
| `--research` | 即使已存在 `RESEARCH.md` 也强制重新调研 |
| `--skip-research` | 跳过领域研究步骤 |
| `--gaps` | 缺口修补模式（读取 `VERIFICATION.md`，跳过 research） |
| `--skip-verify` | 跳过 plan checker 验证循环 |
| `--prd <file>` | 使用 PRD 文件作为上下文，而不是 `discuss-phase` |
| `--reviews` | 结合 `REVIEWS.md` 中的跨 AI 评审反馈重新规划 |

**前置条件：** 存在 `.planning/ROADMAP.md`
**产出：** `{phase}-RESEARCH.md`、`{phase}-{N}-PLAN.md`、`{phase}-VALIDATION.md`

```bash
/gsd:plan-phase 1                   # 阶段 1：研究 + 规划 + 验证
/gsd:plan-phase 3 --skip-research   # 不做 research 直接规划（熟悉领域）
/gsd:plan-phase --auto              # 非交互式规划
```

---

### `/gsd:execute-phase`

使用基于 wave 的并行化执行某个阶段的全部计划，或只执行某个 wave。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | **是** | 要执行的阶段编号 |
| `--wave N` | 否 | 只执行该阶段中的第 `N` 个 Wave |

**前置条件：** 该阶段存在 PLAN.md 文件
**产出：** 每个计划对应的 `{phase}-{N}-SUMMARY.md`、git commit，以及整个阶段完成后生成的 `{phase}-VERIFICATION.md`

```bash
/gsd:execute-phase 1                # 执行阶段 1
/gsd:execute-phase 1 --wave 2       # 只执行 Wave 2
```

---

### `/gsd:verify-work`

带自动诊断的用户验收测试。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 阶段编号（默认最近一次执行的阶段） |

**前置条件：** 该阶段已执行
**产出：** `{phase}-UAT.md`，若发现问题则生成修复计划

```bash
/gsd:verify-work 1                  # 阶段 1 的 UAT
```

---

### `/gsd:next`

自动推进到下一个合理的工作流步骤。读取项目状态并运行合适的命令。

**前置条件：** 存在 `.planning/` 目录
**行为：**
- 没有项目 → 建议运行 `/gsd:new-project`
- 阶段需要讨论 → 运行 `/gsd:discuss-phase`
- 阶段需要规划 → 运行 `/gsd:plan-phase`
- 阶段需要执行 → 运行 `/gsd:execute-phase`
- 阶段需要验证 → 运行 `/gsd:verify-work`
- 所有阶段完成 → 建议运行 `/gsd:complete-milestone`

```bash
/gsd:next                           # 自动识别并执行下一步
```

---

### `/gsd:session-report`

生成会话报告，包含工作摘要、结果和估算资源消耗。

**前置条件：** 活跃项目且最近有工作记录
**产出：** `.planning/reports/SESSION_REPORT.md`

```bash
/gsd:session-report                 # 生成会话后总结
```

**报告包含：**
- 已执行的工作（commit、计划、阶段推进）
- 结果与交付物
- 阻塞项与已做决策
- 估算 token / 成本使用情况
- 下一步建议

---

### `/gsd:ship`

从已完成阶段的工作创建 PR，并自动生成 PR body。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 阶段编号或 milestone 版本（例如 `4` 或 `v1.0`） |
| `--draft` | 否 | 创建为 draft PR |

**前置条件：** 阶段已验证通过（`/gsd:verify-work` 通过），已安装并登录 `gh` CLI
**产出：** 带丰富描述的 GitHub PR，以及更新后的 `STATE.md`

```bash
/gsd:ship 4                         # 发布阶段 4
/gsd:ship 4 --draft                 # 以 draft PR 形式发布
```

**PR body 包含：**
- 来自 `ROADMAP.md` 的阶段目标
- 来自 `SUMMARY.md` 文件的变更摘要
- 已覆盖的需求（REQ-ID）
- 验证状态
- 关键决策

---

### `/gsd:ui-review`

对已实现前端进行回溯式的 6 支柱视觉审计。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 阶段编号（默认最近一次执行的阶段） |

**前置条件：** 项目包含前端代码（可独立运行，不需要 GSD 项目）
**产出：** `{phase}-UI-REVIEW.md`，以及 `.planning/ui-reviews/` 下的截图

```bash
/gsd:ui-review                      # 审计当前阶段
/gsd:ui-review 3                    # 审计阶段 3
```

---

### `/gsd:audit-uat`

跨阶段审计所有未关闭的 UAT 和验证项。

**前置条件：** 至少一个阶段已经执行并产生过 UAT 或 verification
**产出：** 带人工测试计划的分类审计报告

```bash
/gsd:audit-uat
```

---

### `/gsd:audit-milestone`

验证某个 milestone 是否达到其完成定义。

**前置条件：** 所有阶段已执行
**产出：** 带 gap 分析的审计报告

```bash
/gsd:audit-milestone
```

---

### `/gsd:complete-milestone`

归档 milestone，并打 release tag。

**前置条件：** milestone 审计已完成（推荐）
**产出：** `MILESTONES.md` 条目、git tag

```bash
/gsd:complete-milestone
```

---

### `/gsd:milestone-summary`

从 milestone 产物中生成项目综合摘要，用于团队 onboarding 和审阅。

| Argument | 必需 | 说明 |
|----------|------|------|
| `version` | 否 | Milestone 版本（默认当前 / 最新 milestone） |

**前置条件：** 至少存在一个已完成或进行中的 milestone
**产出：** `.planning/reports/MILESTONE_SUMMARY-v{version}.md`

**摘要包含：**
- 概览、架构决策、按阶段拆解
- 关键决策与 trade-off
- 需求覆盖情况
- 技术债与延期项
- 给新团队成员的快速上手指南
- 生成后可继续进行交互式问答

```bash
/gsd:milestone-summary                # 汇总当前 milestone
/gsd:milestone-summary v1.0           # 汇总指定 milestone
```

---

### `/gsd:new-milestone`

开启下一个版本周期。

| Argument | 必需 | 说明 |
|----------|------|------|
| `name` | 否 | Milestone 名称 |
| `--reset-phase-numbers` | 否 | 新 milestone 从 Phase 1 重新开始，并在重新做 roadmap 前归档旧阶段目录 |

**前置条件：** 上一个 milestone 已完成
**产出：** 更新后的 `PROJECT.md`、新的 `REQUIREMENTS.md`、新的 `ROADMAP.md`

```bash
/gsd:new-milestone                  # 交互模式
/gsd:new-milestone "v2.0 Mobile"    # 指定 milestone 名称
/gsd:new-milestone --reset-phase-numbers "v2.0 Mobile"  # 阶段编号重置为 1
```

---

## 阶段管理命令

### `/gsd:add-phase`

向 roadmap 末尾追加一个新阶段。

```bash
/gsd:add-phase                      # 交互模式，描述这个阶段
```

### `/gsd:insert-phase`

使用小数编号在两个阶段之间插入紧急工作。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 插入到该阶段之后 |

```bash
/gsd:insert-phase 3                 # 插入在 phase 3 和 4 之间 -> 创建 3.1
```

### `/gsd:remove-phase`

移除未来阶段，并重新编号后续阶段。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 要移除的阶段编号 |

```bash
/gsd:remove-phase 7                 # 删除 phase 7，并将 8→7、9→8 等
```

### `/gsd:list-phase-assumptions`

在规划前预览 Claude 打算采用的实现方式。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 阶段编号 |

```bash
/gsd:list-phase-assumptions 2       # 查看阶段 2 的假设
```

### `/gsd:plan-milestone-gaps`

为 milestone 审计发现的缺口创建新阶段。

```bash
/gsd:plan-milestone-gaps             # 为每个审计缺口创建 phase
```

### `/gsd:research-phase`

只执行深度生态调研（独立模式，通常更推荐直接使用 `/gsd:plan-phase`）。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 阶段编号 |

```bash
/gsd:research-phase 4               # 调研阶段 4 所属领域
```

### `/gsd:validate-phase`

回溯式审计并补齐 Nyquist 验证缺口。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 阶段编号 |

```bash
/gsd:validate-phase 2               # 审计阶段 2 的测试覆盖
```

---

## 导航命令

### `/gsd:progress`

显示当前状态和下一步。

```bash
/gsd:progress                       # “我现在在哪？下一步是什么？”
```

### `/gsd:resume-work`

从上一个会话恢复完整上下文。

```bash
/gsd:resume-work                    # 上下文重置或新会话后恢复
```

### `/gsd:pause-work`

在阶段中途停止时保存交接上下文。

```bash
/gsd:pause-work                     # 创建 continue-here.md
```

### `/gsd:manager`

用于在一个终端里管理多个阶段的交互式命令中心。

**前置条件：** 存在 `.planning/ROADMAP.md`
**行为：**
- 以 dashboard 形式展示所有阶段及其可视化状态
- 基于依赖和进度推荐最佳下一步动作
- 调度工作：discuss 内联运行，plan / execute 以后台 agent 运行
- 面向需要跨多个阶段并行推进工作的重度用户

```bash
/gsd:manager                        # 打开命令中心 dashboard
```

---

### `/gsd:help`

显示所有命令及其使用说明。

```bash
/gsd:help                           # 快速参考
```

---

## 工具型命令

### `/gsd:quick`

以 GSD 保障机制执行一个临时任务。

| Flag | 说明 |
|------|------|
| `--full` | 启用 plan checking（2 次迭代）和执行后验证 |
| `--discuss` | 轻量级的规划前讨论 |
| `--research` | 在规划前拉起一个聚焦 researcher |

这些 flag 可以组合使用。

```bash
/gsd:quick                          # 基础 quick 任务
/gsd:quick --discuss --research     # 讨论 + 调研 + 规划
/gsd:quick --full                   # 带 plan checking 和验证
/gsd:quick --discuss --research --full  # 启用全部可选阶段
```

### `/gsd:autonomous`

自主运行所有剩余阶段。

| Flag | 说明 |
|------|------|
| `--from N` | 从指定阶段开始 |

```bash
/gsd:autonomous                     # 运行所有剩余阶段
/gsd:autonomous --from 3            # 从阶段 3 开始
```

### `/gsd:do`

将自由文本路由到合适的 GSD 命令。

```bash
/gsd:do                             # 然后描述你想做什么
```

### `/gsd:note`

零摩擦记录想法：追加、列出或将 note 提升为 todo。

| Argument | 必需 | 说明 |
|----------|------|------|
| `text` | 否 | 要记录的 note 文本（默认追加模式） |
| `list` | 否 | 列出项目级和全局范围的所有 note |
| `promote N` | 否 | 将第 N 条 note 转成结构化 todo |

| Flag | 说明 |
|------|------|
| `--global` | 对 note 操作使用全局范围 |

```bash
/gsd:note "Consider caching strategy for API responses"
/gsd:note list
/gsd:note promote 3
```

### `/gsd:debug`

带持久化状态的系统化调试。

| Argument | 必需 | 说明 |
|----------|------|------|
| `description` | 否 | bug 描述 |

```bash
/gsd:debug "Login button not responding on mobile Safari"
```

### `/gsd:add-todo`

记录一个想法或任务，留待后续处理。

| Argument | 必需 | 说明 |
|----------|------|------|
| `description` | 否 | todo 描述 |

```bash
/gsd:add-todo "Consider adding dark mode support"
```

### `/gsd:check-todos`

列出待处理 todo，并选择其中一个继续做。

```bash
/gsd:check-todos
```

### `/gsd:add-tests`

为一个已完成阶段生成测试。

| Argument | 必需 | 说明 |
|----------|------|------|
| `N` | 否 | 阶段编号 |

```bash
/gsd:add-tests 2                    # 为阶段 2 生成测试
```

### `/gsd:stats`

显示项目统计信息。

```bash
/gsd:stats                          # 项目指标 dashboard
```

### `/gsd:profile-user`

基于 Claude Code 会话分析，从 8 个行为维度生成人类开发者画像（沟通风格、决策模式、调试方式、UX 偏好、厂商选择、挫败触发点、学习方式、解释深度）。产出的结果会用于个性化 Claude 的响应。

| Flag | 说明 |
|------|------|
| `--questionnaire` | 使用交互式问卷，而不是会话分析 |
| `--refresh` | 重新分析会话并重新生成 profile |

**生成产物：**
- `USER-PROFILE.md`：完整行为画像
- `/gsd:dev-preferences` 命令：在任意会话中加载偏好
- `CLAUDE.md` 的 profile 区块：由 Claude Code 自动发现

```bash
/gsd:profile-user                   # 分析会话并生成 profile
/gsd:profile-user --questionnaire   # 交互式问卷兜底
/gsd:profile-user --refresh         # 基于最新会话重新生成
```

### `/gsd:health`

校验 `.planning/` 目录完整性。

| Flag | 说明 |
|------|------|
| `--repair` | 自动修复可恢复问题 |

```bash
/gsd:health                         # 检查完整性
/gsd:health --repair                # 检查并修复
```

### `/gsd:cleanup`

归档已完成 milestone 累积下来的阶段目录。

```bash
/gsd:cleanup
```

---

## 诊断命令

### `/gsd:forensics`

对失败或卡住的 GSD 工作流进行事后取证调查。

| Argument | 必需 | 说明 |
|----------|------|------|
| `description` | 否 | 问题描述（省略时会提示输入） |

**前置条件：** 存在 `.planning/` 目录
**产出：** `.planning/forensics/report-{timestamp}.md`

**调查内容包括：**
- Git 历史分析（最近 commit、卡住模式、时间断层）
- 产物完整性（已完成阶段应有文件是否存在）
- `STATE.md` 异常和会话历史
- 未提交工作、冲突、被遗弃的改动
- 至少检查 4 类异常（卡死循环、产物缺失、工作被遗弃、崩溃 / 中断）
- 如果发现可执行结论，可继续创建 GitHub issue

```bash
/gsd:forensics                              # 交互模式，先描述问题
/gsd:forensics "Phase 3 execution stalled"  # 直接附带问题描述
```

---

## Workstream 管理

### `/gsd:workstreams`

管理并行 workstream，以便在不同 milestone 领域上并发工作。

**子命令：**

| Subcommand | 说明 |
|------------|------|
| `list` | 列出所有 workstream 及其状态（未指定子命令时默认） |
| `create <name>` | 创建新的 workstream |
| `status <name>` | 查看单个 workstream 的详细状态 |
| `switch <name>` | 设置当前活跃 workstream |
| `progress` | 查看所有 workstream 的进度摘要 |
| `complete <name>` | 归档一个已完成的 workstream |
| `resume <name>` | 恢复某个 workstream 的工作 |

**前置条件：** 存在活跃的 GSD 项目
**产出：** `.planning/` 下的 workstream 目录，以及每个 workstream 的状态跟踪

```bash
/gsd:workstreams                    # 列出所有 workstream
/gsd:workstreams create backend-api # 创建新的 workstream
/gsd:workstreams switch backend-api # 设置活跃 workstream
/gsd:workstreams status backend-api # 查看详细状态
/gsd:workstreams progress           # 跨 workstream 进度概览
/gsd:workstreams complete backend-api  # 归档已完成 workstream
/gsd:workstreams resume backend-api    # 恢复该 workstream
```

---

## 配置命令

### `/gsd:settings`

交互式配置工作流开关和模型 profile。

```bash
/gsd:settings                       # 交互式配置
```

### `/gsd:set-profile`

快速切换 profile。

| Argument | 必需 | 说明 |
|----------|------|------|
| `profile` | **是** | `quality`、`balanced`、`budget` 或 `inherit` |

```bash
/gsd:set-profile budget             # 切到 budget profile
/gsd:set-profile quality            # 切到 quality profile
```

---

## 存量项目命令

### `/gsd:map-codebase`

通过并行 mapper agent 分析现有代码库。

| Argument | 必需 | 说明 |
|----------|------|------|
| `area` | 否 | 将分析范围限定到某个区域 |

```bash
/gsd:map-codebase                   # 全量代码库分析
/gsd:map-codebase auth              # 聚焦 auth 区域
```

---

## 更新命令

### `/gsd:update`

带 changelog 预览地更新 GSD。

```bash
/gsd:update                         # 检查更新并安装
```

### `/gsd:reapply-patches`

在 GSD 更新后恢复本地修改。

```bash
/gsd:reapply-patches                # 合并回本地改动
```

---

## 快速与内联命令

### `/gsd:fast`

以内联方式执行一个琐碎任务，不拉起 subagent，也没有规划开销。适用于修 typo、改配置、小型重构、补漏掉的 commit。

| Argument | 必需 | 说明 |
|----------|------|------|
| `task description` | 否 | 要做什么（省略时会提示输入） |

**它不是 `/gsd:quick` 的替代品**。凡是需要 research、多步骤规划或验证的任务，都应使用 `/gsd:quick`。

```bash
/gsd:fast "fix typo in README"
/gsd:fast "add .env to gitignore"
```

---

## 代码质量命令

### `/gsd:review`

调用外部 AI CLI 对阶段计划做跨 AI 同行评审。

| Argument | 必需 | 说明 |
|----------|------|------|
| `--phase N` | **是** | 要评审的阶段编号 |

| Flag | 说明 |
|------|------|
| `--gemini` | 纳入 Gemini CLI 评审 |
| `--claude` | 纳入 Claude CLI 评审（独立会话） |
| `--codex` | 纳入 Codex CLI 评审 |
| `--all` | 纳入所有可用 CLI |

**产出：** `{phase}-REVIEWS.md`，可由 `/gsd:plan-phase --reviews` 消费

```bash
/gsd:review --phase 3 --all
/gsd:review --phase 2 --gemini
```

---

### `/gsd:pr-branch`

通过过滤 `.planning/` 相关 commit 来生成一个干净的 PR 分支。

| Argument | 必需 | 说明 |
|----------|------|------|
| `target branch` | 否 | 基准分支（默认：`main`） |

**用途：** 让 reviewer 只看到代码变更，而不是 GSD 规划产物。

```bash
/gsd:pr-branch                     # 相对 main 过滤
/gsd:pr-branch develop             # 相对 develop 过滤
```

---

### `/gsd:audit-uat`

跨阶段审计所有未完成的 UAT 与验证项。

**前置条件：** 至少一个阶段已经执行并产生过 UAT 或 verification
**产出：** 带人工测试计划的分类审计报告

```bash
/gsd:audit-uat
```

---

## Backlog 与 Thread 命令

### `/gsd:add-backlog`

使用 999.x 编号把一个想法放进 backlog 停车场。

| Argument | 必需 | 说明 |
|----------|------|------|
| `description` | **是** | backlog 项描述 |

**999.x 编号** 会让 backlog 项始终位于活跃阶段序列之外。系统会立刻创建 phase 目录，因此 `/gsd:discuss-phase` 和 `/gsd:plan-phase` 可以直接在这些项上工作。

```bash
/gsd:add-backlog "GraphQL API layer"
/gsd:add-backlog "Mobile responsive redesign"
```

---

### `/gsd:review-backlog`

审查 backlog 项，并将其提升到活跃 milestone。

**每个条目的操作：** Promote（移动到活跃序列）、Keep（保留在 backlog）、Remove（删除）。

```bash
/gsd:review-backlog
```

---

### `/gsd:plant-seed`

记录一个面向未来的想法，并附带触发条件，让它在合适的 milestone 自动浮现。

| Argument | 必需 | 说明 |
|----------|------|------|
| `idea summary` | 否 | seed 描述（省略时会提示输入） |

Seed 用来解决 context rot：与其把一句没人会看的备注塞进 Deferred，不如用 seed 保留完整的 WHY、何时浮现，以及通往细节的 breadcrumbs。

**产出：** `.planning/seeds/SEED-NNN-slug.md`
**消费方：** `/gsd:new-milestone`（扫描 seed 并展示匹配项）

```bash
/gsd:plant-seed "Add real-time collaboration when WebSocket infra is in place"
```

---

### `/gsd:thread`

管理跨会话工作的持久上下文 thread。

| Argument | 必需 | 说明 |
|----------|------|------|
| (none) | — | 列出所有 thread |
| `name` | — | 按名称恢复已有 thread |
| `description` | — | 创建新 thread |

Thread 是轻量级的跨会话知识存储，适用于跨多个会话、但又不属于某个具体 phase 的工作。它比 `/gsd:pause-work` 更轻量。

```bash
/gsd:thread                         # 列出所有 thread
/gsd:thread fix-deploy-key-auth     # 恢复 thread
/gsd:thread "Investigate TCP timeout in pasta service"  # 新建
```

---

## 社区命令

### `/gsd:join-discord`

打开 Discord 社区邀请链接。

```bash
/gsd:join-discord
```
