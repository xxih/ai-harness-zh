# 规格说明：写作内核 skill 第一版

## 1. 背景

上一轮已经完成内容写作相关 skill 调研，并得出几个关键判断：

- `article-writing` 最适合作为写作内核起点；
- `content-engine` 更适合作为多平台改写层；
- `content-production`、`content-strategy`、`social-content` 适合拆方法论，不适合第一版整体引入；
- `wechat-article-writer` 与 `xhs-publisher` 更像中文平台适配或发布层。

本轮要基于这些结论，落一个平台无关、边界清晰的第一版写作 skill，并把“内容生产骨架”拆出来，方便后续扩展。

## 2. 任务目标

### 2.1 第一版写作内核 skill

需要新增一个正式 package，承载平台无关的通用长文写作 skill。

成功标志：

- package 落在 `packages/content-writing/`。
- skill 正文能清楚表达适用场景、核心规则、写作流程与质量门槛。
- skill 正文明确写出不覆盖的职责，避免平台耦合。

验收证据：

- `packages/content-writing/README.md`
- `packages/content-writing/skills/content-writing/SKILL.md`
- `packages/content-writing/targets/codex/README.md`

### 2.2 内容生产骨架拆解

需要输出一份结构化文档，清楚说明：

- 第一版 skill 覆盖什么；
- 第一版 skill 不覆盖什么；
- 其他候选 skill 分别补哪一层；
- 后续可沿哪些方向继续拆分或增强。

成功标志：

- 至少覆盖写作内核、研究 / brief、策略、平台改写、平台适配 / 发布五类层次。
- 对每个参考 skill 都说明是适合 adopt、adapt 还是仅参考。
- 文档能让用户据此选择下一轮优化方向。

验收证据：

- `nanospec/20260319-写作内核skill第一版/assets/research/写作内核skill拆解.md`

### 2.3 仓库说明同步

因为本轮新增 package，需要同步更新仓库级说明文档。

成功标志：

- `README.md` 与 `packages/README.md` 都能看到新 package。
- 分类关系与包边界保持一致。

验收证据：

- `README.md`
- `packages/README.md`

### 2.4 NanoSpec 工作面完整

需要完整记录本轮需求、方案、执行与结论。

成功标志：

- 当前任务目录下有完整的 `brief.md`、`outputs/1-spec.md`、`outputs/2-plan.md`、`outputs/3-tasks.md`。
- 本轮完成后补 `outputs/summary.md`。

验收证据：

- `nanospec/20260319-写作内核skill第一版/brief.md`
- `nanospec/20260319-写作内核skill第一版/outputs/1-spec.md`
- `nanospec/20260319-写作内核skill第一版/outputs/2-plan.md`
- `nanospec/20260319-写作内核skill第一版/outputs/3-tasks.md`
- `nanospec/20260319-写作内核skill第一版/outputs/summary.md`

## 3. 非目标

- 本轮不做 SEO 全流程 skill。
- 本轮不做多平台改写或内容日历 skill。
- 本轮不做公众号 / 小红书等平台发布适配器。
- 本轮不追求把外部候选 skill 全部合并进一个大而全 package。

## 4. 约束

- 正式资产遵循 package-first。
- skill 正文默认保持平台无关。
- 若后续范围变化，要先补 `alignment.md`，再调整 spec / plan / tasks。
