# 内容写作 / 平台写作 skills 调研

## 1. 调研范围

本轮只看和以下场景强相关的 skill：

- 长文写作：article、blog、newsletter、guide
- 自媒体写作：公众号、个人品牌、内容创作
- 平台原生改写：X、LinkedIn、TikTok、YouTube、newsletter
- 中文平台：公众号、小红书
- 平台发布：把内容真正推到目标平台的自动化能力

## 2. 已拉到本地的相关仓库

| 仓库 | 本地路径 | 远端 | 本地最近提交 |
|---|---|---|---|
| everything-claude-code | `references/repos/everything-claude-code` | `https://github.com/affaan-m/everything-claude-code.git` | `fdea3085` / 2026-03-13 |
| happy-claude-skills | `references/repos/happy-claude-skills` | `https://github.com/iamzhihuix/happy-claude-skills.git` | `cffc6762` / 2026-03-18 |
| byheaven-skills | `references/repos/byheaven-skills` | `https://github.com/byheaven/byheaven-skills.git` | `fbbab52c` / 2026-03-19 |
| alirezarezvani/claude-skills | `references/repos/alirezarezvani-claude-skills` | `https://github.com/alirezarezvani/claude-skills.git` | `5adbfdce` / 2026-03-18 |

补充说明：

- `everything-claude-code` 相关中文翻译已在 `references/translations/everything-claude-code/docs/zh-CN/skills/` 下存在。
- 本轮新增拉取的是 `happy-claude-skills`、`byheaven-skills`、`alirezarezvani-claude-skills`。

## 3. 候选 skill 清单

### 3.1 `article-writing`（everything-claude-code）

- 路径：`references/repos/everything-claude-code/skills/article-writing/SKILL.md`
- 定位：长文写作与 voice capture。
- 最适用：博客、教程、newsletter、品牌长文、创始人风格文章。
- 优点：
  - skill 很短，但边界非常清楚。
  - 把“先抓 voice，再写文章”这件事写得很明确。
  - 对 AI 味、空话、套话的约束很强，适合作为长文底层写作规范。
- 局限：
  - 不处理平台发布。
  - 不包含中文平台场景。
  - 更像“写作内核”，不是完整内容运营 workflow。
- 判断：适合直接 adopt 方法论，尤其适合作为当前仓库未来“长文写作 skill”的基座。

### 3.2 `content-engine`（everything-claude-code）

- 路径：`references/repos/everything-claude-code/skills/content-engine/SKILL.md`
- 定位：多平台内容改写与 repurposing。
- 最适用：把一篇文章 / 一个 demo / 一个视频拆成 X、LinkedIn、TikTok、YouTube、newsletter 等多平台版本。
- 优点：
  - 平台差异意识很强，明确反对一稿多投。
  - 给了清晰的 repurposing flow：anchor asset -> atomic ideas -> platform-native variants。
  - 适合“一个源内容喂多个平台”的内容引擎场景。
- 局限：
  - 更偏英文社媒平台。
  - 对中文平台的规则没有直接覆盖。
  - 没有 SEO 长文那一套研究与 brief 机制。
- 判断：适合直接 adopt 到“平台内容引擎”方向；如果后续做 package，很适合做成通用平台改写层。

### 3.3 `wechat-article-writer`（happy-claude-skills）

- 路径：`references/repos/happy-claude-skills/skills/wechat-article-writer/SKILL.md`
- 定位：公众号文章 4 步 workflow：搜资料 -> 撰写 -> 标题 -> 排版。
- 最适用：中文公众号、自媒体教程文、热点解读文。
- 优点：
  - 中文场景直接可用，命名与步骤都很贴近“公众号写作”语境。
  - 明确要求先搜索资料，再写文章，不只是直接出稿。
  - 把标题和排版单独拆出来，符合公众号实际生产流程。
- 局限：
  - workflow 比较粗，很多约束写得偏经验化。
  - 强依赖 `CLAUDE.md` 风格文件，迁移到别的运行时要改口径。
  - 更像一个“单篇爆款写作流程”，不是长期内容体系。
- 判断：适合局部 adapt，尤其适合作为中文自媒体 package 的平台适配参考；不建议原样作为通用写作 skill。

### 3.4 `xhs-publisher`（byheaven-skills）

- 路径：`references/repos/byheaven-skills/plugins/xhs-publisher/skills/xhs-publisher/SKILL.md`
- 定位：小红书创作者平台发布自动化。
- 最适用：已经有标题、正文、标签，准备发布到小红书。
- 优点：
  - 平台知识很细，连入口 URL、DOM、发布形式切换都写清楚了。
  - 直接覆盖“小红书短文配图 / 图文笔记”的真实差异。
  - 安全边界较清楚：自动填充后仍由用户最终确认发布。
- 局限：
  - 这是发布 skill，不是写作 skill。
  - 对选题、结构、语气、平台文案策略支持很弱。
  - 强绑定具体平台 DOM 与浏览器自动化环境，维护成本高。
- 判断：基于文件内容，我判断它更适合作为“小红书发布适配器”，而不是当前仓库想要的内容写作主 skill。

### 3.5 `content-production`（alirezarezvani/claude-skills）

