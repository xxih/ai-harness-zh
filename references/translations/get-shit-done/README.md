# get-shit-done 中文翻译

## 当前范围

- 源仓库：`references/repos/get-shit-done`
- 当前覆盖：
  - `README.md` -> `README.zh-CN.md`
  - `docs/README.md` -> `docs/zh-CN/README.md`
  - `docs/USER-GUIDE.md` -> `docs/zh-CN/USER-GUIDE.md`
  - `docs/references/*.md` -> `docs/zh-CN/references/*.md`
  - `docs/COMMANDS.md` -> `docs/zh-CN/COMMANDS.md`
  - `docs/AGENTS.md` -> `docs/zh-CN/AGENTS.md`
- 其中：
  - `README.zh-CN.md` 与 `docs/zh-CN/**` 先回收 upstream 已提供的中文版本
  - `docs/zh-CN/COMMANDS.md` 与 `docs/zh-CN/AGENTS.md` 为当前仓库补翻
- 暂不覆盖：
  - `agents/*.md`
  - `commands/gsd/*.md`
  - `docs/ARCHITECTURE.md`、`docs/FEATURES.md`、`docs/CONFIGURATION.md`、`docs/CLI-TOOLS.md`
  - `sdk/`、`hooks/`、测试与其他非核心 prompt / 说明资产

## 翻译口径

- 优先覆盖理解 GSD 工作方式、命令面和 agent 体系所需的核心入口文档
- 命令名、路径、flag、代码块、协议关键字、工具名与模型名保持原文
- 中文尽量保留原文的约束强度、流程顺序与前置条件
- 对 `workstream`、`Nyquist`、`UAT` 等已有专有名词，优先保留英文或英文缩写，避免失去检索性

## 后续同步建议

1. 先更新 `references/repos/get-shit-done` 到准备对照的 upstream 版本
2. 检查当前覆盖范围内的源文件哈希是否变化
3. 优先同步 `README.md`、`docs/README.md`、`docs/USER-GUIDE.md`、`docs/references/*.md`、`docs/COMMANDS.md` 与 `docs/AGENTS.md`
4. 若 upstream 新增中文版本，优先回收上游译稿；若未提供，再由本仓库补翻
5. 同步完成后更新 `manifest.json` 中的 `head_commit` 与 `source_sha256`
