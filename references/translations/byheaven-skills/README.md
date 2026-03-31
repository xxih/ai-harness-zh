# byheaven-skills 中文收录

## 当前范围

- 源仓库：`references/repos/byheaven-skills`
- 当前覆盖：
  - `README.md` -> `README.zh-CN.md`
  - `plugins/newproject/README.md` -> `plugins/newproject/README.zh-CN.md`
  - `plugins/newproject/skills/newproject/SKILL.md`
  - `plugins/xhs-publisher/README.md`
  - `plugins/xhs-publisher/skills/xhs-publisher/SKILL.md`
- 暂不覆盖：
  - `assets/` 下的模板、workflow、脚本与图标
  - `.claude-plugin/plugin.json`、CI 配置与其他非核心 prompt 资产

## 收录口径

- `README.zh-CN.md` 直接收录 upstream 自带中文 README，作为仓库级中文入口
- `newproject` 当前由本仓库补中文 README 与中文 SKILL，便于后续按英文源文件做 diff 同步
- `xhs-publisher` 的 README 与 SKILL 源文件本身已经是中文，这里按“中文核心 prompt 资产”镜像收录，方便统一检索和对照

## 后续同步建议

1. 先更新 `references/repos/byheaven-skills` 到准备对照的 upstream 版本
2. 检查 `README.md`、`plugins/newproject/README.md`、`plugins/newproject/skills/newproject/SKILL.md` 是否发生变化
3. 若 `xhs-publisher` 的中文原文有变化，也同步更新这里的镜像版本
4. 同步完成后更新 `manifest.json` 中的 `head_commit` 与各条目的 `source_sha256`
