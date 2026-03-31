# alirezarezvani-claude-skills 中文翻译

## 当前范围

- 源仓库：`references/repos/alirezarezvani-claude-skills`
- 当前覆盖：
  - `README.md` -> `README.zh-CN.md`
  - `CLAUDE.md`
  - `GEMINI.md`
  - `agents/CLAUDE.md`
  - `standards/CLAUDE.md`
  - `templates/CLAUDE.md`
  - `orchestration/ORCHESTRATION.md`
  - `business-growth/SKILL.md`
  - `business-growth/CLAUDE.md`
  - `c-level-advisor/SKILL.md`
  - `c-level-advisor/CLAUDE.md`
  - `engineering-team/CLAUDE.md`
  - `engineering/SKILL.md`
  - `finance/SKILL.md`
  - `finance/CLAUDE.md`
  - `marketing-skill/SKILL.md`
  - `marketing-skill/CLAUDE.md`
  - `product-team/SKILL.md`
  - `product-team/CLAUDE.md`
  - `project-management/SKILL.md`
  - `project-management/CLAUDE.md`
  - `ra-qm-team/SKILL.md`
  - `ra-qm-team/CLAUDE.md`
  - `custom-gpt/README.md`
- 暂不覆盖：
  - 大多数各 domain 下更深层的 `README.md`
  - 具体 skill 子目录中的 `SKILL.md`
  - `agents/`、`commands/`、`standards/`、`templates/` 与各类 `scripts/`、`references/`、`assets/`

## 翻译口径

- 先覆盖仓库级入口与顶层核心 prompt 资产，方便快速理解该仓库的组织方式和主入口
- skill 名称、路径、命令、代码块、工具名、产品名与协议关键字保持原文
- frontmatter 中面向读者的说明文案翻译为中文，标识型字段如 `name`、`tags`、agent 标识保持原文
- 尽量保留原文的约束强度、流程顺序、命令示例和目录结构

## 后续同步建议

1. 先更新 `references/repos/alirezarezvani-claude-skills` 到准备对照的 upstream 版本
2. 检查当前已覆盖源文件的哈希是否变化
3. 如有漂移，优先同步仓库级入口文件与顶层 domain `SKILL.md`
4. 若后续要继续扩展，可按 domain 逐步补子目录 skill，而不是一次性整仓翻译
5. 同步完成后更新 `manifest.json` 中的 `head_commit` 与 `source_sha256`
