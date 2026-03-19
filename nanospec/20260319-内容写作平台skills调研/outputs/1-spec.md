# 规格说明：内容写作平台skills调研

## 1. 背景

当前仓库已经有一些外部参考仓库与翻译资产，但围绕“内容写作 / 自媒体 / 平台原生写作”这条线还没有一份集中判断。用户本轮希望确认：

- 长文写作有没有成熟 skill；
- 多平台内容改写有没有成熟 skill；
- 中文自媒体尤其是公众号、小红书有没有更贴近发布场景的 skill；
- 哪些值得继续吸收，哪些只适合作为局部参考。

## 2. 任务目标

本轮需要完成一份可复用的调研结论，覆盖候选 skill 的来源、适用场景、优缺点，以及对当前仓库后续吸收方向的建议。

## 3. 交付范围

### 3.1 外部候选拉取到本地

需要把本轮新增候选仓库拉到 `references/repos/`，并记录本地路径、远端来源与本地 HEAD 信息。

成功标志：

- 至少补充 2 个以上与内容写作相关的外部仓库到本地。
- 新增仓库都位于 `references/repos/`。
- 调研文档中能追溯到来源仓库与本地路径。

验收证据：

- `references/repos/happy-claude-skills`
- `references/repos/byheaven-skills`
- `references/repos/alirezarezvani-claude-skills`

### 3.2 候选 skill 横向比较

需要围绕以下维度做比较：

- 长文写作能力
- 多平台原生改写能力
- 中文自媒体适配度
- 平台发布自动化能力
- 可移植性与是否过度绑定宿主工具
- 适合直接 adopt、局部 adapt，还是仅作参考

成功标志：

- 至少覆盖 5 个以上具体 skill。
- 每个 skill 都有清晰定位，而不是只贴链接。
- 对小红书、公众号、多平台内容分发分别给出结论。

验收证据：

- `nanospec/20260319-内容写作平台skills调研/assets/research/候选skills调研.md`

### 3.3 结论与建议

需要给出面向当前仓库的建议，包括：

- 哪些 skill 值得优先吸收方法论；
- 哪些更适合作为平台适配层；
- 哪些虽然能用，但不适合原样引入当前仓库。

成功标志：

- 有明确的推荐分层，而不是平均用力。
- 能区分“写作 skill”和“发布 / 自动化 skill”。
- 能说明哪些判断是直接来源于文件，哪些是基于文件内容做出的推断。

验收证据：

- `nanospec/20260319-内容写作平台skills调研/outputs/summary.md`

### 3.4 NanoSpec 工作记录

本轮研究过程需要完整落在 NanoSpec 任务目录下，便于后续继续扩展或吸收成 package。

成功标志：

- `brief.md`、`outputs/1-spec.md`、`outputs/2-plan.md`、`outputs/3-tasks.md` 完整。
- 最终有可读的调研文档与总结。

验收证据：

- `nanospec/20260319-内容写作平台skills调研/brief.md`
- `nanospec/20260319-内容写作平台skills调研/outputs/1-spec.md`
- `nanospec/20260319-内容写作平台skills调研/outputs/2-plan.md`
- `nanospec/20260319-内容写作平台skills调研/outputs/3-tasks.md`
- `nanospec/20260319-内容写作平台skills调研/outputs/summary.md`

## 4. 非目标

- 不在本轮直接把候选 skill 改写成当前仓库正式 package。
- 不补做完整中文翻译或统一格式清洗。
- 不接入真实发布账号或跑自动化发布。
- 不对外部仓库做内容修改。

## 5. 约束

- 文档默认使用简体中文。
- 外部仓库只放在 `references/repos/` 作为参考输入。
- 若后续判断发生范围变化，需要先补 `alignment.md` 再扩展。
