# 写作内核 skill 第一版

## 背景

承接 `nanospec/20260319-内容写作平台skills调研/` 的结论：`article-writing` 适合作为长文写作内核，`content-engine` 适合作为多平台改写层，公众号 / 小红书相关能力更适合作为平台适配层。

用户希望先开一个新任务，先做一版平台无关的“写作内核” skill，基本沿用 `article-writing` 的骨架，但要把边界拆清楚：当前 skill 覆盖什么、不覆盖什么，外部其他 skill 又分别覆盖什么。

## 目标

1. 产出一个第一版通用写作 skill，默认放进正式 package。
2. 明确这个 skill 只负责写作内核，不混入平台发布与运营动作。
3. 形成一份“内容生产骨架”拆解文档，帮助用户判断后续优化方向。

## 约束

1. 仓库资产遵循 package-first，正式 skill 优先放进 `packages/<package>/`。
2. 仓库文档默认使用简体中文，代码、路径、API 名称保持原文。
3. 本轮先 `adapt` `article-writing`，不追求一步到位整合所有内容生产链路。
4. 结构性变更后，要同步更新相关 README。
