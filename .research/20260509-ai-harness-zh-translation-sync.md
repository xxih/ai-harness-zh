# 2026-05-09 ai-harness-zh 翻译巡检

## 目标

- 拉取 `references/repos/*` 中各 reference 仓库的 `main/master`
- 对照 `references/translations/*/manifest.json` 检查当前翻译覆盖情况
- 补齐本地已存在缺口的中文译稿

## 研究过程

### 本地清单与约定

- 已读取 [`references/translations/README.md`](/Users/xxih/workspace/ai-harness-zh/references/translations/README.md)
- 已读取 `gstack` 的 [`manifest.json`](/Users/xxih/workspace/ai-harness-zh/references/translations/gstack/manifest.json)
- 已核对 `references/repos/*` 中可用 reference repo 与当前分支

### 外部同步阻塞

- 试跑：`git -C references/repos/gstack fetch origin main master --prune`
- 结果：失败，错误为 `Failed to connect to 127.0.0.1 port 7897`
- 结论：当前运行环境无法访问 GitHub，今天不能完成真正的 upstream 拉取，只能基于本地已有副本做审阅

### 差异筛查结果

- `gstack` 目录下已有一批新增中文稿与 manifest/README 变更：
  - `docs/ADDING_A_HOST.md`
  - `docs/OPENCLAW.md`
  - `docs/REMOTE_BROWSER_ACCESS.md`
  - `openclaw/agents-gstack-section.md`
  - `openclaw/gstack-full-CLAUDE.md`
  - `openclaw/gstack-lite-CLAUDE.md`
  - `openclaw/gstack-plan-CLAUDE.md`
- 已验证上述 7 个新条目都已写入 [`references/translations/gstack/manifest.json`](/Users/xxih/workspace/ai-harness-zh/references/translations/gstack/manifest.json)，且 `source_sha256` 与当前本地 `references/repos/gstack` 中对应源文件一致
- 已抽查新增中文稿完整性，确认不是半成品；`OPENCLAW` 与 remote browser 两份长文档的末尾章节齐全

### 其他仓库说明

- `get-shit-done` / `oh-my-opencode` 的 manifest 里存在 `source: null` 或“中文稿本身作为参考资产”的条目，不能用简单 glob 缺口判断直接扩面
- `gstack` 中大量旧条目的 `source_sha256` 与当前本地源码不一致，但 `head_commit` 又与本地 `HEAD` 相同；这更像历史 hash 记录口径不一致，今天没有足够证据去整体重刷 manifest

## 决策

- `adopt`：沿用现有 `manifest.json + README.md + 镜像路径` 组织方式
- `adapt`：本轮只确认并承接 `gstack` 已经落地的新增翻译，不扩面修历史 hash
- `keep-task-local`：把 fetch 阻塞和 hash 口径问题先留在本任务记录与 automation memory，不升级为仓库级规则

## 下一步

1. 在可联网环境下重新执行各 repo 的 `git fetch`
2. 优先确认 `gstack` 旧条目的 hash 生成口径，再决定是否整份重刷 manifest
3. 若上游确实有新提交，再按 manifest scope 逐仓补译
