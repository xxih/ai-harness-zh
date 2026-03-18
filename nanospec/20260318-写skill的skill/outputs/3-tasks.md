## 1. 已完成

验收条件：本次任务已经有可继续协作的 NanoSpec 工作面。

- [x] 1.1 创建 `nanospec/20260318-写skill的skill/` 任务骨架，并写入 `.nanospec/.current`。
- [x] 1.2 补充 `brief.md`，明确背景、目标与约束。
- [x] 1.3 产出 `outputs/1-spec.md`，明确交付范围、成功标志与非目标。
- [x] 1.4 产出 `outputs/2-plan.md`，明确“三源合成 + source 为真相来源 + target 同步”的实施方案。

## 2. 本轮执行

验收条件：创建 skill 的 source 资产经确认可用，且 Codex target 已同步。

- [x] 2.1 核对 `src/domains/asset-governance/skills/writing-skills/` 是否符合调研结论与当前仓库约束。
- [x] 2.2 修正 `writing-skills`，去掉把当前仓库内部目录结构写成默认前提的内容。
- [x] 2.3 同步 `targets/codex/skills/writing-skills/`。
- [x] 2.4 通过文件存在性与 source/target diff 做最小校验。

## 3. 本轮对齐修正

验收条件：当前任务记录与 skill 正文口径一致，不再冲突。

- [x] 3.1 执行 `/align`，记录“skill 默认应保持独立，不绑定当前仓库结构”的偏差。
- [x] 3.2 同步更新 `brief.md`、`outputs/1-spec.md`、`outputs/2-plan.md`。
- [x] 3.3 同步更新 `writing-skills` 正文与支撑 references。

## 4. 后续候选

验收条件：后续如果继续扩展 skill authoring 体系，有明确候选但不进入本轮范围。

- [ ] 4.1 视需要再补更通用的 skill authoring eval。
- [ ] 4.2 若后续出现更多平台差异，再为其他分发目标增加对应副本。

## 5. 其他 skill 对齐

验收条件：除 `nanospec` / `spec-driven` 这类本身定义任务容器的 skill 外，其它通用 skill 不再把当前仓库结构写成默认前提。

- [x] 5.1 扫描 `learning-capture`、`quality-*`、`search-first`、`agent-orchestration` 中的强绑定仓库表述。
- [x] 5.2 将默认落点改为通用文件名或“当前工作面”，去掉 `.learned/`、`.quality/`、`.research/`、`nanospec`、`src/...`、`targets/...` 等当前仓库前提。
- [x] 5.3 同步对应 `targets/codex/skills/` 分发副本。

## 6. 默认记录目录回调

验收条件：保留 `.research/`、`.quality/`、`.learned/` 作为分类默认落点，但不重新引入 `src/...`、`targets/...`、`nanospec` 等强绑定实现细节。

- [x] 6.1 执行 `/align`，记录“默认记录目录不该一并去掉”的修正。
- [x] 6.2 恢复 `learning-capture` 的 `.learned/` 默认落点。
- [x] 6.3 恢复 `quality-*` 的 `.quality/quality-check.md` 默认落点。
- [x] 6.4 恢复 `search-first` 与 `agent-orchestration` 的 `.research/` 默认落点。
