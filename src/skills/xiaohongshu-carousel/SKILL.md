---
name: xiaohongshu-carousel
description: Use when you already have source content and need to turn it into publishable Xiaohongshu carousel images with Chinese-first rewriting, page planning, renderable source files, and export-ready PNG assets.
---

# Xiaohongshu Carousel

把已有文章、课程讲义、口播稿或长文笔记，快速转换成可直接发布的小红书图文多图。这个 skill 聚焦内容重组、拆页、排版和导出，不负责前期选题与策划。

## 何时使用

- 已经有相对完整的内容初稿
- 目标是尽快输出一组可发的小红书图文图片
- 需要多张竖版图片，而不是只要一份改写文案

不适用：

- 还没有内容，只是要找选题
- 还在做账号定位、人设、竞品分析、选题验证
- 需要补采访、补研究、补事实采集

## 产物

每次使用本 skill，默认产出以下最小集合：

1. 结构化源文件
   - `output/xiaohongshu/<topic>/slides.md`
2. 图片成品
   - `output/xiaohongshu/<topic>/slide-01.png` 到 `slide-0N.png`
3. 可回溯源文件
   - `output/xiaohongshu/<topic>/slide-01.html` 到 `slide-0N.html`
   - 或 `output/xiaohongshu/<topic>/slide-01.svg` 到 `slide-0N.svg`
4. 交付清单
   - `output/xiaohongshu/<topic>/manifest.md`
5. 编译产物
   - `output/xiaohongshu/<topic>/source.json`
6. 生成入口
   - `scripts/build_xiaohongshu_carousel.py`

默认要求：

- `slides.md` 是主要事实来源，后续改样式或重导出时优先改这里
- `source.json` 可以作为脚本编译后的中间结构，但不应成为主要人工编辑对象
- 不要把一次性的手写 HTML 当成长期工作流
- 正文页默认优先使用 `layout: markdown`，直接写 markdown 内容，再交给脚本渲染
- 只有在信息表达确实需要时，才额外使用 `cover` 之外的特殊布局；不要先把内容改写成一堆卡片语义结构
- 至少支持两套以上视觉风格，优先通过主题切换而不是复制页面文件实现

如果当前环境不能直接导出 PNG，至少保留可渲染源文件和 `manifest.md`，并在结论中说明缺失的导出步骤。

## 工作流

1. 先界定输入边界
   - 明确这次只处理“已有内容 -> 小红书图文”
   - 不擅自扩展到选题、调研、账号定位等前期工作
2. 先做拆页规划
   - 通读原文，判断更适合教程型、清单型、步骤型、避坑型还是总结型结构
   - 先定页数和每页角色，再写每页内容
3. 重写为手机可读版本
   - 保留原文事实、流程顺序、技术名词和关键操作
   - 压缩冗余表达，改成适合翻页阅读的短段落和结构化信息块
4. 生成可发布资产
   - 先把页结构写入 `slides.md`
   - 除封面等少量特殊页外，正文默认直接写 `layout: markdown`
   - 用统一脚本把 markdown 编译成 HTML、`manifest.md` 和 `source.json`
   - 优先直接输出 PNG
   - 若环境不支持，输出 HTML 或 SVG 源文件，保证后续可稳定导出 PNG
   - 同时写出 `manifest.md`
5. 自检后交付
   - 检查尺寸、页数、封面钩子、正文密度、结尾收束
   - 检查是否引入原文没有支持的结论或事实
   - 检查当前主题是否真的适合手机阅读，而不是桌面网页截图感

## 版式标准

- 画布固定为 `1242x1660`
- 比例固定为 `3:4`
- 整体风格统一，不要每页像不同模板拼接
- 优先中文阅读体验，字号、行距、留白按手机阅读优化
- 默认优先“大字少字”，宁可多一页，也不要把一页塞成文字墙
- 每页只表达一个核心点
- 单页正文尽量控制在 `3-6` 个信息块内，避免大段文字墙
- 封面必须有强钩子标题，让读者一眼知道这组图解决什么问题
- 正文页优先使用步骤、清单、对比、提醒、结论卡片等结构
- 结尾页必须有明确收束，例如完成标志、复盘、行动建议或下一步

## 内容约束

- 不编造事实、案例、数据、用户反馈、平台规则或原文没有支持的结论
- 可以重写表达，但不能改变关键步骤和技术准确性
- 如果信息不足以支持强结论，宁可保守表达
- 如果原文有重复信息，主动合并
- 如果原文层级太深，主动重组成更适合翻页阅读的顺序

## 交付格式

`manifest.md` 至少包含：

- 总标题
- 封面标题
- 每页页码
- 每页一句话目标
- 每页正文文案
- 每页版式说明
- 结尾页行动引导
- 重组说明

`slides.md` 至少包含：

- 顶部 frontmatter：主题、总标题、封面标题、CTA、重组说明
- 每页的标题
- 每页的布局类型
- 每页的 markdown 正文
- 每页在 `manifest.md` 中的目标、正文摘要、版式说明

`source.json` 至少包含：

- 主题名
- 总标题
- 封面标题
- 每页的布局类型
- 每页的文案结构数据
- 每页在 `manifest.md` 中的目标、正文摘要、版式说明

## 脚本

优先使用 `scripts/build_xiaohongshu_carousel.py` 从 `slides.md` 统一生成交付文件，而不是手写每一页 HTML。

脚本应满足：

- 读取 `slides.md`
- 将 markdown 编译为统一的结构化数据
- 支持主题切换
- 批量输出 `slide-*.html`
- 批量输出 `manifest.md`
- 允许后续接 PNG 导出流程

当你需要决定主题或页型时，先读参考文件，再改 `slides.md`，不要直接改最终 PNG 或手写 HTML。

## 模板

需要页型参考和 `manifest.md` 模板时，读取 [references/page-patterns.md](references/page-patterns.md)。
需要主题选择建议时，读取 [references/visual-styles.md](references/visual-styles.md)。
需要 markdown 写法时，读取 [references/markdown-authoring.md](references/markdown-authoring.md)。
