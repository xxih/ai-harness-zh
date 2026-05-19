# Workflows

本指南介绍 OpenSpec 的常见 workflow 模式，以及各自适用的场景。基础安装与初始化请见 [Getting Started](getting-started.md)，命令参考请见 [Commands](commands.md)。

## 理念：动作，而不是阶段

传统 workflow 会强制你按阶段推进：先规划，再实现，然后结束。但真实工作并不会这么整齐。

OPSX 采用了不同的方式：

```text
传统方式（锁死阶段）：

  PLANNING ────────► IMPLEMENTING ────────► DONE
      │                    │
      │   “不能回头”       │
      └────────────────────┘

OPSX（流动动作）：

  proposal ──► specs ──► design ──► tasks ──► implement
```

**核心原则：**

- **Actions, not phases**：命令表示“你现在可以做什么”，而不是“你被卡在哪个阶段”
- **Dependencies are enablers**：依赖只说明“哪些事情已经可做”，不是规定你下一步必须做什么

> **Customization：** OPSX workflow 由 schema 驱动，schema 会定义工件顺序。详细说明见 [Customization](customization.md)。

## Two Modes

### Default Quick Path (`core` profile)

新安装默认使用 `core`，提供以下命令：
- `/opsx:propose`
- `/opsx:explore`
- `/opsx:apply`
- `/opsx:sync`
- `/opsx:archive`

典型流程：

```text
/opsx:propose ──► /opsx:apply ──► /opsx:sync ──► /opsx:archive
```

### Expanded/Full Workflow（自定义选择）

如果你想启用显式的 scaffold-and-build 命令（`/opsx:new`、`/opsx:continue`、`/opsx:ff`、`/opsx:verify`、`/opsx:bulk-archive`、`/opsx:onboard`），可以通过下面的方式开启：

```bash
openspec config profile
openspec update
```

## Workflow Patterns（Expanded Mode）

### Quick Feature

当你已经明确知道要做什么，只需要执行时：

```text
/opsx:new ──► /opsx:ff ──► /opsx:apply ──► /opsx:verify ──► /opsx:archive
```

**示例对话：**

```text
你：/opsx:new add-logout-button

AI：已创建 openspec/changes/add-logout-button/
    已准备创建：proposal

你：/opsx:ff

AI：正在创建全部规划工件...
    ✓ proposal.md
    ✓ specs/
    ✓ design.md
    ✓ tasks.md
    已准备进入实现！

你：/opsx:apply

AI：正在执行任务...
    ✓ 在 header 中添加 logout 按钮
    ✓ 实现 session 清理
    ✓ 添加确认对话框
    所有任务完成！

你：/opsx:archive

AI：✓ 已合并 specs
    ✓ 已归档 change
```

**最适合：** 小到中型功能、bug 修复、直接明确的改动。

### Exploratory

当需求还不清晰，或者你需要先做调查时：

```text
/opsx:explore ──► /opsx:new ──► /opsx:continue ──► ... ──► /opsx:apply
```

**示例对话：**

```text
你：/opsx:explore

AI：你想探索什么？

你：我想提升页面加载性能，但还不确定瓶颈在哪里。

AI：我来帮你调查一下...
    [分析 bundle 大小、识别慢查询、审查组件渲染模式]

    我发现三个主要瓶颈：
    1. 体积过大的未优化图片
    2. ProductList 里的同步数据获取
    3. context 变更导致的重复渲染

    你想先处理哪一个？

你：先解决数据获取问题。

你：/opsx:new optimize-product-list-fetching

AI：已创建 change。已准备创建：proposal

你：/opsx:continue

AI：根据刚才的探索结果创建 proposal...
    [将调查结论写入 proposal]

    接下来可创建：specs、design
    你想先创建哪一个？

你：/opsx:continue

AI：正在创建 specs...
```

**最适合：** 性能优化、排障、架构决策、需求尚不清晰的任务。

### Parallel Changes

同时处理多个 change：

```text
Change A: /opsx:new ──► /opsx:ff ──► /opsx:apply（进行中）
                                         │
                                    切换上下文
                                         │
Change B: /opsx:new ──► /opsx:ff ──────► /opsx:apply
```

**示例对话：**

