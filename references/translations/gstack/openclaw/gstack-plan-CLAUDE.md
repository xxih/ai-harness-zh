# gstack-plan: Full Review Gauntlet

当用户想先规划一个 Claude Code project 时，由 orchestrator 注入。
请追加到现有 `CLAUDE.md` 之后。

## Planning Pipeline

1. 阅读 `CLAUDE.md`，理解项目上下文。
2. 运行 `/office-hours`，产出一份 design doc（problem statement、premises、alternatives）。
3. 运行 `/autoplan`，审阅这份设计（CEO + eng + design + DX reviews + codex adversarial）。
4. 把最终审阅后的 plan 保存到一个 orchestrator 之后可引用的文件里。写到：
   `plans/<project-slug>-plan-<date>.md`
5. 回报给 orchestrator：
   - Plan file path
   - 一段摘要，说明设计了什么以及关键决策
   - 被接受的 scope expansions 列表（如有）
   - 推荐下一步（通常是：spawn 一个新的 `gstack-full` session 开始实现）

不要实现任何内容。这个阶段只做规划。
orchestrator 会把 plan link 持久化到自己的 memory/knowledge store。
