# Learnings

## 2026-03-17 小红书图文字体与产物落位

### Learning: macOS 上宋体类导出要优先验证浏览器渲染链路

- 场景：在本地用 `xhs-md-renderer` 把 markdown 导出成小红书图文，用户明确偏好宋体风格，并发现 web 端正常、CLI 导出不对。
- 触发信号：同一份配置下，web 导出能显示 `SimSun, 'Songti SC', serif`，CLI 导出却不是宋体；追查后 node 侧报出 `Unsupported OpenType signature ttcf`。
- 采取动作：检查 `apps/web` 和 CLI 的导出路径差异，确认 web 端依赖浏览器真实 DOM，而 CLI 走 `satori + resvg`；随后在 `/Users/xxih/workspace/xhs-md-renderer` 增加浏览器渲染导出与自动 fallback。
- 证据：`/Users/xxih/workspace/xhs-md-renderer` 提交 `5e16357 Add browser fallback for TTC font exports`；真实导出结果显示 `Renderer: browser` 且成功导出 12 页；当前产物 manifest 位于 [manifest.json](/Users/xxih/Documents/life/05 Journal/01 日记/0316 AI 时代的词汇量 - 小红书图文/output/manifest.json)。
- 适用范围：macOS 本地导出、目标字体依赖系统字体或 TTC 集合字体、且需要结果尽量贴近浏览器视觉表现的图文生成任务。
- 非适用范围：纯 web 截图流程、已经有稳定 TTF/OTF 内嵌字体的 node 渲染流程、或对浏览器依赖敏感的纯后端批处理环境。
- 当前状态：`promote-later`
