# 写作内核 skill 拆解

## 1. 本轮决策

### 1.1 采用方式

本轮对 `article-writing` 的处理结论是：`adapt`，不是 `adopt`、也不是 `build`。

原因：

- 它已经把长文写作最核心的行为约束压缩得很短；
- 但当前仓库需要中文表达、package-first 组织，以及更清楚的“覆盖 / 不覆盖”边界；
- 这轮用户要看的重点不是单篇文章 prompt，而是“内容生产骨架”。

### 1.2 第一版 skill 的定位

`packages/content-writing/skills/content-writing/SKILL.md` 当前定位是：

- 平台无关的写作内核
- 偏长文与结构化内容
- 强调 voice、结构、事实纪律、AI 味清理
- 不承担策略、研究、分发、平台发布

它解决的是“怎么把内容写好”，不是“写什么”“发到哪”“怎么运营”。

## 2. 内容生产骨架

我把当前样本里的能力拆成 6 层：

| 层次 | 解决的问题 | 代表能力 | 当前第一版是否覆盖 |
|---|---|---|---|
| 1. 策略层 | 该写什么、为什么写、围绕哪些支柱写 | content strategy、topic cluster、content calendar | 否 |
| 2. 研究 / brief 层 | 写之前需要哪些资料、角度、关键词、证据 | research、SERP、brief、sources | 否 |
| 3. 写作内核层 | 怎样把材料写成一篇可信、好读、有风格的正文 | voice、structure、draft、rewrite、quality gate | 是 |
| 4. 多平台改写层 | 一份源内容如何拆成不同平台版本 | repurposing、platform-native variants | 否 |
| 5. 平台适配 / 发布层 | 公众号、小红书等平台怎么排版、怎么发 | title、layout、publish workflow | 否 |
| 6. 运营 / 复盘层 | 发完之后怎么排期、看数据、持续优化 | engagement、calendar、analytics | 否 |

换句话说：

- 第一版只覆盖第 3 层；
- 第 1、2、4、5、6 层当前都故意留空；
- 这样做的好处是：先把“写得好”这件事单独站稳，不被平台细节拖散。

## 3. 第一版 skill 具体覆盖什么

### 3.1 已覆盖

- 明确 audience、purpose、delivery format
- 捕捉 voice：句长、节奏、修辞、幽默度、格式习惯
- 骨架优先：先定每节职责，再写正文
- 开头先落具体例子、结果、数字、场景
- 删除模板味、空话、无证据夸张
- 交付前检查事实性、文风一致性、每节信息增量

### 3.2 明确不覆盖

- 选题优先级、内容支柱、内容日历
- SEO 关键词、SERP 分析、搜索意图判断
- research / source gathering / content brief
- 多平台 repurposing
- 中文平台标题、排版、封面图建议
- 发布自动化、账号操作、数据复盘

### 3.3 这意味着什么

第一版是“写作者”而不是“编辑部”或“运营团队”。

它适合：

- 直接写文章
- 把资料整理成文章
- 把已有草稿重写得更像真人、更成体系

它不适合：

- 从零规划整套内容体系
- 做 SEO 内容生产线
- 一稿多投到多个平台
- 接管公众号 / 小红书的最终发稿动作

## 4. 其他 skill 能补什么

| skill | 主要层次 | 最值得借的东西 | 当前建议 |
|---|---|---|---|
| `article-writing` | 写作内核层 | voice capture、短而强的写作纪律 | 已作为第一版基座 `adapt` |
| `content-production` | 研究 / brief + draft + optimize | research、source、brief、SEO 与 publish-ready gate | 先只借骨架，后续可拆增强层 |
| `content-strategy` | 策略层 | content pillars、topic cluster、priority topics | 暂不并入，作为上游规划层 |
| `content-engine` | 多平台改写层 | anchor asset -> atomic ideas -> platform-native variants | 暂不并入，未来适合单独做 skill |
| `social-content` | 运营 / 分发层 | content pillars 与社媒节奏、排期、互动优化 | 只作运营层参考 |
| `wechat-article-writer` | 平台适配层 | 中文公众号 workflow、标题、排版意识 | 未来如要做中文平台层，可局部 adapt |
| `xhs-publisher` | 发布层 | 小红书真实发布动作与安全边界 | 明确不并入写作内核 |

## 5. 一眼看懂的覆盖关系

### 5.1 当前已有

- “怎么把长文写好” -> 已覆盖

### 5.2 当前缺口

- “该写什么” -> 缺策略层
- “写前需要哪些材料和 brief” -> 缺研究层
- “一篇内容怎么变成多平台版本” -> 缺 repurposing 层
- “公众号 / 小红书怎么做最后一跳” -> 缺平台适配 / 发布层
- “发完怎么持续优化” -> 缺运营层

### 5.3 当前最合理的组合方式

短期内不要把所有层揉成一个 skill，而是把它们看成未来可拼装的 skill 家族：

1. `content-writing` 负责写作内核
2. 未来可新增 research / brief skill
3. 未来可新增 content repurposing skill
4. 未来可新增 中文平台 adapter skill
5. 未来可新增 publish / ops skill

## 6. 后续优化方向候选

### 方向 A：保持“小而强”

只继续打磨 `content-writing` 本身：

- 增加更细的写作类型指引
- 增加更明确的“重写已有草稿”路径
- 增加中文常见 AI 味清单

适合：你想先把“写得像人”这件事做扎实。

### 方向 B：补 research / brief 层

吸收 `content-production` 的前半段：

- sources
- research checklist
- brief 模板
- 事实性证据门禁

适合：你想让写作不是凭空生成，而是更像可复用生产流。

### 方向 C：补多平台改写层

吸收 `content-engine`：

- anchor asset
- atomic ideas
- platform-native variants

适合：你已有源文章，下一步最关心“一稿多形态分发”。

### 方向 D：补中文平台层

吸收 `wechat-article-writer` 的中文平台意识，但不要整体照搬：

- 标题候选
- 排版建议
- 中文自媒体语境

适合：你接下来重点是公众号 / 中文内容生产。

### 方向 E：补发布 / 运营层

把发布与运营单独拆出去：

- publish adapter
- content calendar
- analytics / iteration

适合：你要的不只是会写，而是完整内容生产系统。

## 7. 当前建议

如果目标是“先看到最清楚的骨架，再决定往哪长”，当前最合适的停点就是现在这版：

- 先把 `content-writing` 固定为第 3 层写作内核；
- 暂时不把其他层塞进来；
- 下一轮再按你的优先级，从 research、repurposing、中文平台、发布运营里选一层单独增强。
