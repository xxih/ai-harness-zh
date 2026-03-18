# Codex 常用 MCP Server 调研与安装指南

*更新日期：2026-03-14*

本文调研了 6 个在 Codex 工作流里最常见的 MCP server：

- GitHub
- Context7
- Exa
- Memory
- Playwright
- Sequential Thinking

重点回答 4 个问题：

1. 这东西是做什么的
2. 在 Codex 里怎么装
3. 什么时候值得开
4. 它的限制、风险和我的评价是什么

说明：

- 文中的 shell 命令默认面向 macOS / Linux 的 `bash` 或 `zsh`
- Windows 需要换成等价的环境变量写法
- 凭证建议通过环境变量、客户端 secret store 或 `codex mcp add` 注入
- 不建议把 PAT、API key 直接写进可提交的 `config.toml`

## 先看结论

如果你想先做一套实用、稳定、不太吵的 Codex MCP 组合，我的建议是：

- 常驻开启：`Context7`、`Memory`
- 高价值按需开启：`Exa`、`GitHub`、`Playwright`
- 需要时再开：`Sequential Thinking`

如果你主要是写代码而不是做外部研究，优先级通常是：

1. `Context7`
2. `Memory`
3. `GitHub`
4. `Playwright`
5. `Exa`
6. `Sequential Thinking`

如果你经常做资料搜集、公司研究、新闻跟踪，优先级通常是：

1. `Exa`
2. `Context7`
3. `GitHub`
4. `Memory`
5. `Playwright`
6. `Sequential Thinking`

## 一张表看完

| MCP Server | 主要作用 | 推荐安装方式 | 是否需要凭证 | 是否建议常开 | 我的评价 |
|---|---|---|---|---|---|
| GitHub | 读写 issue/PR/repo、查 CI、看代码 | 官方 GitHub MCP Server | 通常需要 GitHub 认证 | 按需 | 很强，但权限高，适合明确的 GitHub 工作流 |
| Context7 | 查最新库文档和代码示例 | Remote 或本地 `npx` | 推荐 API Key | 是 | 开发型 MCP 里性价比最高之一 |
| Exa | 网页搜索、代码搜索、公司/人物研究 | 官方 Remote | 可无 key，建议有 | 按需 | 很强，但更重、更广 |
| Memory | 跨任务记忆、实体关系存储 | 本地 `npx` | 不需要 | 是 | 简单有效，适合长期工作流 |
| Playwright | 浏览器自动化、页面抓取、表单操作 | 本地 `npx` | 不需要 | 按需 | 对真实网页调试很值，但权限和开销都高 |
| Sequential Thinking | 结构化思考、分步推理 | 本地 `npx` | 不需要 | 否 | 对复杂分析有用，但不该每题都开 |

## 1. GitHub MCP Server

### 它是做什么的

GitHub MCP Server 让 agent 直接访问 GitHub 资源和操作，包括：

- 读取和搜索仓库内容
- 查看和评论 issue / pull request
- 查看 CI、checks、reviews、diff
- 在有权限时创建分支、提交文件、发起 PR

它适合“GitHub 是工作中心”的开发流程，而不是单纯的本地写码。

### 官方安装方式

GitHub 官方目前主推的是 `github/github-mcp-server`，并且单独给出了 OpenAI Codex 的安装说明。

#### 方式 A：用 `codex mcp add` 添加

```bash
codex mcp add github -- env GITHUB_PERSONAL_ACCESS_TOKEN=YOUR_GITHUB_PAT npx -y github-mcp-server
```

如果你希望在启动前先把 token 放进环境变量，也可以用：

```bash
export GITHUB_PERSONAL_ACCESS_TOKEN=YOUR_GITHUB_PAT
codex mcp add github -- npx -y github-mcp-server
```

#### 方式 B：固定到本机 Codex 配置

GitHub 官方文档重点给的是 `codex mcp add` 方式。  
如果你想把它固定到 `~/.codex/config.toml`，更稳妥的做法是：

- 先用 `codex mcp add` 生成或注册
- 凭证通过启动前环境变量注入
- 不要把 PAT 直接写进 `config.toml`

### 认证与权限

GitHub 官方文档要求使用 PAT 或 GitHub App 等认证方式。最常见的是 `GITHUB_PERSONAL_ACCESS_TOKEN`。

这类 server 的风险不在“能不能搜”，而在“它真的能写”。如果 token scope 给大了，它就能：

- 改 issue
- 改 PR
- 推分支
- 改文件

