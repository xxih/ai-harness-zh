# 方案：内容写作平台skills调研

## 总体策略

本轮采用“已有本地参考 + 定向补拉外部仓库 + 场景矩阵比较”的方式推进，不做大范围泛搜。

原因：

1. 当前仓库已经有 `everything-claude-code` 等强参考源，可先复用。
2. 用户明确提到内容写作与平台写作，适合围绕少量高信号仓库做深读，而不是拉一堆泛化 prompt 集合。
3. 最终目标是形成后续可吸收的判断，因此重点是“结构化比较”，不是“收集越多越好”。

## 实施方式

### 阶段 1：建立候选池

候选分三层：

1. 当前本地已有且明显相关的 skill：
   - `everything-claude-code/skills/article-writing`
   - `everything-claude-code/skills/content-engine`
2. 面向中文自媒体 / 平台发布的外部仓库：
   - `happy-claude-skills`
   - `byheaven-skills`
3. 面向营销内容体系、内容工厂与社媒分发的外部仓库：
   - `alirezarezvani/claude-skills`

### 阶段 2：按场景读取关键 skill

只读取和本轮问题直接相关的 skill：

- 长文 / article：`article-writing`、`content-production`
- 多平台改写：`content-engine`、`social-content`
- 内容规划：`content-strategy`
- 中文平台：`wechat-article-writer`、`xhs-publisher`

避免把大仓库里的无关 skill 一起读进来，降低噪音。

### 阶段 3：建立比较维度

调研文档统一按以下维度比较：

- 核心定位
- 最适用场景
- 优点
- 局限
- 是否适合直接 adopt / 局部 adapt / 仅参考

并额外区分两类能力：

- 写作 / 改写 / 选题类 skill
- 发布 / 自动化 / 平台操作类 skill

### 阶段 4：给出组合建议

最终不只给单个 skill 排名，而是给场景组合：

- 长文写作组合
- 多平台内容引擎组合
- 公众号写作组合
- 小红书写作 + 发布组合

## 风险与收口

### 风险 1：把“发布插件”误判成“写作 skill”

收口：

- 单独标记 `xhs-publisher` 这类自动化能力，避免把它和内容策划 / 写作能力混为一谈。

### 风险 2：大而全仓库看起来很强，但不适合直接吸收

收口：

- 对 `alirezarezvani/claude-skills` 只抽取内容写作链路相关 skill，不按整仓推荐。

### 风险 3：中文平台结论过度泛化

收口：

- 明确指出目前找到的中文平台 skill 主要覆盖公众号与小红书，且小红书更偏发布自动化，这是基于当前样本的判断。

### 风险 4：本地已有翻译资产与原文口径不一致

收口：

- 以原始 `references/repos/*` 为主要判断依据；中文翻译只作为辅助阅读入口。
