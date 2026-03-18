---
name: using-git-worktrees
description: 当你开始需要隔离工作区的功能开发，或准备执行实现计划时使用；它会创建隔离的 git worktree，并带上目录选择和安全校验
---

# 使用 Git Worktrees

## 概览

Git worktree 允许你在共享同一个仓库对象库的前提下，同时拥有多个独立工作区，而不必来回切 branch。

**核心原则：**系统化地选择目录 + 做安全校验 = 可靠的隔离环境。

**开始时要明确说明：**“我正在使用 using-git-worktrees skill 来建立隔离工作区。”

## 目录选择流程

按下面优先级执行：

### 1. 检查现有目录

```bash
# Check in priority order
ls -d .worktrees 2>/dev/null     # Preferred (hidden)
ls -d worktrees 2>/dev/null      # Alternative
```

**如果存在：**就用它。如果两个都存在，优先 `.worktrees`。

### 2. 检查 CLAUDE.md

```bash
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
```

**如果里面写了偏好：**直接按它来，不需要再问。

### 3. 问用户

如果既没有现有目录，也没有 CLAUDE.md 偏好，就问：

```
No worktree directory found. Where should I create worktrees?

1. .worktrees/ (project-local, hidden)
2. ~/.config/superpowers/worktrees/<project-name>/ (global location)

Which would you prefer?
```

## 安全校验

### 对项目内目录（`.worktrees` / `worktrees`）

**创建 worktree 前，必须确认目录已被 ignore：**

```bash
# Check if directory is ignored (respects local, global, and system gitignore)
git check-ignore -q .worktrees 2>/dev/null || git check-ignore -q worktrees 2>/dev/null
```

**如果没有被 ignore：**

按 Jesse 的规则 “Fix broken things immediately”：
1. 在 `.gitignore` 里加正确规则
2. 提交这个改动
3. 再继续创建 worktree

**为什么重要：**否则 worktree 内容可能误进 git 追踪。

### 对全局目录（`~/.config/superpowers/worktrees`）

不需要 `.gitignore` 校验，因为它在仓库外面。

## 创建步骤

### 1. 检测项目名

```bash
project=$(basename "$(git rev-parse --show-toplevel)")
```

### 2. 创建 Worktree

```bash
# Determine full path
case $LOCATION in
  .worktrees|worktrees)
    path="$LOCATION/$BRANCH_NAME"
    ;;
  ~/.config/superpowers/worktrees/*)
    path="~/.config/superpowers/worktrees/$project/$BRANCH_NAME"
    ;;
esac

# Create worktree with new branch
git worktree add "$path" -b "$BRANCH_NAME"
cd "$path"
```

### 3. 运行项目初始化

自动检测项目类型并执行对应初始化：

```bash
# Node.js
if [ -f package.json ]; then npm install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then poetry install; fi

# Go
if [ -f go.mod ]; then go mod download; fi
```

### 4. 验证干净基线

先跑测试，确保新 worktree 的基线是干净的：

```bash
# Examples - use project-appropriate command
npm test
cargo test
pytest
go test ./...
```

**如果测试失败：**把失败告诉用户，并询问是继续还是先调查。  
**如果测试通过：**报告工作区已可用。

### 5. 报告位置

```
Worktree ready at <full-path>
Tests passing (<N> tests, 0 failures)
Ready to implement <feature-name>
```

## 快速参考

| Situation | Action |
|-----------|--------|
| `.worktrees/` exists | Use it (verify ignored) |
| `worktrees/` exists | Use it (verify ignored) |
| Both exist | Use `.worktrees/` |
| Neither exists | Check CLAUDE.md -> Ask user |
| Directory not ignored | Add to .gitignore + commit |
| Tests fail during baseline | Report failures + ask |
| No package.json/Cargo.toml | Skip dependency install |

## 常见错误

### 跳过 ignore 校验
- **问题：**worktree 内容被 git 追踪，污染状态
- **修复：**项目内目录一律先 `git check-ignore`

### 擅自决定目录位置
- **问题：**破坏项目约定，造成混乱
- **修复：**严格遵循优先级：existing > CLAUDE.md > ask

### 基线测试失败还继续推进
- **问题：**无法区分新 bug 和旧问题
- **修复：**先报告失败，明确征得同意后再继续

### 把初始化命令写死
- **问题：**在不同项目里会失效
- **修复：**按项目文件自动检测

## 示例工作流

```
You: I'm using the using-git-worktrees skill to set up an isolated workspace.

[Check .worktrees/ - exists]
[Verify ignored - git check-ignore confirms .worktrees/ is ignored]
[Create worktree: git worktree add .worktrees/auth -b feature/auth]
[Run npm install]
[Run npm test - 47 passing]

Worktree ready at /Users/jesse/myproject/.worktrees/auth
Tests passing (47 tests, 0 failures)
Ready to implement auth feature
```

## 红旗

**绝不要：**
- 在没确认 ignore 之前创建项目内 worktree
- 跳过基线测试验证
- 在测试失败时不问就继续
- 在目录位置不明确时自己拍板
- 跳过 CLAUDE.md 检查

**始终要做：**
- 遵循目录优先级：existing > CLAUDE.md > ask
- 对项目内目录做 ignore 校验
- 自动检测并运行项目初始化
- 验证干净测试基线

## 集成关系

**由以下 skill 调用：**
- **brainstorming**（Phase 4）—— 设计确认后、实现开始前必须用
- **subagent-driven-development** —— 执行任何任务前必须用
- **executing-plans** —— 执行任何任务前必须用
- 任何需要隔离工作区的其他 skill

**配对 skill：**
- **finishing-a-development-branch** —— 工作完成后做清理
