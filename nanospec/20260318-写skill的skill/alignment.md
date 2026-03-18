# 对齐记录：写skill的skill

## 2026-03-18

- [偏差] 初版把“创建 skill 的 skill”误写成依赖当前仓库内部结构的资产，正文混入了 `src/domains/...`、`targets/...`、`nanospec`、仓库记录目录等内容；这与用户要求的“skill 默认应保持独立，最终用于分发给他人导入 AI 工具使用”不一致。
  - 处理决定：把 `writing-skills` 改回“独立 skill 包优先”的口径。正文默认只描述独立 `SKILL.md` 与可选 `references/`、`scripts/`、`assets/`，不再把当前仓库的领域分层、任务容器、记录目录或 target 目录写成默认前提。
  - 影响范围：`brief.md`、`outputs/1-spec.md`、`outputs/2-plan.md`、`outputs/3-tasks.md`、`src/domains/asset-governance/skills/writing-skills/` 及对应分发副本。

- [变更] 用户进一步要求继续扫描仓库内其他 skill，把已写过的强绑定仓库表述一并对齐。
  - 处理决定：对通用 skill 去掉 `.learned/`、`.quality/`、`.research/`、`nanospec`、`src/...`、`targets/...`、`commands/` 等当前仓库前提，改为“回写当前工作面”或“使用通用文件名”的表述；`nanospec` 与 `spec-driven` 这类本身就定义任务容器的 skill 保持原样。
  - 影响范围：`learning-capture`、`quality-*`、`search-first`、`agent-orchestration` 及对应分发副本。
