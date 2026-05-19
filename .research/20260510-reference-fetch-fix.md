# 2026-05-10 reference 拉取修复研究

## 目标

- 让 `references/repos/*` 的日常上游拉取在自动化里更稳定
- 避免再次因为本地代理或 SSH 端口限制，导致整轮 translation 巡检被卡住

## 本地搜索结果

### 已有资产

- 仓库级脚本只有 [`scripts/sync_codex_targets.py`](/Users/xxih/workspace/ai-harness-zh/scripts/sync_codex_targets.py)
- reference 维护说明在：
  - [`references/README.md`](/Users/xxih/workspace/ai-harness-zh/references/README.md)
  - [`references/translations/README.md`](/Users/xxih/workspace/ai-harness-zh/references/translations/README.md)
- 现有研究记录：
  - [`/Users/xxih/workspace/ai-harness-zh/.research/20260509-ai-harness-zh-translation-sync.md`](/Users/xxih/workspace/ai-harness-zh/.research/20260509-ai-harness-zh-translation-sync.md)

### 运行环境证据

- 环境变量注入了代理：
  - `http_proxy=http://127.0.0.1:7897`
  - `https_proxy=http://127.0.0.1:7897`
  - `all_proxy=socks5h://127.0.0.1:7897`
- `git config` 没有设置 proxy，说明代理来自运行环境，而不是 git 仓库或全局配置
- `networksetup` / `scutil --proxy` 显示系统代理统一指向 `127.0.0.1:7897`
- 进程里存在 `Clash Verge` / `verge-mihomo`，确认 `7897` 是本机代理端口

### 参考仓库 remote 现状

- 大多数 `references/repos/*` 使用 `https://github.com/...`
- [`references/repos/agency-agents`](/Users/xxih/workspace/ai-harness-zh/references/repos/agency-agents) 的 `origin` 使用 `git@github.com:...`，单独受 SSH 22 端口限制

## 复现与验证

### 失败原因复现

- 在旧自动化环境中，HTTPS repo 会尝试连 `127.0.0.1:7897`，如果代理不可达，则报：
  - `Failed to connect to 127.0.0.1 port 7897`
- `agency-agents` 因为走 SSH，会报：
  - `ssh: connect to host github.com port 22: Operation not permitted`

### 修复动作验证

- 去代理直连 HTTPS：
  - `env -u http_proxy -u https_proxy -u all_proxy ... git -C references/repos/gstack fetch origin --prune`
  - 验证通过
- 对 GitHub SSH remote 临时改走 HTTPS，但不改本地 remote：
  - `git -c remote.origin.url=https://github.com/msitarzewski/agency-agents.git -C references/repos/agency-agents fetch origin --prune`
  - 验证通过

## 候选实现

1. 只改自动化 prompt，要求手工清 proxy
   - 缺点：不稳定，容易回归
2. 新增仓库级拉取脚本，默认去代理并对 GitHub SSH remote 做 HTTPS fallback
   - 优点：可复用、可验证、不污染用户本地 remote
3. 直接批量把所有 SSH remote 改成 HTTPS
   - 缺点：修改用户本地工作副本状态，副作用偏大

## 决策

- 结论：`adapt`
- 方案：新增 repo 级脚本，沿用当前 `references/repos/*` 目录组织，不碰 manifest 机制；只把“怎么稳定拉取 reference”工具化

## 计划改动

1. 新增 [`scripts/fetch_reference_repos.py`](/Users/xxih/workspace/ai-harness-zh/scripts/fetch_reference_repos.py)
2. 在 [`README.md`](/Users/xxih/workspace/ai-harness-zh/README.md)、[`references/README.md`](/Users/xxih/workspace/ai-harness-zh/references/README.md)、[`references/translations/README.md`](/Users/xxih/workspace/ai-harness-zh/references/translations/README.md) 里补用法
3. 本地执行脚本做一次真实验证
