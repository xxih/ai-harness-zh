---
name: finishing-a-development-branch
description: 当实现已经完成、所有测试都通过，并且你需要决定如何集成这些工作时使用；它通过结构化选项指导你完成 merge、PR 或清理收尾
---

# 完成开发分支

## 概览

用清晰选项引导开发收尾，并按用户选择执行对应流程。

**核心原则：**先验证测试 -> 再展示选项 -> 执行用户选择 -> 最后清理。

**开始时要明确说明：**“我正在使用 finishing-a-development-branch skill 来完成这项工作。”

## 流程

### 第一步：验证测试

**展示选项之前，必须先确认测试通过：**

```bash
# Run project's test suite
npm test / cargo test / pytest / go test ./...
```

**如果测试失败：**
```
Tests failing (<N> failures). Must fix before completing:

[Show failures]

Cannot proceed with merge/PR until tests pass.
```

停止。不要进入第二步。

**如果测试通过：**继续第二步。

### 第二步：确定基础分支

```bash
# Try common base branches
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null
```

或者直接问："This branch split from main - is that correct?"

### 第三步：展示选项

必须**原样**展示下面 4 个选项：

```
Implementation complete. What would you like to do?

1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)
4. Discard this work

Which option?
```

**不要补充解释。** 保持简洁。

### 第四步：执行用户选择

#### 选项 1：本地合并

```bash
# Switch to base branch
git checkout <base-branch>

# Pull latest
git pull

# Merge feature branch
git merge <feature-branch>

# Verify tests on merged result
<test command>

# If tests pass
git branch -d <feature-branch>
```

然后执行：清理 worktree（第五步）

#### 选项 2：推送并创建 PR

```bash
# Push branch
git push -u origin <feature-branch>

# Create PR
gh pr create --title "<title>" --body "$(cat <<'EOF'
## Summary
<2-3 bullets of what changed>

## Test Plan
- [ ] <verification steps>
EOF
)"
```

然后执行：清理 worktree（第五步）

#### 选项 3：保持现状

报告：`Keeping branch <name>. Worktree preserved at <path>.`

**不要清理 worktree。**

#### 选项 4：丢弃这项工作

**必须先确认：**
```
This will permanently delete:
- Branch <name>
- All commits: <commit-list>
- Worktree at <path>

Type 'discard' to confirm.
```

必须等待用户精确输入确认。

如果确认：
```bash
git checkout <base-branch>
git branch -D <feature-branch>
```

然后执行：清理 worktree（第五步）

### 第五步：清理 Worktree

**对于选项 1、2、4：**

先检查当前是否在 worktree：
```bash
git worktree list | grep $(git branch --show-current)
```

如果是：
```bash
git worktree remove <worktree-path>
```

**对于选项 3：**保留 worktree。

## 快速参考

| Option | Merge | Push | Keep Worktree | Cleanup Branch |
|--------|-------|------|---------------|----------------|
| 1. Merge locally | ✓ | - | - | ✓ |
| 2. Create PR | - | ✓ | ✓ | - |
| 3. Keep as-is | - | - | ✓ | - |
| 4. Discard | - | - | - | ✓ (force) |

## 常见错误

**跳过测试验证**
- **问题：**把坏代码合进来，或开出失败的 PR
- **修复：**展示选项前必须先验证测试

**提开放式问题**
- **问题：**“接下来你想怎么做？”太模糊
- **修复：**必须只给这 4 个结构化选项

**自动清理 worktree**
- **问题：**在用户可能还要继续处理时提前删掉 worktree（特别是选项 2、3）
- **修复：**只在选项 1 和 4 清理

**丢弃前不确认**
- **问题：**误删工作
- **修复：**必须要求用户显式输入 `discard`

## 红旗

**绝不要：**
- 测试失败还继续推进
- 不验证合并结果就合并
- 不确认就删除工作
- 未经明确要求就 force-push

**始终要做：**
- 展示选项前先验证测试
- 只展示那 4 个选项
- 选项 4 必须要求用户键入确认
- 选项 1 和 4 要清理 worktree

## 集成关系

**由以下 skill 调用：**
- **subagent-driven-development**（Step 7）—— 全部任务完成后
- **executing-plans**（Step 5）—— 全部批次完成后

**配对 skill：**
- **using-git-worktrees** —— 清理那个 skill 创建出来的 worktree
