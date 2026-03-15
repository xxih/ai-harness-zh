# Markdown Authoring

## 原则

- 主输入永远优先用 `slides.md`
- 人和 AI 都直接写 markdown，不手写页面 HTML
- 正文页默认优先使用 `layout: markdown`
- 如果某一页开始先设计卡片结构，再回头塞内容，通常说明这页还没有写对

## 默认写法

一页就是一个 markdown block，用 `---` 分隔：

```md
---
title: 总标题
cover_title: 封面标题
theme: clean-notes
cta: 结尾行动引导
restructure_notes:
  - 重组说明 1
  - 重组说明 2
---

# 装好 Codex App // 跑通你的第一个 Agent
> id: slide-01
> layout: cover
> eyebrow: AI Agent 课程｜第 1 课
> chip: 安装 App
> chip: 配好 API
> chip: 生成 hello.md
> goal: 说明这一页的目标
> layout-note: 封面页只保留标题、导语和结果标签
> body-note: 装好 Codex App
> body-note: 配好 API
> body-note: 生成 hello.md

这一课只做一件事：把 Codex App 装好、把 API 接好、再让 Agent 真正在你的电脑里创建一个文件。

---

# 这节课到底要完成什么
> id: slide-02
> layout: markdown
> eyebrow: 先看范围
> goal: 先把本课边界讲清楚
> layout-note: 标题 + 段落 + 列表，直接按 markdown 流式渲染
> body-note: 装好 Codex App
> body-note: 用 CC Switch 配好 API
> body-note: 让 Agent 创建 hello.md

先别追求复杂能力，这一课只要把最小闭环跑通。

## 你要拿下的 3 件事
- 装好 Codex App，并且能正常打开
- 用 CC Switch 配好供应商和 API Key
- 让 Agent 在当前项目里创建 `hello.md`
```

## `layout: markdown` 支持什么

默认正文页直接写这些 markdown 元素：

- 普通段落
- `##` 二级标题
- `###` 三级标题
- 无序列表 `- item`
- 有序列表 `1. item`
- 代码块 ```` ```text ```` 或其他 fence
- 行内代码 `` `code` ``
- 加粗 `**重点**`
- 链接 `[文字](https://example.com)`

脚本负责统一渲染它们，不需要你手动写 HTML 容器。

## 写正文时的建议

- 一页只放一个核心点
- 单页尽量控制在 `2-4` 个小节内
- 能用列表讲清楚，就不要再拆成“卡片标题 + 卡片描述”
- 代码块只保留必要内容，别把整段长命令都堆进去
- 如果一页开始显得拥挤，优先拆成两页，不要缩小字号硬塞

## 什么时候才用其他布局

### `cover`

- 适合第一页
- 用来放课程名、主标题、少量标签
- 封面也尽量保持克制，不要堆很多指标卡

### 其他特殊布局

- 只有某页确实需要更强的结构约束时再用
- 它们是补充，不是默认工作流
- 如果用完之后页面更像网页组件拼贴，而不是手机图文，说明用错了