```text
你：我在做 add-dark-mode，但被临时拉去修一个 bug

你：/opsx:new fix-login-redirect

AI：已创建 openspec/changes/fix-login-redirect/

你：/opsx:ff

AI：✓ 已创建规划工件

你：/opsx:apply

AI：正在处理 fix-login-redirect...
    [实现修复]
    所有任务完成！

你：/opsx:archive

AI：✓ 已归档 fix-login-redirect

你：回到 dark mode

你：/opsx:apply add-dark-mode

AI：继续处理 add-dark-mode...
    从任务 2.3 开始：更新 Header...
```

**最适合：** 并行工作流、被紧急事项打断、团队协作。

当你有多个已完成 change 时，可以使用 `/opsx:bulk-archive`：

```text
你：/opsx:bulk-archive

AI：发现 3 个已完成的 change：
    - add-dark-mode（所有任务已完成）
    - fix-login-redirect（所有任务已完成）
    - update-footer（所有任务已完成）

    正在检查 spec 冲突...
    ⚠ add-dark-mode 和 update-footer 都修改了 specs/ui/

    正在检查代码库以解决冲突...
    两个 change 都已实现。将按时间顺序应用：

    Archive 全部 3 个 change 吗？

你：是

AI：✓ 已归档 add-dark-mode
    ✓ 已归档 fix-login-redirect
    ✓ 已归档 update-footer
    Specs 合并顺序：add-dark-mode → update-footer
```

`bulk archive` 会在多个 change 触及同一份 spec 时检测冲突，并通过检查真实实现来决定合并顺序。

### Completing a Change

推荐的收尾流程：

```text
/opsx:apply ──► /opsx:verify ──► /opsx:archive
                    │                 │
                 验证实现          如有需要会提示
                 是否匹配工件      先 sync specs
```

#### Verify：检查你的工作

`/opsx:verify` 会从三个维度验证实现是否与工件一致：

```text
你：/opsx:verify

AI：正在验证 add-auth...

    COMPLETENESS
    ✓ tasks.md 中 12 个任务全部勾选
    ✓ specs 中所有 requirement 都能在代码里找到对应实现
    ⚠ “Session timeout after inactivity” 场景没有测试覆盖

    CORRECTNESS
    ✓ 实现符合 spec 意图
    ✓ 场景里的边界条件已处理
    ✓ 错误状态与 spec 定义一致

    COHERENCE
    ✓ 设计决策已反映在代码结构中
    ✓ 命名与 design.md 保持一致
    ⚠ design 提到 “event-driven”，但实现使用 polling

    SUMMARY
    ─────────────────────────────
    Critical issues: 0
    Warnings: 2
    Ready to archive: Yes (with warnings)

    Recommendations:
    1. 为 session timeout 场景补一条测试
    2. 评估是否按 design 改回 event-driven，或更新 design.md
```

**What verify checks：**

| Dimension | What it validates |
|-----------|------------------|
| Completeness | 所有任务完成、所有 requirement 已实现、场景有覆盖 |
| Correctness | 实现符合 spec 意图，边界情况已处理 |
| Coherence | 设计决策体现在代码中，模式保持一致 |

`verify` 不会阻止归档，但会提前暴露你可能想先处理的问题。

#### Archive：完成并收尾

`/opsx:archive` 会完成 change 并将其移入归档目录：

```text
你：/opsx:archive

AI：正在归档 add-auth...

    Artifact status:
    ✓ proposal.md 已存在
    ✓ specs/ 已存在
    ✓ design.md 已存在
    ✓ tasks.md 已存在（12/12 任务已完成）

    Delta specs：尚未同步到 main
    → 现在要 sync 吗？

你：是

AI：✓ 已同步 specs 到 openspec/specs/auth/spec.md
    ✓ 已移动到 openspec/changes/archive/2025-01-24-add-auth/

    Change 已成功归档。
```

如果 specs 还没 sync，archive 会主动提示。它不会因为 tasks 未完成而硬性阻塞，但会给出警告。

## When to Use What

### `/opsx:ff` vs `/opsx:continue`

| Situation | Use |
|-----------|-----|
| 需求清晰，已经准备好实现 | `/opsx:ff` |
| 还在探索，想逐步审阅每一步 | `/opsx:continue` |
| 想先迭代 proposal 再写 specs | `/opsx:continue` |
| 时间紧，需要快速推进 | `/opsx:ff` |
| 改动复杂，想保留控制感 | `/opsx:continue` |

**经验法则：** 如果你一开始就能完整描述范围，用 `/opsx:ff`；如果你是边做边搞清楚，用 `/opsx:continue`。

