## 1. NanoSpec 工作面

验收条件：当前任务目标、范围与约束明确，且已承接上一轮结论。

- [x] 1.1 创建 `nanospec/20260319-写作内核skill第一版/` 任务骨架，并写入 `.nanospec/.current`。
- [x] 1.2 补充 `brief.md`，明确背景、目标与约束。
- [x] 1.3 产出 `outputs/1-spec.md`。
- [x] 1.4 产出 `outputs/2-plan.md`。

## 2. 第一版 skill 落地

验收条件：仓库内存在一个正式 package，且 skill 边界清楚、平台无关。

- [x] 2.1 新增 `packages/content-writing/README.md`。
- [x] 2.2 新增 `packages/content-writing/skills/content-writing/SKILL.md`。
- [x] 2.3 新增 `packages/content-writing/targets/codex/README.md`。
- [x] 2.4 运行 `python3 scripts/sync_codex_targets.py content-writing`，同步 Codex target 副本。

## 3. 内容生产骨架拆解

验收条件：有一份结构化文档能看出覆盖边界、空缺层与参考来源。

- [x] 3.1 产出 `assets/research/写作内核skill拆解.md`。
- [x] 3.2 明确第一版 skill 覆盖 / 不覆盖项。
- [x] 3.3 明确其他参考 skill 的补位关系。
- [x] 3.4 提出后续可选优化方向。

## 4. 仓库说明同步

验收条件：结构变更已同步到仓库说明文档。

- [x] 4.1 更新 `README.md`。
- [x] 4.2 更新 `packages/README.md`。

## 5. 收口

验收条件：本轮有简洁总结，且任务状态回写完整。

- [x] 5.1 产出 `outputs/summary.md`。
- [x] 5.2 回写本轮完成状态到 `outputs/3-tasks.md`。
