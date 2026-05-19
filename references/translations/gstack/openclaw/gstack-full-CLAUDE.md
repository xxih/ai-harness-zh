# gstack-full Pipeline

由 orchestrator 注入，用于完整 feature build。请追加到现有 `CLAUDE.md` 之后。

## Full Pipeline

1. 阅读 `CLAUDE.md`，理解项目上下文。
2. 运行 `/autoplan`，先审阅你的实现路径（CEO + eng + design review pipeline）。
3. 实现被批准的计划。执行时遵守上面的 planning discipline。
4. 运行 `/ship`，创建包含 tests、changelog 和 version bump 的 PR。
5. 回报：PR URL、已交付内容、做过的决策，以及仍不确定的点。

在 PR ready for review 之前，不要向人类索要额外输入。
