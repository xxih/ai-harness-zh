# Promote Candidates

## 2026-03-17 小红书图文字体与产物落位

### Candidate: 为图文导出链路补一条字体诊断与渲染器选择说明

- 来源任务：把 `0316 AI 时代的词汇量.md` 改写成小红书风格并导出图文，排查宋体在 CLI 与 web 导出不一致的问题。
- 想沉淀的模式：当 web 和 CLI 导出视觉效果不一致时，先判断是否属于浏览器字体能力与 node 字体嵌入能力差异；若命中 TTC 或系统字体限制，优先提供 browser renderer 或自动 fallback，而不是继续猜 CSS。
- 为什么可能跨任务复用：这类问题不只会出现在宋体，也会反复出现在本机系统字体、中文字体和“web 看着对、CLI 不对”的导出任务里。
- 现有重叠资产：`xhs-md-renderer` 里已落地实现，但还没有一个面向使用者的简明说明；当前 `life` 仓库也没有一条记录解释为什么这次需要重打包。
- 建议动作：`absorb`
- 需要补的内容：把“何时选 browser renderer、何时保持 node renderer、如何识别 TTC 字体问题”的最小说明补到 `xhs-md-renderer` 的 README 或 CLI 帮助文案。
