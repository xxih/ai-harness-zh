---
description: 面向多 agent 工作流的顺序执行与 tmux/worktree 编排指南。
---

# 编排命令

用于复杂任务的顺序式 agent 工作流。

## 使用

`/orchestrate [workflow-type] [task-description]`

## 工作流类型

### feature

完整功能实现工作流：

```
planner -> tdd-guide -> code-reviewer -> security-reviewer
```

### bugfix

错误调查与修复工作流：

```
planner -> tdd-guide -> code-reviewer
```

### refactor

安全重构工作流：

```
architect -> code-reviewer -> tdd-guide
```

### security

安全审查工作流：

```
security-reviewer -> code-reviewer -> architect
```

## 执行模式

针对工作流中的每个代理：

1. 带着上一个代理留下的上下文**调用下一个代理**
2. 将输出收集为结构化交接文档
3. 将交接文档**传递给链中的下一个代理**
4. 将所有结果**汇总**为最终报告

## 交接文档格式

在代理之间创建如下交接文档：

```markdown
## HANDOFF: [previous-agent] -> [next-agent]

### Context
[已完成工作的总结]

### Findings
[关键发现或决定]

### Files Modified
[已触及的文件列表]

### Open Questions
[留给下一位代理人的未决事项]

### 建议
[建议的后续步骤]

```

## 示例：功能工作流

```
/orchestrate feature "Add user authentication"
```

执行流程：

1. **Planner Agent**
   - 分析需求
   - 生成实施计划
   - 识别依赖
   - 输出：`HANDOFF: planner -> tdd-guide`

2. **TDD Guide Agent**
   - 读取 planner 的交接文档
   - 先写测试
   - 编写实现直到测试通过
   - 输出：`HANDOFF: tdd-guide -> code-reviewer`

3. **Code Reviewer Agent**
   - 审查实现
   - 检查问题
   - 提出改进建议
   - 输出：`HANDOFF: code-reviewer -> security-reviewer`

4. **Security Reviewer Agent**
   - 执行安全审计
   - 检查漏洞
   - 给出最终放行意见
   - 输出：最终报告

## 最终报告格式

```
ORCHESTRATION REPORT
====================
Workflow: feature
Task: Add user authentication
Agents: planner -> tdd-guide -> code-reviewer -> security-reviewer

SUMMARY
-------
[One paragraph summary]

AGENT OUTPUTS
-------------
Planner: [summary]
TDD Guide: [summary]
Code Reviewer: [summary]
Security Reviewer: [summary]

FILES CHANGED
-------------
[List all files modified]

TEST RESULTS
------------
[Test pass/fail summary]

SECURITY STATUS
---------------
[Security findings]

RECOMMENDATION
--------------
[SHIP / NEEDS WORK / BLOCKED]
```

## 并行执行

对于彼此独立的检查，可以并行运行多个代理：

```markdown
### 并行阶段
同时运行：
- code-reviewer（质量）
- security-reviewer（安全）
- architect（设计）

### 合并结果
将输出合并为单一报告

```

对于使用独立 git worktree 的外部 tmux-pane worker，请使用 `node scripts/orchestrate-worktrees.js plan.json --execute`。内置编排模式保持在当前进程内运行；这个辅助工具更适合长时间运行或跨测试框架的会话。

当 worker 需要看到主检出目录中的脏文件或未跟踪本地文件时，请在计划文件中加入 `seedPaths`。ECC 只会在 `git worktree add` 之后把这些选定路径覆盖到各 worker 的 worktree 中，从而既维持分支隔离，又能暴露正在编辑的本地脚本、计划或文档。

```json
{
  "sessionName": "workflow-e2e",
  "seedPaths": [
    "scripts/orchestrate-worktrees.js",
    "scripts/lib/tmux-worktree-orchestrator.js",
    ".claude/plan/workflow-e2e-test.json"
  ],
  "workers": [
    { "name": "docs", "task": "Update orchestration docs." }
  ]
}
```

若要导出实时 tmux/worktree 会话的 control plane 快照，请运行：

```bash
node scripts/orchestration-status.js .claude/plan/workflow-visual-proof.json
```

快照会以 JSON 形式记录会话活动、tmux pane 元数据、worker 状态、目标、seed 覆盖层以及最近的交接摘要。

## 操作员指挥中心交接

当工作流跨越多个会话、worktree 或 tmux pane 时，请在最终交接中追加一个 control-plane 区块：

```markdown
CONTROL PLANE
-------------
Sessions:
- 活动会话 ID 或别名
- 每个活跃 worker 的分支与 worktree 路径
- 若适用，附上 tmux pane 或 detached session 名称

Diffs:
- git 状态摘要
- 已修改文件的 git diff --stat
- 合并/冲突风险说明

Approvals:
- 待处理的用户审批
- 等待确认的受阻步骤

Telemetry:
- 最后活动时间戳或空闲信号
- 预估的令牌或成本漂移
- 由钩子或审查器引发的策略事件
```

这能让 planner、implementer、reviewer 以及 loop worker 在操作员视角下保持清晰可见。

## 参数

$ARGUMENTS:

- `feature <description>` - 完整功能工作流
- `bugfix <description>` - 缺陷修复工作流
- `refactor <description>` - 重构工作流
- `security <description>` - 安全审查工作流
- `custom <agents> <description>` - 自定义代理序列

## 自定义工作流示例

```
/orchestrate custom "architect,tdd-guide,code-reviewer" "Redesign caching layer"
```

## 提示

1. **复杂功能先从 planner 开始**
2. **合并前始终包含 code-reviewer**
3. 处理认证、支付、PII 时**务必加入 security-reviewer**
4. **保持交接简洁**，只保留下一个代理真正需要的信息
5. 需要时，**在代理之间插入验证步骤**
