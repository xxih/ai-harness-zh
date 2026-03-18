---
name: writing-plans
description: 当你已经有 spec 或需求，并且要在动代码前把多步骤任务写成实现计划时使用
---

# 编写计划

## 概览

编写完整的实现计划，并假设执行该计划的工程师对当前代码库几乎没有上下文，而且审美也未必可靠。把他们需要知道的一切都写清楚：每个任务要改哪些文件、相关代码、要看的测试和文档、以及如何验证。把整个实现拆成细粒度任务。坚持 DRY、YAGNI、TDD，并频繁 commit。

默认假设对方是熟练开发者，但对你的工具链和业务背景几乎不了解；同时也假设他们不太擅长测试设计。

**开始时要明确说明：**“我正在使用 writing-plans skill 来编写实现计划。”

**上下文要求：**这个 skill 应该在专用 worktree 中运行（由 `brainstorming` skill 创建）。

**计划保存路径：**`docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`
- 如果用户明确指定了其他计划目录，以用户偏好为准。

## 范围检查

如果 spec 覆盖了多个相互独立的子系统，那么这件事本应在 brainstorming 阶段就拆成多个子项目 spec。若没有拆开，你应建议把它分成多份计划——每个子系统一份。每份计划都必须能独立产出可运行、可测试的软件。

## 文件结构

在定义任务之前，先画清楚要创建或修改哪些文件，以及每个文件分别负责什么。这一步会锁定你的拆分决策。

- 设计边界清晰、接口明确的单元。每个文件应只有一个核心职责。
- 你更容易在脑中同时 hold 住较小的代码单元，编辑也更可靠。因此优先选择更小、更聚焦的文件，而不是臃肿的大文件。
- 经常一起变化的内容应该放在一起。按职责拆，不要机械按技术层拆。
- 在现有代码库里要遵循既有模式。如果代码库本来就偏向大文件，不要单方面大改结构；但如果你正在修改的文件已经失控，把拆分写进计划是合理的。

这些结构设计会直接影响任务拆分。每个任务都应该形成一组能独立成立的自洽变更。

## 小步任务粒度

**每一步都应该只是一件动作（2-5 分钟）：**
- “写一个失败测试” —— 一步
- “运行它并确认失败” —— 一步
- “写最小实现让测试通过” —— 一步
- “再次运行测试并确认通过” —— 一步
- “commit” —— 一步

## 计划文档头部

**每一份计划都必须以这个头部开场：**

```markdown
# [Feature Name] Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

## 任务结构

````markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

- [ ] **Step 1: Write the failing test**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

- [ ] **Step 3: Write minimal implementation**

```python
def function(input):
    return expected
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```
````

## 记住
- 永远写精确文件路径
- 计划里要给出完整代码，不要只写“加校验”这种空话
- 命令要精确，并写明预期输出
- 用 `@` 语法引用相关 skills
- 坚持 DRY、YAGNI、TDD 和频繁 commit

## 计划评审循环

写完整份计划后：

1. 派发一个 `plan-document-reviewer` subagent（见 `plan-document-reviewer-prompt.md`），并且只给它精心构造的评审上下文——不要给你的会话历史。这样 reviewer 会专注审计划本身，而不是你的思路。
   - 提供：计划文档路径、spec 文档路径
2. 如果返回 ❌ Issues Found：修复后，把**整份计划**重新派发评审
3. 如果返回 ✅ Approved：再进入执行交接

**评审循环指导：**
- 修计划的应当还是最初写计划的那个 agent（这样能保留上下文）
- 如果循环超过 3 次，升级给人类协作者请求指导
- reviewer 的反馈是 advisory，不是绝对命令；如果你认为它错了，要解释理由

## 执行交接

计划保存后，给用户两个执行选项：

**“计划已完成，并保存到 `docs/superpowers/plans/<filename>.md`。有两种执行方式：**

**1. Subagent-Driven（推荐）** —— 每个任务派发一个全新 subagent，任务间做 review，迭代更快

**2. Inline Execution** —— 在当前会话里用 executing-plans 执行，按批次推进并设置检查点

**你想选哪一种？”**

**如果用户选择 Subagent-Driven：**
- **必需子 skill：**使用 `superpowers:subagent-driven-development`
- 每个任务一个全新 subagent + 双阶段 review

**如果用户选择 Inline Execution：**
- **必需子 skill：**使用 `superpowers:executing-plans`
- 按批次执行，并设置 review 检查点
