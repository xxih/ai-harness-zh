# 2026-05-19 ai-harness-zh 翻译巡检

## 目标

- 拉取 `references/repos/*` 中各 reference 仓库的 `main/master`
- 检查 `references/translations/*/manifest.json` 与本地翻译覆盖情况
- 对可确认的缺漏补齐中文翻译资产

## 研究过程

### 上游拉取结果

- 执行：`python3 scripts/fetch_reference_repos.py`
- 结果：11 个 reference repo 全部拉取失败
- 共同错误：`Could not resolve host: github.com`
- 结论：本轮运行环境仍无法解析 GitHub，不能宣称“已拉取最新 upstream”

### 本地审计结果

- 执行：`python3 scripts/audit_reference_translations.py`
- 结果：11 份 manifest 全部通过，没有已纳入范围内的漏翻、缺文件或 `source_sha256` 漂移
- 结论：当前缺口不在既有 scope 内，而在 `openspec` 翻译范围仍偏窄

### 缺口判断

- `references/translations/openspec/` 昨日仅覆盖 `README.zh-CN.md`
- 结合上游 `README.md` 的一级文档导航，`docs/commands.md` 与 `docs/workflows.md` 是最明确的高频入口
- 这两份文档分别承接 slash commands 参考与 workflow 模式说明，适合作为 README 之后的第二层中文入口

## 决策

- 结论：`adapt`
- 原因：
  - 仓库内已经有 `manifest.json + README.md + audit 脚本` 这套稳定维护机制，直接扩展 `openspec` scope 即可
  - 在 fetch 失败的前提下，基于本地快照补最明显的高价值入口，风险可控
  - `commands/workflows` 比继续下探实现文档更符合“核心 prompt / workflow 资产”的筛选口径

## 本轮改动

- 新增 `references/translations/openspec/docs/commands.md`
- 新增 `references/translations/openspec/docs/workflows.md`
- 更新 `references/translations/openspec/manifest.json`
- 更新 `references/translations/openspec/README.md`
- 更新 `references/translations/README.md`

## 验证

- `python3 scripts/fetch_reference_repos.py`
  - exit code: `1`
  - 结论：DNS 阻塞，无法获取最新 upstream
- `python3 scripts/audit_reference_translations.py openspec`
  - 结论：`openspec` manifest 通过，新增两份文档已被纳入正式审计
- `python3 scripts/audit_reference_translations.py`
  - 结论：11 份 manifest 全部 `OK`

## 下一步

1. 下轮优先重试 `python3 scripts/fetch_reference_repos.py`
2. 若网络恢复，再基于最新 upstream 判断 `openspec` 是否继续扩到 `docs/getting-started.md`、`docs/customization.md` 或其他一级导航文档
3. 若网络仍不可达，继续沿用本地快照做增量审计
