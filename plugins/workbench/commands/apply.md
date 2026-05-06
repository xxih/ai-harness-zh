---
description: 按 nanospec/<name>/tasks.md 逐条实现并即时勾选
---

调用 `nanospec` skill，按 **Phase: apply** 段执行。

参数：`$ARGUMENTS`（变更名 `<name>`，省略时按以下顺序推断：对话上下文 → `nanospec/` 下唯一活跃变更 → AskUserQuestion 让用户选）。

要求：`nanospec/<name>/tasks.md` 已存在；不存在时先回去跑 `/plan`。
