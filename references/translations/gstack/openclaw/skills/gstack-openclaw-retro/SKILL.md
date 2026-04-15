---
name: gstack-openclaw-retro
description: 每周工程回顾。分析 commit 历史、工作模式和代码质量指标，保留持久化历史并跟踪趋势。具备团队意识，会识别当前执行用户，并分别总结每个贡献者的亮点与成长点。用户要求 weekly retro、what shipped this week 或 engineering retrospective 时使用。
version: 1.0.0
metadata: { "openclaw": { "emoji": "📊" } }
---
<!-- 中文参考译文。 -->

# Weekly Engineering Retrospective

生成一份按时间窗口展开的工程回顾，重点看这段时间到底交付了什么、节奏如何、质量有没有变好。

## 参数

- 默认：最近 7 天
- `24h`
- `14d`
- `30d`
- `compare`：当前窗口对比上一段等长窗口

## 核心关注点

- commit 历史与交付节奏
- 团队 / 个人贡献分布
- praise 与 growth areas
- 代码质量趋势与模式变化

## 关键规则

- 时间计算按用户本地时区。
- 以午夜对齐的绝对日期窗口统计天级区间。
- 输出既要能看团队整体，也要能看每位贡献者的差异。
