# 20260324-readme重写AIHarness定位

背景：

- 当前根 `README.md` 说明了仓库是中文维护的 AI harness 工作区，但还没有把 “AI Harness 到底是什么” 讲清楚。
- 用户希望 README 用简单直接的话说明：AI Harness 可以理解为“除了 LLM 外的一切”。
- 用户还要求补清楚：并不是所有 harness 都由我们控制，当前仓库主要沉淀的是 coding agent 暴露给我们的可定制入口。
- 这次改动不能只停留在 README 对话口径，需要按 `nanospec` 规范把 brief、spec、plan、tasks 一并落盘。

目标：

- 重写根 `README.md` 的开头说明，清楚定义 AI Harness 与本仓库关注的可定制层。
- 在 README 中列出推荐参考的 harness，并写出各自值得参考的原因。
- 在 `nanospec/20260324-readme重写AIHarness定位/` 下补齐本次任务的中间文档。

要求：

1. README 必须显式写出 “AI Harness = 除了 LLM 外的一切” 这一理解方式，但要补足具体组成，避免只剩口号。
2. README 必须说明本仓库关注的是 coding agent 暴露出来的定制口子，例如 prompt、skills、commands、hooks、rules、MCP、target 等。
3. 推荐参考对象优先使用当前仓库已经收录和持续维护的参考仓库。
4. 文案保持中文、直白、面向读者，不写这次任务过程中的对比性叙述。
