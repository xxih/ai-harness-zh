**语言：** English | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md)

# Everything Claude Code

[![Stars](https://img.shields.io/github/stars/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/stargazers)
[![Forks](https://img.shields.io/github/forks/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/network/members)
[![Contributors](https://img.shields.io/github/contributors/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/graphs/contributors)
[![npm ecc-universal](https://img.shields.io/npm/dw/ecc-universal?label=ecc-universal%20weekly%20downloads&logo=npm)](https://www.npmjs.com/package/ecc-universal)
[![npm ecc-agentshield](https://img.shields.io/npm/dw/ecc-agentshield?label=ecc-agentshield%20weekly%20downloads&logo=npm)](https://www.npmjs.com/package/ecc-agentshield)
[![GitHub App Install](https://img.shields.io/badge/GitHub%20App-150%20installs-2ea44f?logo=github)](https://github.com/marketplace/ecc-tools)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnu-bash&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?logo=go&logoColor=white)
![Java](https://img.shields.io/badge/-Java-ED8B00?logo=openjdk&logoColor=white)
![Perl](https://img.shields.io/badge/-Perl-39457E?logo=perl&logoColor=white)
![Markdown](https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white)

> **50K+ stars** | **6K+ forks** | **30 contributors** | **7 languages supported** | **Anthropic Hackathon Winner**

---

<div align="center">

**🌐 Language / 语言 / 語言 / Dil**

[**English**](README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md)

</div>

---

**适用于 AI 智能体平台的性能优化系统。来自 Anthropic 黑客马拉松获胜者。**

不只是配置，而是一整套系统：skills、instincts、记忆优化、持续学习、安全扫描，以及 research-first 开发。这里沉淀的是经过 10 多个月高频真实产品开发演化出的生产级 agents、hooks、commands、rules 和 MCP 配置。

适用于 **Claude Code**、**Codex**、**Cowork** 以及其他 AI 智能体平台。

---

## 指南

这个仓库只包含原始代码，完整方法论请看配套指南。

<table>
<tr>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2012378465664745795">
<img src="./assets/images/guides/shorthand-guide.png" alt="Everything Claude Code 速记指南" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2014040193557471352">
<img src="./assets/images/guides/longform-guide.png" alt="Everything Claude Code 详细指南" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2033263813387223421">
<img src="./assets/images/security/security-guide-header.png" alt="Everything Agentic Security 速记指南" />
</a>
</td>
</tr>
<tr>
<td align="center"><b>Shorthand Guide</b><br/>安装、基础与理念。<b>建议先读。</b></td>
<td align="center"><b>Longform Guide</b><br/>令牌优化、记忆持久化、评估与并行化。</td>
<td align="center"><b>Security Guide</b><br/>攻击面、沙箱、净化、CVE 与 AgentShield。</td>
</tr>
</table>

| 主题 | 你将学到什么 |
|-------|-------------------|
| Token 优化 | 模型选择、系统提示精简、后台进程 |
| 记忆持久化 | 自动在会话间保存/加载上下文的 hooks |
| 持续学习 | 从会话中自动提取模式并沉淀为可复用 skills |
| 验证循环 | checkpoint 与 continuous eval、grader 类型、pass@k 指标 |
| 并行化 | Git worktree、级联方法、何时扩展实例 |
| 子代理编排 | 上下文问题与迭代检索模式 |

---

## 最新动态

### v1.9.0 — 选择性安装与语言扩展（2026 年 3 月）

- **选择性安装架构**：基于 manifest 的安装流水线，引入 `install-plan.js` 与 `install-apply.js`，支持按组件定向安装，并通过状态仓跟踪已安装内容。
- **6 个新 agent**：`typescript-reviewer`、`pytorch-build-resolver`、`java-build-resolver`、`java-reviewer`、`kotlin-reviewer`、`kotlin-build-resolver`，将语言覆盖扩展到 10 种。
- **一批新 skills**：包括 `pytorch-patterns`、`documentation-lookup`、`bun-runtime`、`nextjs-turbopack`、8 个运营类 skills，以及 `mcp-server-patterns`。
- **会话与状态基础设施**：新增 SQLite state store、query CLI、session adapters，以及面向自我改进 skill 的演化基础。
- **编排能力增强**：`harness-audit` 评分改为确定性，编排状态与 launcher 兼容性加强，observer 循环加入 5 层防护。
- **Observer 稳定性提升**：修复内存膨胀，引入节流与 tail sampling，补齐沙箱访问、lazy-start 与重入保护。
- **12 个语言生态**：新增 Java、PHP、Perl、Kotlin/Android/KMP、C++、Rust 规则，与既有 TypeScript、Python、Go 及 common 规则并列。
- **社区贡献扩展**：包括韩文与中文翻译、安全 hook、biome hook 优化、视频处理 skills、运营类 skills、PowerShell 安装器与 Antigravity IDE 支持。
- **CI 加固**：修复 19 个测试失败，补上 catalog 计数校验、安装 manifest 校验，并让全量测试重新转绿。

### v1.8.0 — 平台性能系统（2026 年 3 月）

- **平台优先发布**：ECC 被明确定位为 AI 智能体平台性能系统，而不只是配置集合。
- **Hook 可靠性重构**：加入 SessionStart 根目录回退、Stop 阶段会话摘要，以及以脚本替代脆弱单行 hook。
- **Hook 运行时控制**：支持 `ECC_HOOK_PROFILE=minimal|standard|strict` 和 `ECC_DISABLED_HOOKS=...`，无需改文件即可临时门控。
- **新增平台命令**：`/harness-audit`、`/loop-start`、`/loop-status`、`/quality-gate`、`/model-route`。
- **NanoClaw v2**：模型路由、skill 热加载、会话分支/搜索/导出/压缩/指标。
- **跨平台一致性增强**：Claude Code、Cursor、OpenCode 和 Codex app/CLI 的行为进一步收敛。
- **997 项内部测试通过**：hook/runtime 重构与兼容性调整后，全套测试恢复为绿色。

### v1.7.0 — 跨平台扩展与演示文稿生成器（2026 年 2 月）

- **Codex 应用 + CLI 支持**：通过 `AGENTS.md` 直接支持 Codex，并补充安装器目标与 Codex 文档。
- **`frontend-slides` skill**：零依赖 HTML 幻灯片生成器，附带 PPTX 转换指导与严格视口适配规则。
- **5 个通用业务/内容 skills**：`article-writing`、`content-engine`、`market-research`、`investor-materials`、`investor-outreach`。
- **更广泛的工具覆盖**：进一步增强对 Cursor、Codex 与 OpenCode 的支持。
- **992 项内部测试**：扩展了对插件、hooks、skills 与打包层的验证与回归覆盖。

### v1.6.0 — Codex CLI、AgentShield 与 Marketplace（2026 年 2 月）

- **Codex CLI 支持**：新增 `/codex-setup`，生成适配 OpenAI Codex CLI 的 `codex.md`。
- **7 个新 skills**：`search-first`、`swift-actor-persistence`、`swift-protocol-di-testing`、`regex-vs-llm-structured-text`、`content-hash-cache-pattern`、`cost-aware-llm-pipeline`、`skill-stocktake`。
- **AgentShield 集成**：`/security-scan` 可直接在 Claude Code 中运行 AgentShield；当时测试数为 1282，规则数为 102。
- **GitHub Marketplace**：ECC Tools GitHub App 已上线 <https://github.com/marketplace/ecc-tools>。
- **30+ 社区 PR 合并**：来自 30 位贡献者，覆盖 6 种语言。
- **978 项内部测试**：扩展 agents、skills、commands、hooks 与 rules 的验证套件。

完整变更日志请参见 [Releases](https://github.com/affaan-m/everything-claude-code/releases)。

---

## 🚀 快速开始

2 分钟内上手：

### 第 1 步：安装插件

```bash
# 添加 marketplace
/plugin marketplace add affaan-m/everything-claude-code

# 安装插件
/plugin install everything-claude-code@everything-claude-code
```

### 第 2 步：安装规则（必需）

> ⚠️ **重要：** Claude Code 插件无法自动分发 `rules`，需要手动安装。

```bash
# 先克隆仓库
git clone https://github.com/affaan-m/everything-claude-code.git
cd everything-claude-code

# 安装依赖（任选一种包管理器）
npm install        # 或 pnpm install | yarn install | bun install

# macOS/Linux
./install.sh typescript    # 或 python / golang / swift / php
# ./install.sh typescript python golang swift php
# ./install.sh --target cursor typescript
# ./install.sh --target antigravity typescript
```

```powershell
# Windows PowerShell
.\install.ps1 typescript   # 或 python / golang / swift / php
# .\install.ps1 typescript python golang swift php
# .\install.ps1 --target cursor typescript
# .\install.ps1 --target antigravity typescript

# 通过 npm 安装时，也可使用跨平台入口
npx ecc-install typescript
```

手动安装说明请查看 `rules/README.md`。

### 第 3 步：开始使用

```bash
# 尝试一个命令（插件安装使用带命名空间的形式）
/everything-claude-code:plan "Add user authentication"

# 手动安装（Option 2）时可使用短形式：
# /plan "Add user authentication"

# 查看可用命令
/plugin list everything-claude-code@everything-claude-code
```

✨ **完成。** 现在可使用 28 个 agents、119 个 skills 和 60 个 commands。

---

## 🌐 跨平台支持

现在已完整支持 **Windows、macOS 和 Linux**，并与 Cursor、OpenCode、Antigravity 等主流 IDE 以及 CLI 平台保持紧密集成。所有 hooks 与脚本都已改写为 Node.js，以提高跨平台兼容性。

### 包管理器检测

插件会按以下优先级自动检测你偏好的包管理器（npm、pnpm、yarn、bun）：

1. **环境变量**：`CLAUDE_PACKAGE_MANAGER`
2. **项目配置**：`.claude/package-manager.json`
3. **package.json**：`packageManager` 字段
4. **锁文件**：`package-lock.json`、`yarn.lock`、`pnpm-lock.yaml`、`bun.lockb`
5. **全局配置**：`~/.claude/package-manager.json`
6. **回退**：第一个可用的包管理器

设置方式如下：

```bash
# 通过环境变量
export CLAUDE_PACKAGE_MANAGER=pnpm

# 通过全局配置
node scripts/setup-package-manager.js --global pnpm

# 通过项目配置
node scripts/setup-package-manager.js --project bun

# 检测当前设置
node scripts/setup-package-manager.js --detect
```

也可以直接使用 Claude Code 中的 `/setup-pm`。

### Hook 运行时控制

你可以通过运行时标志临时调整严格度或禁用指定 hooks：

```bash
# Hook 严格度配置（默认：standard）
export ECC_HOOK_PROFILE=standard

# 用逗号分隔要禁用的 hook ID
export ECC_DISABLED_HOOKS="pre:bash:tmux-reminder,post:edit:typecheck"
```

---

## 📦 里面有什么

这个仓库是一个 **Claude Code 插件** - 直接安装或手动复制组件。

```
everything-claude-code/
|-- .claude-plugin/   # 插件和市场清单
|   |-- plugin.json         # 插件元数据和组件路径
|   |-- marketplace.json    # /plugin marketplace add 的市场目录
|
|-- agents/           # 用于委托的专业子代理
|   |-- planner.md           # 功能实现规划
|   |-- architect.md         # 系统设计决策
|   |-- tdd-guide.md         # 测试驱动开发
|   |-- code-reviewer.md     # 质量和安全审查
|   |-- security-reviewer.md # 漏洞分析
|   |-- build-error-resolver.md
|   |-- e2e-runner.md        # Playwright E2E 测试
|   |-- refactor-cleaner.md  # 死代码清理
|   |-- doc-updater.md       # 文档同步
|   |-- go-reviewer.md       # Go 代码审查（新增）
|   |-- go-build-resolver.md # Go 构建错误解决（新增）
|
|-- skills/           # 工作流定义和领域知识
|   |-- coding-standards/           # 语言最佳实践
|   |-- backend-patterns/           # API、数据库、缓存模式
|   |-- frontend-patterns/          # React、Next.js 模式
|   |-- continuous-learning/        # 从会话中自动提取模式（详细指南）
|   |-- continuous-learning-v2/     # 基于直觉的学习与置信度评分
|   |-- iterative-retrieval/        # 子代理的渐进式上下文细化
|   |-- strategic-compact/          # 手动压缩建议（详细指南）
|   |-- tdd-workflow/               # TDD 方法论
|   |-- security-review/            # 安全检查清单
|   |-- eval-harness/               # 验证循环评估（详细指南）
|   |-- verification-loop/          # 持续验证（详细指南）
|   |-- golang-patterns/            # Go 惯用语和最佳实践（新增）
|   |-- golang-testing/             # Go 测试模式、TDD、基准测试（新增）
|   |-- cpp-testing/                # C++ 测试模式、GoogleTest、CMake/CTest（新增）
|   |-- perl-patterns/             # 现代 Perl 5.36+ 惯用语和最佳实践（新增）
|   |-- perl-security/             # Perl 安全模式、污染模式、安全 I/O（新增）
|   |-- perl-testing/              # 使用 Test2::V0、prove、Devel::Cover 的 Perl TDD（新增）
|
|-- commands/         # 用于快速执行的斜杠命令
|   |-- tdd.md              # /tdd - 测试驱动开发
|   |-- plan.md             # /plan - 实现规划
|   |-- e2e.md              # /e2e - E2E 测试生成
|   |-- code-review.md      # /code-review - 质量审查
|   |-- build-fix.md        # /build-fix - 修复构建错误
|   |-- refactor-clean.md   # /refactor-clean - 死代码移除
|   |-- learn.md            # /learn - 会话中提取模式（详细指南）
|   |-- checkpoint.md       # /checkpoint - 保存验证状态（详细指南）
|   |-- verify.md           # /verify - 运行验证循环（详细指南）
|   |-- setup-pm.md         # /setup-pm - 配置包管理器
|   |-- go-review.md        # /go-review - Go 代码审查（新增）
|   |-- go-test.md          # /go-test - Go TDD 工作流（新增）
|   |-- go-build.md         # /go-build - 修复 Go 构建错误（新增）
|   |-- skill-create.md     # /skill-create - 从 git 历史生成技能（新增）
|   |-- instinct-status.md  # /instinct-status - 查看学习的直觉（新增）
|   |-- instinct-import.md  # /instinct-import - 导入直觉（新增）
|   |-- instinct-export.md  # /instinct-export - 导出直觉（新增）
|   |-- evolve.md           # /evolve - 将直觉聚类到技能中（新增）
|
|-- rules/            # 始终遵循的指南（复制到 ~/.claude/rules/）
|   |-- README.md            # 结构概述和安装指南
|   |-- common/              # 与语言无关的原则
|   |   |-- coding-style.md    # 不可变性、文件组织
|   |   |-- git-workflow.md    # 提交格式、PR 流程
|   |   |-- testing.md         # TDD、80% 覆盖率要求
|   |   |-- performance.md     # 模型选择、上下文管理
|   |   |-- patterns.md        # 设计模式、骨架项目
|   |   |-- hooks.md           # 钩子架构、TodoWrite
|   |   |-- agents.md          # 何时委托给子代理
|   |   |-- security.md        # 强制性安全检查
|   |-- typescript/          # TypeScript/JavaScript 特定
|   |-- python/              # Python 特定
|   |-- golang/              # Go 特定
|   |-- perl/                # Perl 特定（新增）
|
|-- hooks/            # 基于触发器的自动化
|   |-- hooks.json                # 所有钩子配置（PreToolUse、PostToolUse、Stop 等）
|   |-- memory-persistence/       # 会话生命周期钩子（详细指南）
|   |-- strategic-compact/        # 压缩建议（详细指南）
|
|-- scripts/          # 跨平台 Node.js 脚本（新增）
|   |-- lib/                     # 共享工具
|   |   |-- utils.js             # 跨平台文件/路径/系统工具
|   |   |-- package-manager.js   # 包管理器检测和选择
|   |-- hooks/                   # 钩子实现
|   |   |-- session-start.js     # 会话开始时加载上下文
|   |   |-- session-end.js       # 会话结束时保存状态
|   |   |-- pre-compact.js       # 压缩前状态保存
|   |   |-- suggest-compact.js   # 战略性压缩建议
|   |   |-- evaluate-session.js  # 从会话中提取模式
|   |-- setup-package-manager.js # 交互式 PM 设置
|
|-- tests/            # 测试套件（新增）
|   |-- lib/                     # 库测试
|   |-- hooks/                   # 钩子测试
|   |-- run-all.js               # 运行所有测试
|
|-- contexts/         # 动态系统提示注入上下文（详细指南）
|   |-- dev.md              # 开发模式上下文
|   |-- review.md           # 代码审查模式上下文
|   |-- research.md         # 研究/探索模式上下文
|
|-- examples/         # 示例配置和会话
|   |-- CLAUDE.md           # 示例项目级配置
|   |-- user-CLAUDE.md      # 示例用户级配置
|
|-- mcp-configs/      # MCP 服务器配置
|   |-- mcp-servers.json    # GitHub、Supabase、Vercel、Railway 等
|
|-- marketplace.json  # 自托管市场配置（用于 /plugin marketplace add）
```

---

## 🛠️ 生态系统工具

### 技能创建器

两种从你的仓库生成 Claude Code 技能的方法：

#### 选项 A：本地分析（内置）

使用 `/skill-create` 命令进行本地分析，无需外部服务：

```bash
/skill-create                    # 分析当前仓库
/skill-create --instincts        # 还为 continuous-learning 生成直觉
```

这在本地分析你的 git 历史并生成 SKILL.md 文件。

#### 选项 B：GitHub 应用（高级）

用于高级功能（10k+ 提交、自动 PR、团队共享）：

[安装 GitHub 应用](https://github.com/apps/skill-creator) | [ecc.tools](https://ecc.tools)

```bash
# 在任何问题上评论：
/skill-creator analyze

# 或在推送到默认分支时自动触发
```

两个选项都创建：
- **SKILL.md 文件** - 可直接用于 Claude Code 的技能
- **直觉集合** - 用于 continuous-learning-v2
- **模式提取** - 从你的提交历史中学习

### 🧠 持续学习 v2

基于直觉的学习系统自动学习你的模式：

```bash
/instinct-status        # 显示带有置信度的学习直觉
/instinct-import <file> # 从他人导入直觉
/instinct-export        # 导出你的直觉以供分享
/evolve                 # 将相关直觉聚类到技能中
/promote                # 将项目级直觉提升为全局直觉
/projects               # 查看已识别项目与直觉统计
```

完整文档见 `skills/continuous-learning-v2/`。

---

## 📥 安装

### 选项 1：作为插件安装（推荐）

使用此仓库的最简单方法 - 作为 Claude Code 插件安装：

```bash
# 将此仓库添加为市场
/plugin marketplace add affaan-m/everything-claude-code

# 安装插件
/plugin install everything-claude-code@everything-claude-code
```

或直接添加到你的 `~/.claude/settings.json`：

```json
{
  "extraKnownMarketplaces": {
    "everything-claude-code": {
      "source": {
        "source": "github",
        "repo": "affaan-m/everything-claude-code"
      }
    }
  },
  "enabledPlugins": {
    "everything-claude-code@everything-claude-code": true
  }
}
```

这让你可以立即访问所有命令、代理、技能和钩子。

> **注意：** Claude Code 插件系统不支持通过插件分发 `rules`（[上游限制](https://code.claude.com/docs/en/plugins-reference)）。你需要手动安装规则：
>
> ```bash
> # 首先克隆仓库
> git clone https://github.com/affaan-m/everything-claude-code.git
>
> # 选项 A：用户级规则（应用于所有项目）
> cp -r everything-claude-code/rules/* ~/.claude/rules/
>
> # 选项 B：项目级规则（仅应用于当前项目）
> mkdir -p .claude/rules
> cp -r everything-claude-code/rules/* .claude/rules/
> ```

---

### 🔧 选项 2：手动安装

如果你希望对安装的内容进行手动控制：

```bash
# 克隆仓库
git clone https://github.com/affaan-m/everything-claude-code.git

# 将代理复制到你的 Claude 配置
cp everything-claude-code/agents/*.md ~/.claude/agents/

# 复制规则（通用 + 语言特定）
cp -r everything-claude-code/rules/common/* ~/.claude/rules/
cp -r everything-claude-code/rules/typescript/* ~/.claude/rules/   # 选择你的技术栈
cp -r everything-claude-code/rules/python/* ~/.claude/rules/
cp -r everything-claude-code/rules/golang/* ~/.claude/rules/
cp -r everything-claude-code/rules/perl/* ~/.claude/rules/

# 复制命令
cp everything-claude-code/commands/*.md ~/.claude/commands/

# 复制技能
cp -r everything-claude-code/skills/* ~/.claude/skills/
```

#### 将钩子添加到 settings.json

将 `hooks/hooks.json` 中的钩子复制到你的 `~/.claude/settings.json`。

#### 配置 MCP

将所需的 MCP 服务器从 `mcp-configs/mcp-servers.json` 复制到你的 `~/.claude.json`。

**重要：** 将 `YOUR_*_HERE` 占位符替换为你的实际 API 密钥。

---

## 🎯 关键概念

### 代理

子代理以有限范围处理委托的任务。示例：

```markdown
---
name: code-reviewer
description: 审查代码的质量、安全性和可维护性
tools: ["Read", "Grep", "Glob", "Bash"]
model: opus
---

你是一名高级代码审查员...
```

### 技能

技能是由命令或代理调用的工作流定义：

```markdown
# TDD 工作流

1. 首先定义接口
2. 编写失败的测试（RED）
3. 实现最少的代码（GREEN）
4. 重构（IMPROVE）
5. 验证 80%+ 的覆盖率
```

### 钩子

钩子在工具事件时触发。示例 - 警告 console.log：

```json
{
  "matcher": "tool == \"Edit\" && tool_input.file_path matches \"\\\\.(ts|tsx|js|jsx)$\"",
  "hooks": [{
    "type": "command",
    "command": "#!/bin/bash\ngrep -n 'console\\.log' \"$file_path\" && echo '[Hook] 移除 console.log' >&2"
  }]
}
```

### 规则

规则是始终遵循的指南，分为 `common/`（通用）+ 语言特定目录：

```
~/.claude/rules/
  common/          # 通用原则（必装）
  typescript/      # TS/JS 特定模式和工具
  python/          # Python 特定模式和工具
  golang/          # Go 特定模式和工具
  perl/            # Perl 特定模式和工具
```

---

## 🧪 运行测试

插件包含一个全面的测试套件：

```bash
# 运行所有测试
node tests/run-all.js

# 运行单个测试文件
node tests/lib/utils.test.js
node tests/lib/package-manager.test.js
node tests/hooks/hooks.test.js
```

---

## 🤝 贡献

**欢迎并鼓励贡献。**

这个仓库旨在成为社区资源。如果你有：
- 有用的代理或技能
- 聪明的钩子
- 更好的 MCP 配置
- 改进的规则

请贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解指南。

### 贡献想法

- 特定语言的技能（Rust、C#、Kotlin、Java）- 现已包含 Go、Python、Perl、Swift 和 TypeScript！
- 特定框架的配置（Django、Rails、Laravel）
- DevOps 代理（Kubernetes、Terraform、AWS）
- 测试策略（不同框架）
- 特定领域的知识（ML、数据工程、移动）

---

## 📖 背景

自实验性推出以来，我一直在使用 Claude Code。2025 年 9 月，与 [@DRodriguezFX](https://x.com/DRodriguezFX) 一起使用 Claude Code 构建 [zenith.chat](https://zenith.chat)，赢得了 Anthropic x Forum Ventures 黑客马拉松。

这些配置在多个生产应用中经过了实战测试。

---

## ⚠️ 重要说明

### 上下文窗口管理

**关键：** 不要一次启用所有 MCP。如果启用了太多工具，你的 200k 上下文窗口可能会缩小到 70k。

经验法则：
- 配置 20-30 个 MCP
- 每个项目保持启用少于 10 个
- 活动工具少于 80 个

在项目配置中使用 `disabledMcpServers` 来禁用未使用的。

### 定制化

这些配置适用于我的工作流。你应该：
1. 从适合你的开始
2. 为你的技术栈进行修改
3. 删除你不使用的
4. 添加你自己的模式

---

## 🌟 Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=affaan-m/everything-claude-code&type=Date)](https://star-history.com/#affaan-m/everything-claude-code&Date)

---

## 🔗 链接

- **精简指南（从这里开始）：** [The Shorthand Guide to Everything Claude Code](https://x.com/affaanmustafa/status/2012378465664745795)
- **详细指南（高级）：** [The Longform Guide to Everything Claude Code](https://x.com/affaanmustafa/status/2014040193557471352)
- **关注：** [@affaanmustafa](https://x.com/affaanmustafa)
- **zenith.chat:** [zenith.chat](https://zenith.chat)
- **技能目录：** awesome-agent-skills（社区维护的智能体技能目录）

---

## 📄 许可证

MIT - 自由使用，根据需要修改，如果可以请回馈。

---

**如果这个仓库有帮助，请给它一个 Star。阅读两个指南。构建一些很棒的东西。**