所以建议：

- 优先用最小权限 token
- 不要在所有项目都常开
- 只在明确需要 GitHub 操作时启用

### 什么时候最值

- 你要 review PR、查 CI 失败、看 issue 上下文
- 你要自动化处理 GitHub 流程，而不是只读本地代码
- 你经常在 agent 里做“查仓库状态 -> 提修改 -> 发 PR”闭环

### 限制与风险

- 权限高，安全边界比纯搜索工具敏感得多
- 依赖 GitHub 认证和网络
- 它解决的是“平台操作”，不是“库文档准确性”

### 我的评价

这是一个典型的“高价值，但不建议无脑常开”的 MCP。

如果你的工作流高度依赖 GitHub，它非常值；如果你主要是在本地仓库里改代码，它的优先级没有 Context7 和 Memory 高。

### 参考来源

- GitHub 官方仓库：https://github.com/github/github-mcp-server
- GitHub 官方安装文档（OpenAI Codex）：https://docs.github.com/en/copilot/how-tos/context/model-context-protocol/using-the-github-mcp-server

## 2. Context7 MCP

### 它是做什么的

Context7 的定位非常明确：给 AI 提供“最新、按版本区分的库文档和代码示例”。

它不是全网搜索引擎，而是“库文档检索器”。核心流程通常是：

1. 先把库名解析成 Context7 的 library ID
2. 再按库和版本查询文档内容

它特别适合解决这类问题：

- “这个库在 2026 年现在的 API 是什么样？”
- “Next.js / React / Supabase 这个版本到底怎么配？”
- “我不想让模型凭记忆乱写第三方库用法”

### 官方安装方式

Context7 官方同时支持 Remote 和本地 `npx` 安装。

#### 方式 A：Remote MCP

```toml
[mcp_servers.context7]
url = "https://mcp.context7.com/mcp"
```

