---
description: 在 proposal 之后落 nanospec/<name>/design.md + tasks.md
---

调用 `nanospec` skill，按 **Phase: plan** 段执行。

参数：`$ARGUMENTS`（变更名 `<name>`，省略时按上下文推断）

要求：`nanospec/<name>/proposal.md` 已存在；不存在时先回去跑 `/propose`。
