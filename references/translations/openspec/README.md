# OpenSpec 中文翻译

## 当前范围

- 源仓库：`references/repos/openspec`
- 当前覆盖：
  - `README.md` -> `README.zh-CN.md`
  - `docs/commands.md` -> `docs/commands.md`
  - `docs/workflows.md` -> `docs/workflows.md`
- 暂不覆盖：
  - `AGENTS.md`
  - 其他 `docs/*.md`
  - `openspec/**`、`src/**`、`scripts/**` 等实现与运行时目录
  - `CHANGELOG.md`、`MAINTAINERS.md`、`WORKSPACE_REIMPLEMENTATION_*.md` 等非首批入口材料

## 仓库导读

`OpenSpec` 是一套面向 AI coding workflow 的 spec framework。它通过 `openspec init`、`openspec update` 和一组 `/opsx:*` 命令，把 proposal、spec、design、tasks 等工件固定进项目目录，让“先对齐需求、再开始实现”成为可重复流程。

当前这一批中文资产先覆盖仓库级 `README.md` 与两份高频入口文档，目的有两点：

- 先把 OpenSpec 的定位、核心 workflow、slash commands 心智模型和文档导航纳入当前仓库的中文参考集
- 先建立 `manifest.json` 与同步口径；后续若需要继续收录 `docs/getting-started.md`、`docs/customization.md` 或 `AGENTS.md`，可以在现有基础上扩面

## 同步规则

维护 `OpenSpec` 中文翻译前：

1. 先更新 `references/repos/openspec/` 到准备对照的 upstream 版本
2. 记录最新 upstream commit
3. 检查 `README.md`、`docs/commands.md`、`docs/workflows.md` 是否发生内容变化
4. 如有变化，手动同步对应中文译稿
5. 同步完成后，更新 `references/translations/openspec/manifest.json`

## 翻译原则

- 中文尽量保留原文的产品语气、workflow 顺序和命令心智模型
- 命令、路径、包名、slash command、文件树名称与协议关键字保持原文
- 徽标、badge、图片和外链保持原始链接，避免引入额外维护成本