#### 方式 B：本地 `npx`

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp@latest"]
```

如果你要启用更高限额或 private repositories，按 Context7 官方文档把 API key 注入到客户端认证配置里；不要把真实 key 直接写进仓库文件。

官方排障文档说明本地模式通常要求：

- `Node.js v18+`
- 某些环境需要显式加 `@latest`

### 认证要求

Context7 官方说 API Key 是“推荐”而不是“绝对必须”，但有 key 会更稳，因为：

- rate limit 更高
- 能访问更多资源
- 支持 private repositories 等场景

### 什么时候最值

- 你主要在写代码、修 bug、看框架文档
- 你很在意“官方文档优先”和“版本准确”
- 你希望降低第三方库 API 幻觉

### 限制与风险

- 它不擅长新闻、人物、公司、市场研究
- 本地模式要依赖 Node 环境
- 官方明确提示存在速率限制
- 官方也写了免责声明：文档来源并非全部完全开源和完全保证准确

### 我的评价

如果只选一个“开发型 MCP”，我通常会先选 Context7。

它的优点是：

- 噪声低
- 回答更聚焦
- 对写代码的直接收益很高

这是我最推荐常驻开启的 MCP 之一。

### 参考来源

- 官方安装总览：https://context7.com/docs/installation
- API Keys：https://context7.com/docs/howto/api-keys
- 排障说明：https://context7.com/docs/resources/troubleshooting
- 官方仓库：https://github.com/upstash/context7

## 3. Exa MCP

### 它是做什么的

Exa MCP 是一个更“研究型”的工具集。官方能力覆盖：

- web search
- code search
- company research
- people search
- deep research

如果说 Context7 是“窄而深”的文档工具，Exa 更像“宽而强”的搜索与研究底座。

### 官方安装方式

Exa 官方主推 Remote MCP。

#### 方式 A：官方 Remote

```bash
codex mcp add exa --url https://mcp.exa.ai/mcp
```

或者按 Codex 当前配置格式写进 `~/.codex/config.toml`：

```toml
[mcp_servers.exa]
url = "https://mcp.exa.ai/mcp"
```

#### 方式 B：本地 `npx`

```toml
[mcp_servers.exa]
command = "npx"
args = ["-y", "exa-mcp-server"]
```

如果你要带自己的 key，通常使用环境变量：

```bash
export EXA_API_KEY=YOUR_EXA_API_KEY
```

### 认证要求

Exa 官方说明：

- 不带 key 也可以开始用
- 遇到免费额度限制、`429` 或想用更完整能力时，建议带上自己的 key
- 某些高级能力明确要求 key，例如更深入的 research 能力

### 什么时候最值

- 你要查最新网页信息
- 你要找代码例子和外部技术资料
- 你要做公司、融资、竞争对手、人物背景研究
- 你要让 agent 做“先搜，再抓全文，再总结”

### 限制与风险

- 它依赖第三方远程服务，隐私暴露面高于纯本地工具
- 工具比较多，MCP 描述会消耗上下文
- 对“只写代码、不做外部研究”的项目来说，它可能太宽

### 我的评价

Exa 很强，但它不是“越早装越好”，而是“你有研究需求时特别值”。

如果你经常做下面这些事，它的价值会很高：

- 调研新技术
- 追踪最新变化
- 查公司、产品、人物
- 做带来源的研究报告

如果你的工作主要是本地开发，Exa 更适合作为按需启用，而不是默认常开。

### 参考来源

- 官方文档：https://exa.ai/docs/reference/exa-mcp
- 产品页：https://exa.ai/mcp
- 官方仓库：https://github.com/exa-labs/exa-mcp-server

## 4. Memory MCP

### 它是做什么的

Memory MCP 是一个“长期记忆层”。它不是搜索引擎，也不是浏览器，而是把信息组织成：

- 实体
- 观察
- 关系

你可以把它理解成“可查询的知识图谱记忆”，适合跨任务保留稳定上下文。

它典型适合记录：

- 用户偏好
- 项目结构认知
- 长期约定
- 实体关系，例如“某仓库属于某团队”“某服务依赖某数据库”

### 安装方式

官方参考实现是 `@modelcontextprotocol/server-memory`。

下面这段不是 Memory 官方单独发布的 Codex 安装页，而是基于 MCP 参考实现和 Codex 当前 stdio 配置方式整理出的可用写法：

```toml
[mcp_servers.memory]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-memory"]
```

这是一个本地 stdio server，不需要远程托管地址，也通常不需要额外凭证。

### 认证与存储

官方 README 说明它是基于本地图存储的记忆 server。默认更适合单人、本机、长期使用，而不是多用户共享系统。

### 什么时候最值

- 你希望 agent 记住长期偏好
- 你在多个回合里持续维护同一个项目或同一批项目
- 你不想把稳定背景每次都重讲一遍

### 限制与风险

- 它不是事实真相系统，而是“被写入什么，就记住什么”
- 如果写入质量差，会积累噪声
- 更适合稳定信息，不适合高频变化事实

### 我的评价

Memory 的价值不在“单次任务立刻变强”，而在“长期使用越久越值”。

如果你经常做连续项目，它值得常开，而且通常是低风险、低噪声的那类 MCP。

### 参考来源

- 官方参考服务器仓库：https://github.com/modelcontextprotocol/servers
- npm 包：https://www.npmjs.com/package/@modelcontextprotocol/server-memory

## 5. Playwright MCP

### 它是做什么的

Playwright MCP 把真实浏览器自动化能力暴露给 agent。它能做的不是“看文档”，而是“真的去打开网页并操作”。

典型能力包括：

- 导航到页面
- 点击、输入、选择
- 截图
- 获取页面快照
- 抓网络请求
- 用浏览器调试真实 UI 流程

### 官方安装方式

Playwright 官方仓库给了面向 Codex 的安装示例。

#### 方式 A：直接添加

```bash
codex mcp add playwright -- npx @playwright/mcp@latest
```

#### 方式 B：写入 `~/.codex/config.toml`

```toml
[mcp_servers.playwright]
command = "npx"
args = ["@playwright/mcp@latest"]
```

ECC 这份仓库里的示例还额外带了 `--extension`：

```toml
[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@latest", "--extension"]
```

如果你只是想先跑起来，先用官方最小安装即可。

### 认证与依赖

它通常不需要 API key，但依赖本机浏览器能力和 Node 环境。

如果本机环境不完整，第一次运行时可能还要补浏览器相关依赖。

### 什么时候最值

- 你要复现前端 bug
- 你要走真实登录、表单、点击流程
- 你要抓页面状态、网络请求或截图
- 你要让 agent“看见页面现在到底什么样”

### 限制与风险

- 它会真的操作页面，所以权限和副作用比纯搜索工具高
- 运行成本更高，也更容易受环境影响
- 并不适合所有任务；纯后端或纯文档任务通常没必要带着它

### 我的评价

Playwright MCP 非常值，但它是“重工具”。

对前端调试、E2E、网页采集类任务，它的价值极高；对普通代码问答，它没有必要常驻开启。

### 参考来源

- 官方仓库：https://github.com/microsoft/playwright-mcp

## 6. Sequential Thinking MCP

### 它是做什么的

Sequential Thinking 是 MCP 官方参考服务器之一。它不是外部世界工具，而是“思考过程工具”。

它的作用是让 agent 以更显式的方式进行：

- 分步分析
- 方案修正
- 分支探索
- 假设与验证

它更适合复杂问题分解，而不是事实查询。

### 安装方式

官方参考实现是 `@modelcontextprotocol/server-sequential-thinking`。

下面这段不是 Sequential Thinking 官方单独发布的 Codex 安装页，而是基于 MCP 参考实现和 Codex 当前 stdio 配置方式整理出的可用写法：

```toml
[mcp_servers.sequential-thinking]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-sequential-thinking"]
```

### 什么时候最值

- 问题复杂、路径不明确
- 要做多步设计、架构权衡、问题分解
- 你希望模型显式修正之前的思路

### 限制与风险

- 它不增加事实来源
- 它也不代替文档、搜索、浏览器、GitHub 操作
- 如果每个小问题都开，会显得过度设计

### 我的评价

这是一个“复杂题增益明显、简单题容易过度使用”的 MCP。

我建议把它当成备用工具，而不是默认常驻工具。

### 参考来源

- 官方参考服务器仓库：https://github.com/modelcontextprotocol/servers
- npm 包：https://www.npmjs.com/package/@modelcontextprotocol/server-sequential-thinking

## 安装建议：给 Codex 的一套实用配置

如果你想先配一套“稳定、实用、不夸张”的组合，我建议这样开始。

下面是“适合写进配置文件的无密钥部分”；涉及 PAT 或 API key 的认证，建议在启动 Codex 前通过环境变量或 `codex mcp add` 完成，不要硬编码进 TOML：

```toml
[mcp_servers.context7]
url = "https://mcp.context7.com/mcp"

[mcp_servers.memory]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-memory"]
```

如果你已经在外部环境里注入了 GitHub 凭证，再补：

```toml
[mcp_servers.github]
command = "npx"
args = ["-y", "github-mcp-server"]
```

然后按需再加：

```toml
[mcp_servers.exa]
url = "https://mcp.exa.ai/mcp"

[mcp_servers.playwright]
command = "npx"
args = ["@playwright/mcp@latest"]

[mcp_servers.sequential-thinking]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-sequential-thinking"]
```

## 最后的建议

### 如果你主要写代码

- 先装 `Context7`
- 再装 `Memory`
- 如果 GitHub 流程很多，再装 `GitHub`
- 如果经常调前端和网页，再装 `Playwright`
- `Exa` 和 `Sequential Thinking` 放到后面

### 如果你主要做研究

- 先装 `Exa`
- 再装 `Context7`
- 需要平台操作时再加 `GitHub`
- `Memory` 负责长期上下文

### 如果你担心上下文被工具描述吃掉

ECC 自己的 README 也明确提醒：MCP 不要一次全开。启用的 server 越多，工具描述越多，模型上下文就越被占用。

因此最稳的策略不是“全装全开”，而是：

- 常驻保留 2 到 4 个高频工具
- 其余按项目或按任务启用

## 参考资料汇总

- GitHub MCP Server 官方仓库：https://github.com/github/github-mcp-server
- GitHub 官方文档（含 OpenAI Codex）：https://docs.github.com/en/copilot/how-tos/context/model-context-protocol/using-the-github-mcp-server
- Context7 安装文档：https://context7.com/docs/installation
- Context7 API Keys：https://context7.com/docs/howto/api-keys
- Context7 排障文档：https://context7.com/docs/resources/troubleshooting
- Context7 官方仓库：https://github.com/upstash/context7
- Exa MCP 文档：https://exa.ai/docs/reference/exa-mcp
- Exa MCP 产品页：https://exa.ai/mcp
- Exa MCP 官方仓库：https://github.com/exa-labs/exa-mcp-server
- MCP 官方参考服务器仓库：https://github.com/modelcontextprotocol/servers
- Memory npm 包：https://www.npmjs.com/package/@modelcontextprotocol/server-memory
- Sequential Thinking npm 包：https://www.npmjs.com/package/@modelcontextprotocol/server-sequential-thinking
- Playwright MCP 官方仓库：https://github.com/microsoft/playwright-mcp
- ECC 本仓库关于 MCP 数量的提醒：[README.md](../../README.md)
