# claudeception 中文翻译

## 当前范围

- 源仓库：`references/repos/claudeception`
- 当前覆盖：
  - `README.md` -> `README.zh-CN.md`
  - `SKILL.md`
  - `WARP.md`
  - `resources/skill-template.md`
  - `resources/research-references.md`
  - `examples/*/SKILL.md`
- 暂不覆盖：
  - `scripts/`、测试配置与其他非核心 prompt 资产

## 翻译口径

- 优先覆盖可直接理解 Claudeception 工作方式的核心 prompt 资产
- 保持 skill 名称、路径、命令、代码块、工具名和协议关键字原文不变
- 中文翻译尽量保留原文的约束强度、流程顺序和触发条件
- 示例中的精确报错、搜索词和 URL 以原文为准，避免失去可检索性

## 后续同步建议

1. 先更新 `references/repos/claudeception` 到准备对照的 upstream 版本
2. 检查本目录当前覆盖范围内的源文件哈希是否变化
3. 如有漂移，优先同步 `SKILL.md`、`WARP.md`、模板、研究说明和示例 skill
4. 同步完成后更新 `manifest.json` 中的 `head_commit` 与 `source_sha256`
