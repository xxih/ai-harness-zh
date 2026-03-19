# 方案：写作内核 skill 第一版

## 总体策略

本轮采用 `adapt article-writing + 拆清边界 + 留出扩展接口` 的策略。

原因：

1. `article-writing` 已经证明自己适合作为“小而强”的写作内核。
2. 用户当前更想看清楚“内容生产骨架”，而不是一次性做完整内容工厂。
3. 仓库已有 package-first 组织方式，适合先落一个独立 package，再看是否加上游 / 下游配套能力。

## 实施方式

### 阶段 1：确定第一版边界

第一版只保留最核心的写作动作：

- audience / purpose / voice 对齐
- 文章骨架搭建
- 正文展开
- 模板味清理
- 事实与文风质量门禁

明确排除：

- 选题策略
- SEO research / brief
- 多平台改写
- 平台排版与发布
- 发布后运营优化

### 阶段 2：落正式 package

新增 `packages/content-writing/`，保持最小结构：

- `README.md`
- `skills/content-writing/SKILL.md`
- `targets/codex/README.md`

skill 正文尽量短，只保留真正影响行为的规则与流程。

### 阶段 3：写骨架拆解文档

在 NanoSpec 任务下写一份分析文档，按“内容生产层次”拆开：

1. 策略层
2. 研究 / brief 层
3. 写作内核层
4. 多平台改写层
5. 平台适配 / 发布层
6. 复盘 / 运营层

然后把参考 skill 放回这些层里，看哪里已覆盖、哪里仍空缺。

### 阶段 4：同步 README 与 target

新增 package 后：

- 更新 `README.md`
- 更新 `packages/README.md`
- 运行 `python3 scripts/sync_codex_targets.py content-writing`

## adopt / adapt / build 判断

- `article-writing`：`adapt`
  - 直接吸收其写作核心规则与 voice capture 骨架
  - 改写为当前仓库中文风格与更清楚的边界表达
- `content-engine`：`reference`
  - 作为未来多平台改写层参考，不并入第一版
- `content-production`：`reference`
  - 作为未来 research / brief / optimize 增强层参考
- `content-strategy`：`reference`
  - 作为未来选题和内容规划层参考
- `wechat-article-writer`：`reference`
  - 作为中文平台适配层参考
- `social-content` / `xhs-publisher`：`reference`
  - 分别作为运营分发层与发布适配层参考

## 风险与收口

### 风险 1：skill 变成“大而全内容工厂”

收口：

- skill 正文显式写出不覆盖范围
- 研究、平台、发布能力只在拆解文档中作为后续候选层

### 风险 2：内容生产骨架说不清，导致用户仍看不出方向

收口：

- 用层次图 + 参考 skill 对照表表达
- 每层都写“当前覆盖 / 当前不覆盖 / 可借鉴来源”

### 风险 3：新增 package 后仓库说明失真

收口：

- 同步更新 `README.md` 与 `packages/README.md`
- 完成 target 同步，保持 source / target 一致
