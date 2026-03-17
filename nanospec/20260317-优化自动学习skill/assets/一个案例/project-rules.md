# Project Rules

## 2026-03-17 小红书图文字体与产物落位

### Rule Candidate: 小红书图文产物不要放在 attachment 目录

- 规则内容：图文导出产物应放在笔记旁边的独立目录，并保留 `render-config/` 与 `output/` 这类可重复生成结构；不要把最终交付物放进 attachment 目录。
- 作用范围：`project`
- 来源纠正：本次对话中用户明确纠正“不要把产物放在 attachment 里”“找个另外的地方放”。
- 证据：当前产物实际落在 [output](/Users/xxih/Documents/life/05 Journal/01 日记/0316 AI 时代的词汇量 - 小红书图文/output)，且相关提交为 `b31cd8f Move Xiaohongshu render assets out of attachments` 与 `763d5e4 Refresh XHS export with browser-rendered Songti output`。
- 建议落点：`AGENTS.md`
- 当前状态：`propose-agents-update`

### Rule Candidate: 外部工具生成的最终图文也要回写到 life 仓库内

- 规则内容：即使渲染工具位于别的代码仓库，最终交付给笔记使用的图文产物也应写回 `life` 仓库中的目标目录，再由 `life` 仓库单独提交。
- 作用范围：`project`
- 来源纠正：本次对话中用户明确要求“重新打包输出在 life 库里”。
- 证据：工具修复提交位于 `/Users/xxih/workspace/xhs-md-renderer` 的 `5e16357`，最终产物提交位于当前仓库的 `763d5e4`，两者被有意拆开。
- 建议落点：`AGENTS.md`
- 当前状态：`propose-agents-update`
