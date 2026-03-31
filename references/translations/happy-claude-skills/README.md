# happy-claude-skills 中文翻译

## 当前范围

- 源仓库：`references/repos/happy-claude-skills`
- 当前覆盖：
  - `README.md` -> `README.zh-CN.md`
  - `skills/browser/SKILL.md`
  - `skills/docx-format-replicator/SKILL.md`
  - `skills/docx-format-replicator/references/content_data_schema.md`
  - `skills/docx-format-replicator/references/format_config_schema.md`
  - `skills/video-processor/SKILL.md`
  - `skills/wechat-article-writer/SKILL.md`
- 暂不覆盖：
  - `skills/*/scripts/**`
  - `skills/docx-format-replicator/assets/**`
  - `LICENSE`、`.claude-plugin/**`、`package.json` 等非核心 prompt 资产

## 收录口径

- 仓库级中文入口以 `README.md` 为基线翻译，输出为 `README.zh-CN.md`
- 源仓库虽自带 `README.zh-CN.md`，但当前内容未完整覆盖 `README.md` 中的技能清单与说明，因此本目录单独维护一份对齐 `README.md` 的中文译本
- `wechat-article-writer/SKILL.md` 源文件本身已经是中文，这里按“中文核心 prompt 资产”镜像收录，方便统一检索和后续 diff 同步
- 当前 checkout 的 `README.md` 提到了 `trends-bulletin`，但仓库里未见对应 `SKILL.md`；因此这里只翻译仓库级说明，不额外补写不存在的 skill 文档

## 后续同步建议

1. 先更新 `references/repos/happy-claude-skills` 到准备对照的 upstream 版本
2. 检查 `README.md` 与当前已覆盖的 `skills/**.md` 是否发生变化
3. 若 upstream 新增 `trends-bulletin` 等核心 prompt 文档，再决定是否扩充本目录覆盖范围
4. 同步完成后更新 `manifest.json` 中的 `head_commit` 与各条目的 `source_sha256`
