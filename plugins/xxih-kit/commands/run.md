---
description: 一键跑完 propose → plan → apply。检测 nanospec/<name>/ 当前进度并自动接续
---

调用 `nanospec` skill，按 **Phase: run** 段执行。

参数：`$ARGUMENTS`

参数解释（场景路由）：

- 较完整的需求描述（`/run 实现用户登录…`）→ **场景 A**：自动建目录 + brief，从 propose 开始
- 仅给 `<name>` 或留空 → **场景 B**：在 `nanospec/` 下定位变更，按进度从缺口处接续

跑完一个阶段就把产物落盘再进下一阶段，确保中断后再跑 `/run` 能从断点继续。
