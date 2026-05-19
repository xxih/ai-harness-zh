---
name: finishing-a-development-branch
description: 当实现已经完成、所有测试都通过，并且你需要决定如何集成这些工作时使用；它通过结构化选项指导你完成 merge、PR 或清理收尾
---

# 完成开发分支

## 概览

用清晰选项引导开发收尾，并按用户选择执行对应流程。

**核心原则：**先验证测试 -> 检测环境 -> 展示选项 -> 执行用户选择 -> 最后清理。

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

### 第二步：检测环境

**展示选项前，先判断当前工作区状态：**

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
```

这一步会决定要展示哪套菜单，以及后续怎样清理：

| 状态 | 菜单 | 清理方式 |
|-------|------|---------|
| `GIT_DIR == GIT_COMMON`（普通仓库） | 标准 4 选项 | 没有 worktree 需要清理 |
| `GIT_DIR != GIT_COMMON`，且在命名分支上 | 标准 4 选项 | 按来源判断是否清理（见第六步） |
| `GIT_DIR != GIT_COMMON`，且是 detached HEAD | 精简 3 选项（无 merge） | 不清理（外部托管） |

### 第三步：确定基础分支

```bash
# Try common base branches
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null
```

或者直接问："This branch split from main - is that correct?"

### 第四步：展示选项

**普通仓库和命名分支 worktree：必须原样展示下面 4 个选项：**

```
Implementation complete. What would you like to do?

1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)
4. Discard this work

Which option?
```

**detached HEAD：必须原样展示下面 3 个选项：**

```
Implementation complete. You're on a detached HEAD (externally managed workspace).

1. Push as new branch and create a Pull Request
2. Keep as-is (I'll handle it later)
3. Discard this work

Which option?
```

**不要补充解释。**保持简洁。

### 第五步：执行用户选择

#### 选项 1：本地合并

```bash
# Get main repo root for CWD safety
MAIN_ROOT=$(git -C "$(git rev-parse --git-common-dir)/.." rev-parse --show-toplevel)
cd "$MAIN_ROOT"

# Merge first — verify success before removing anything
git checkout <base-branch>
git pull
git merge <feature-branch>

# Verify tests on merged result
<test command>

# Only after merge succeeds: cleanup worktree (Step 6), then delete branch
```

然后执行：清理 worktree（第六步），再删除分支：

```bash
git branch -d <feature-branch>
```

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

**不要清理 worktree。**用户还需要保留它来继续处理 PR 反馈。

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
MAIN_ROOT=$(git -C "$(git rev-parse --git-common-dir)/.." rev-parse --show-toplevel)
cd "$MAIN_ROOT"
```

然后执行：清理 worktree（第六步），再强制删除分支：

```bash
git branch -D <feature-branch>
```

### 第六步：清理工作区

**只对选项 1 和 4 执行。**选项 2 和 3 一律保留 worktree。

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
WORKTREE_PATH=$(git rev-parse --show-toplevel)
```

**如果 `GIT_DIR == GIT_COMMON`：**当前是普通仓库，没有 worktree 需要清理，结束。

**如果 worktree 路径位于 `.worktrees/`、`worktrees/` 或 `~/.config/superpowers/worktrees/` 下：**这是 Superpowers 自己创建的 worktree，可以清理。

```bash
MAIN_ROOT=$(git -C "$(git rev-parse --git-common-dir)/.." rev-parse --show-toplevel)
cd "$MAIN_ROOT"
git worktree remove "$WORKTREE_PATH"
git worktree prune  # 自愈：清掉陈旧注册
```

**否则：**当前工作区由宿主环境（harness）托管，**不要**手动移除它。如果平台提供退出工作区的原生工具，就用那个；否则保持原样。

## 快速参考

| Option | Merge | Push | Keep Worktree | Cleanup Branch |
|--------|-------|------|---------------|----------------|
| 1. Merge locally | yes | - | - | yes |
| 2. Create PR | - | yes | yes | - |
| 3. Keep as-is | - | - | yes | - |
| 4. Discard | - | - | - | yes (force) |

## 常见错误

**跳过测试验证**
- **问题：**把坏代码合进来，或开出失败的 PR
- **修复：**展示选项前必须先验证测试

**提开放式问题**
- **问题：**“What should I do next?” 太模糊
- **修复：**必须给出精确的 4 个结构化选项（detached HEAD 时是 3 个）

**为选项 2 清理 worktree**
- **问题：**把用户后续处理 PR 反馈需要的 worktree 提前删掉
- **修复：**只在选项 1 和 4 清理

**删除分支早于移除 worktree**
- **问题：**worktree 仍然引用该分支时，`git branch -d` 会失败
- **修复：**先完成合并，再移除 worktree，最后删分支

**在 worktree 内部执行 `git worktree remove`**
- **问题：**当当前目录就是待删除 worktree 时，命令可能静默失败
- **修复：**先 `cd` 回主仓库根目录，再执行 `git worktree remove`

**清理了 harness 托管的 worktree**
- **问题：**误删宿主环境创建的工作区，会造成幽灵状态
- **修复：**只清理位于 `.worktrees/`、`worktrees/` 或 `~/.config/superpowers/worktrees/` 下的 worktree

**丢弃前不确认**
- **问题：**误删工作
- **修复：**必须要求用户显式输入 `discard`

## 红旗

**绝不要：**
- 测试失败还继续推进
- 不验证合并结果就合并
- 不确认就删除工作
- 未经明确要求就 force-push
- 在确认合并成功前就移除 worktree
- 清理不是你自己创建的 worktree（来源校验失败）
- 在 worktree 内部直接运行 `git worktree remove`

**始终要做：**
- 展示选项前先验证测试
- 展示菜单前先检测环境
- 只展示那 4 个选项（detached HEAD 时是 3 个）
- 选项 4 必须要求用户键入确认
- 选项 1 和 4 要清理 worktree
- 在移除 worktree 前先 `cd` 回主仓库根目录
- 移除后执行 `git worktree prune`
