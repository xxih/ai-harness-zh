---
description: 把偏差 / 临时变更落到 nanospec/<name>/alignment.md，并把影响传播到 proposal/design/tasks
---

调用 `nanospec` skill，按 **Phase: align** 段执行。

参数：`$ARGUMENTS`（可选——一句话描述当前要纠的偏差或要补充的口径；空则等用户在对话里说明）。

记得：

- 标签使用 `[偏差]` `[变更]` `[缺失]` `[歧义]` `[冲突]`
- 待用户确认的条目加 `⏳ 待确认`
- align 产生的后续动作必须落到 `tasks.md`，不要只停在 alignment.md