### 什么时候更新，什么时候新开 change

一个常见问题是：什么时候继续更新现有 change 没问题，什么时候应该新开一个？

**在以下情况更新现有 change：**

- 意图相同，只是执行方式更精细
- 范围收窄（先做 MVP，剩下以后再补）
- 因认知加深而做修正（代码库和你原先预想不一样）
- 实现过程中发现需要微调设计

**在以下情况新开 change：**

- 意图已经根本变化
- 范围膨胀成另一件事
- 原始 change 本身已经可以独立标记为 “done”
- 再往原 change 里打补丁只会更混乱

```text
                     ┌─────────────────────────────────────┐
                     │     Is this the same work?          │
                     └──────────────┬──────────────────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
          Same intent?      >50% overlap?      Can original
          Same problem?     Same scope?        be "done" without
                 │                  │          these changes?
                 │                  │                  │
       ┌────────┴────────┐  ┌──────┴──────┐   ┌───────┴───────┐
       │                 │  │             │   │               │
      YES               NO YES           NO  NO              YES
       │                 │  │             │   │               │
       ▼                 ▼  ▼             ▼   ▼               ▼
    UPDATE            NEW  UPDATE       NEW  UPDATE          NEW
```

**示例：“Add dark mode”**

- “还想顺便支持自定义主题” → 新开 change（范围已经膨胀）
- “System preference detection 比预想更难” → 更新原 change（意图没变）
- “先发 toggle，preference 以后再做” → 先更新并归档，再新开后续 change

## Best Practices

### 让 change 保持聚焦

一个 change 最好只承载一个逻辑上完整的工作单元。如果你在做 “新增功能 X，顺便重构 Y”，通常应该拆成两个 change。

**为什么重要：**
- 更容易审阅和理解
- 归档历史更清晰
- 可以独立发布
- 出问题时更容易回滚

### 在需求不清楚时优先用 `/opsx:explore`

在正式创建 change 之前，先探索问题空间：

```text
你：/opsx:explore

AI：你想探索什么？

你：我们的 API 应该怎么做 rate limiting？

AI：我来先看你的现状和可选方案...
    [研究代码库与已有模式]

    我看到三种主要方式：
    1. 基于 middleware（简单，按 endpoint 生效）
    2. 基于 Redis（可扩展，共享状态）
    3. 每个用户独立 token bucket（更公平，但更复杂）

    从你现在的栈来看，#1 或 #2 更合适。你的规模大概是什么级别？
```

探索能在你创建工件之前，先把思路理清楚。

### 归档前先 Verify

用 `/opsx:verify` 检查实现是否与工件一致：

```text
你：/opsx:verify

AI：正在验证 add-dark-mode...

    ✓ tasks.md 中所有任务都已勾选
    ✓ specs 中的 requirement 都有对应代码
    ✓ design 决策已反映到实现里

    Ready to archive!
```

这样可以在收尾前先发现偏差。

### 给 change 起清晰的名字

好名字会让 `openspec list` 真正有用：

```text
Good:                          Avoid:
add-dark-mode                  feature-1
fix-login-redirect             update
optimize-product-query         changes
implement-2fa                  wip
```

## Command Quick Reference

完整命令详情与选项见 [Commands](commands.md)。

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/opsx:propose` | 创建 change + 规划工件 | 默认快速路径（`core` profile） |
| `/opsx:explore` | 探索想法 | 需求不清晰、需要调查时 |
| `/opsx:new` | 创建 change scaffold | Expanded mode，需要显式控制工件 |
| `/opsx:continue` | 创建下一个工件 | Expanded mode，逐步生成工件 |
| `/opsx:ff` | 一次性创建全部规划工件 | Expanded mode，范围清晰时 |
| `/opsx:apply` | 实现 tasks | 已准备写代码时 |
| `/opsx:verify` | 验证实现 | Expanded mode，归档前 |
| `/opsx:sync` | 合并 delta specs | Expanded mode，可选 |
| `/opsx:archive` | 完成并归档 change | 所有工作完成后 |
| `/opsx:bulk-archive` | 一次归档多个 change | Expanded mode，并行工作时 |

## Next Steps

- [Commands](commands.md) - 所有 slash command 的完整参考
- [Concepts](concepts.md) - 深入理解 specs、artifacts 与 schemas
- [Customization](customization.md) - 创建自定义 workflows
