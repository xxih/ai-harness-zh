---
description: 起一个新变更并写 nanospec/<YYYYMMDD-task-name>/proposal.md（Why / What Changes / Impact）
---

调用 `nanospec` skill，按 **Phase: propose** 段执行。

参数：`$ARGUMENTS`

参数解释：

- 完整变更名（`YYYYMMDD-task-name`） → 直接用
- 任务描述 → 自动用今天日期 + 派生 kebab-case
- 留空 → 用 AskUserQuestion 问"这次要做什么变更？"