- 路径：`references/repos/alirezarezvani-claude-skills/.gemini/skills/content-production/SKILL.md`
- 定位：从 research/brief 到 draft/optimize 的完整内容生产流水线。
- 最适用：SEO 长文、B2B SaaS 内容、需要 source / keyword / brief 的文章生产。
- 优点：
  - 深度比 `article-writing` 更强，覆盖 research、brief、draft、optimize 三段。
  - 强调竞争内容分析、搜索意图、引用来源、SEO 与质量门槛。
  - 很适合作为“内容工厂”或“内容团队标准作业流”的参考。
- 局限：
  - 默认语境偏英文、偏 B2B SaaS、偏搜索流量。
  - skill 很长，且依赖配套 template / reference / script 生态。
  - 对中文自媒体和个人 IP 语境不够贴近。
- 判断：适合局部吸收工作流骨架，不适合原样搬进当前仓库。

### 3.6 `content-strategy`（alirezarezvani/claude-skills）

- 路径：`references/repos/alirezarezvani-claude-skills/.gemini/skills/content-strategy/SKILL.md`
- 定位：内容策略、topic cluster、内容规划。
- 最适用：不知道该写什么、需要建立内容支柱与选题优先级时。
- 优点：
  - 补上了选题与内容规划层，不只解决“怎么写”。
  - 对 searchable / shareable 区分比较清楚。
  - 很适合给未来的内容写作 skill 家族补一个上游策略层。
- 局限：
  - 偏市场与增长语境。
  - 需要较多业务上下文，不适合“我现在就要写一篇文”的直接调用。
- 判断：适合方法论参考，适合作为未来 package 的上游 planning 参考层。

### 3.7 `social-content`（alirezarezvani/claude-skills）

- 路径：`references/repos/alirezarezvani-claude-skills/.gemini/skills/social-content/SKILL.md`
- 定位：社交平台内容创建、排期与优化。
- 最适用：LinkedIn、X、Instagram、TikTok 这类社媒分发。
- 优点：
  - 把平台节奏、内容支柱、hook、repurposing、calendar 串成一套。
  - 比 `content-engine` 更像运营手册。
  - 对“发什么、怎么排、怎么复盘”覆盖更完整。
- 局限：
  - 平台重心仍是海外社媒。
  - 文档较长，若只想做一个轻量通用 skill，会显得过重。
- 判断：适合拆着学，不适合直接整体引入。

## 4. 场景结论

## 4.1 长文 / article writing

优先级建议：

1. `article-writing`
2. `content-production`

原因：

- `article-writing` 更适合做底层写作规范与 voice capture。
- `content-production` 更适合在需要 SEO、研究、brief、优化时做增强层。

我的判断是：如果当前仓库未来只想先落一个“小而强”的长文写作 skill，应优先吸收 `article-writing`；如果后续要做企业内容工厂，再从 `content-production` 拆研究与优化段。

## 4.2 多平台内容分发

优先级建议：

1. `content-engine`
2. `social-content`

原因：

- `content-engine` 更轻、更像通用 repurposing 内核。
- `social-content` 更重，适合补运营、排期、复盘、内容支柱。

## 4.3 中文自媒体 / 公众号

优先级建议：

1. `wechat-article-writer`
2. `article-writing`

原因：

- `wechat-article-writer` 直接命中中文公众号 workflow。
- 但它的写作质量约束不如 `article-writing` 稳，所以更适合“平台层 + 中文语境层”。

组合建议：

- 用 `article-writing` 兜底文章质量与 voice。
- 用 `wechat-article-writer` 补公众号标题、排版和中文自媒体语境。

## 4.4 小红书

优先级建议：

1. `xhs-publisher` 负责发布
2. `content-engine` 或 `article-writing` 负责内容生成

原因：

- 当前样本里，小红书方向最强的是发布自动化，不是文案生成。
- 基于已读文件，我没有找到一个同等成熟、又专门面向“小红书文案结构 + 语气 + 选题”的独立 skill。
- 因此更合理的组合是：先用通用写作 / 改写 skill 生成笔记，再用 `xhs-publisher` 做最后一跳。

这条判断属于基于当前样本的推断，不代表外部世界不存在更好的小红书写作 skill。

## 5. 总体推荐

### A 档：最值得吸收

- `article-writing`
- `content-engine`

原因：

- 边界清楚
- 复用性强
- 不过度绑定单一平台
- 能直接变成当前仓库自己的 package 素材

### B 档：值得吸收，但应拆层处理

- `content-production`
- `content-strategy`
- `social-content`

原因：

- 内容足够深
- 但仓库体量太大、上下文太重
- 更适合拆方法论，不适合原样镜像

### C 档：强平台适配层，不应误当通用写作 skill

- `wechat-article-writer`
- `xhs-publisher`

原因：

- 非常贴近中文平台实际工作流
- 但要么偏经验流，要么偏发布自动化
- 更适合作为平台 adapter，而不是通用底座

## 6. 面向当前仓库的吸收建议

如果后续要把这轮结论落成正式资产，我建议优先按下面顺序吸收：

1. 先做一个通用长文 / 内容引擎 package：吸收 `article-writing` + `content-engine`。
2. 再做中文平台适配层：吸收 `wechat-article-writer` 的公众号 workflow。
3. 最后单独评估是否需要“小红书发布适配器”这类操作性很强的 package，而不是把它混进写作 package。

换句话说：

- 写作内核和平台发布要分层。
- 中文平台 skill 值得要，但不该成为整个写作体系的默认抽象。
