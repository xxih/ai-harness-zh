# superpowers 中文翻译

## 当前范围

- 源仓库：`references/repos/superpowers`
- 当前先覆盖：`skills/*/SKILL.md`
- 暂不覆盖：
  - `skills/*/references/*`
  - `skills/*/*-prompt.md`
  - `agents/`、`commands/`、`hooks/` 等其他目录

## 同步规则

维护 `superpowers` 中文翻译前：

1. 先更新 `references/repos/superpowers/` 到准备对照的 upstream 版本
2. 查看 upstream commit 是否变化
3. 查看哪些 `skills/*/SKILL.md` 发生了内容漂移
4. 同步修改本目录下对应中文文件
5. 手动更新 `references/translations/superpowers/manifest.json`

## 说明

- 中文翻译尽量保持 prompt 约束、流程顺序和强弱语气一致
- skill 名称、路径、命令、代码块和协议关键字保持原文
- 如果某段更适合保留英文原文（例如命令示例、路径、占位符），优先保留原文
