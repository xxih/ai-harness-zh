# 翻译质量评审记录

## 范围

- 审查对象：`references/translations/**`
- 审查方式：
  - 校验全部 `manifest.json` 的译文文件存在性、源文件存在性与 `source_sha256`
  - 检查 `scope.include` 对应范围是否兑现
  - 对高风险条目做人工抽查

## Strengths

- 除 `oh-my-opencode` 外，所有已登记翻译条目的 `source_sha256` 都能和当前基线源文件对上。
- `agency-agents`、`superpowers`、`get-shit-done` 当前声明覆盖范围内未发现漏登记或缺文件。
- `gstack` 的大量结构差异有文档说明，属于“结构化中文译要”策略，不应按逐段直译标准误判。

## Issues

### Minor

- `references/translations/oh-my-opencode/manifest.json`
  - 已统一改为仅指向仓库内 `references/repos/oh-my-opencode`。
  - 当前 `README.zh-cn.md` 被明确记录为“现成中文参考稿”，不再伪装成某一版 `README.md` 的严格逐段镜像；后续若要恢复哈希级追踪，需要先把这份中文 README 重新按 canonical README 审阅一遍。
- `references/translations/README.md`
  - 总览页对 `agency-agents` 的描述仍是“`strategy/EXECUTIVE-BRIEF.md`、`strategy/QUICKSTART.md` 与若干 `integrations/*/README.md` 首批译稿”。
  - 但当前实际已覆盖完整 integrations 总览与全部工具 README，这里已经落后于现状。

## Assessment

- 结论：`not-ready`
- 原因：
  - scoped 翻译内容本身整体质量可接受，未发现大面积漏段或漏文件。
  - `oh-my-opencode` 的基线错位已修正，但总览说明仍有滞后项，且 `README.zh-cn.md` 还没有恢复到可做哈希级逐段追踪的状态。

## 建议动作

1. 更新 `references/translations/README.md` 中对 `agency-agents` 覆盖范围的总览说明。
2. 若后续想恢复 `oh-my-opencode/README.zh-cn.md` 的哈希级追踪，先基于 `references/repos/oh-my-opencode/README.md` 重新审阅并决定是重翻、补注释，还是继续保留为参考稿。
