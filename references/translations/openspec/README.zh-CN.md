<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec">
    <picture>
      <source srcset="assets/openspec_bg.png">
      <img src="assets/openspec_bg.png" alt="OpenSpec logo">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml/badge.svg" /></a>
  <a href="https://www.npmjs.com/package/@fission-ai/openspec"><img alt="npm version" src="https://img.shields.io/npm/v/@fission-ai/openspec?style=flat-square" /></a>
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" /></a>
  <a href="https://discord.gg/YctCnvvshC"><img alt="Discord" src="https://img.shields.io/discord/1411657095639601154?style=flat-square&logo=discord&logoColor=white&label=Discord&suffix=%20online" /></a>
</p>

<details>
<summary><strong>最受欢迎的 spec framework 之一。</strong></summary>

[![Stars](https://img.shields.io/github/stars/Fission-AI/OpenSpec?style=flat-square&label=Stars)](https://github.com/Fission-AI/OpenSpec/stargazers)
[![Downloads](https://img.shields.io/npm/dm/@fission-ai/openspec?style=flat-square&label=Downloads/mo)](https://www.npmjs.com/package/@fission-ai/openspec)
[![Contributors](https://img.shields.io/github/contributors/Fission-AI/OpenSpec?style=flat-square&label=Contributors)](https://github.com/Fission-AI/OpenSpec/graphs/contributors)

</details>
<p></p>
我们的理念：

```text
→ 灵活而非僵硬
→ 迭代而非瀑布
→ 简单而非复杂
→ 不只适合 greenfield，也为 brownfield 而生
→ 从个人项目到企业团队都能扩展
```

> [!TIP]
> **新的 workflow 已上线！** 我们用新的 artifact-guided workflow 重建了 OpenSpec。
>
> 运行 `/opsx:propose "your idea"` 开始。→ [点击这里了解更多](docs/opsx.md)

<p align="center">
  关注 <a href="https://x.com/0xTab">@0xTab</a> 获取更新 · 加入 <a href="https://discord.gg/YctCnvvshC">OpenSpec Discord</a> 获取帮助并提问。
</p>

<!-- TODO: Add GIF demo of /opsx:propose → /opsx:archive workflow -->

## 实战演示

```text
你：/opsx:propose add-dark-mode
AI：已创建 openspec/changes/add-dark-mode/
    ✓ proposal.md — 为什么要做、将变更什么
    ✓ specs/       — 需求与场景
    ✓ design.md    — 技术方案
    ✓ tasks.md     — 实现清单
    已准备进入实现！

你：/opsx:apply
AI：正在执行任务...
    ✓ 1.1 添加主题上下文 provider
    ✓ 1.2 创建切换组件
    ✓ 2.1 添加 CSS variables
    ✓ 2.2 接入 localStorage
    所有任务完成！

你：/opsx:archive
AI：已归档到 openspec/changes/archive/2025-01-23-add-dark-mode/
    Specs 已更新。可以开始下一个功能了。
```

<details>
<summary><strong>OpenSpec Dashboard</strong></summary>

<p align="center">
  <img src="assets/openspec_dashboard.png" alt="OpenSpec dashboard preview" width="90%">
</p>

</details>

## 快速开始

**需要 Node.js 20.19.0 或更高版本。**

全局安装 OpenSpec：

```bash
npm install -g @fission-ai/openspec@latest
```

然后进入你的项目目录并初始化：

```bash
cd your-project
openspec init
```

接下来告诉你的 AI：`/opsx:propose <what-you-want-to-build>`

如果你想启用扩展 workflow（`/opsx:new`、`/opsx:continue`、`/opsx:ff`、`/opsx:verify`、`/opsx:bulk-archive`、`/opsx:onboard`），使用 `openspec config profile` 选择它，再运行 `openspec update` 应用。

> [!NOTE]
> 不确定你的工具是否受支持？[查看完整列表](docs/supported-tools.md) ，目前已支持 25+ 工具，并且还在持续增加。
>
> 也支持 pnpm、yarn、bun 和 nix。参见[安装选项](docs/installation.md)。

## 文档

→ **[Getting Started](docs/getting-started.md)**：第一步怎么走<br>
→ **[Workflows](docs/workflows.md)**：组合方式与使用模式<br>
→ **[Commands](docs/commands.md)**：slash commands 与 skills<br>
→ **[CLI](docs/cli.md)**：终端参考手册<br>
→ **[Supported Tools](docs/supported-tools.md)**：工具集成与安装路径<br>
→ **[Concepts](docs/concepts.md)**：整体理念如何拼起来<br>
→ **[Multi-Language](docs/multi-language.md)**：多语言支持<br>
→ **[Customization](docs/customization.md)**：按你的方式自定义

## 社区 schema

通过独立仓库分发的第三方 schema bundle。这些 bundle 会提供带有明确风格的 workflow，把 OpenSpec 与其他工具集成起来，类似 [github/spec-kit's community extension catalog](https://github.com/github/spec-kit/tree/main/extensions) 的扩展方式。

→ **[浏览目录](docs/customization.md#community-schemas)**：见 customization 文档中的社区 schema 列表。

## 为什么是 OpenSpec？

当需求只存在于聊天记录里时，AI coding assistant 虽然强大，但也容易失控。OpenSpec 增加了一层轻量 spec，让你在任何代码写下去之前，先对“要构建什么”达成一致。

- **先对齐，再开工**：人在写代码前先和 AI 在 spec 上对齐
- **保持条理**：每次变更都有自己的 proposal、specs、design 和 tasks 目录
- **灵活推进**：任何工件都可以随时更新，不依赖僵硬的 phase gate
- **沿用你的工具**：通过 slash commands 兼容 20+ AI assistants

### 对比方式

**vs. [Spec Kit](https://github.com/github/spec-kit)**（GitHub）: 体系完整，但偏重。它有更刚性的 phase gate、大量 Markdown 和 Python setup；OpenSpec 更轻，也允许你更自由地迭代。

**vs. [Kiro](https://kiro.dev)**（AWS）: 功能强，但你被锁在他们的 IDE 里，而且主要受限于 Claude models；OpenSpec 可以直接跑在你已经在用的工具上。

**vs. 什么都不用**: 没有 spec 的 AI coding 往往意味着 prompt 模糊、结果不可预测。OpenSpec 用更低的仪式成本换来更高的可预测性。

## 更新 OpenSpec

**升级包**

```bash
npm install -g @fission-ai/openspec@latest
```

**刷新 agent 指令**

在每个项目目录里运行下面的命令，重新生成 AI 指导文件，并确保最新的 slash commands 已经生效：

```bash
openspec update
```

## 使用说明

**模型选择**：OpenSpec 更适合高推理模型。我们推荐在规划和实现两个阶段都使用 Opus 4.5 与 GPT 5.2。

**上下文卫生**：OpenSpec 依赖干净的上下文窗口。开始实现前先清理上下文，并在整个会话中持续维护良好的 context hygiene。

## 贡献

**小改动**：Bug 修复、typo 更正和小型改进，可以直接提交 PR。

**大改动**：新功能、较大重构或架构级变更，建议先提交 OpenSpec change proposal，再开始实现，这样可以先对意图和目标达成一致。

写 proposal 时，请记住 OpenSpec 的理念：它服务的是广泛的用户、不同的 coding agents、不同的模型和多样化的使用场景。变更应该对所有人都工作良好。

**欢迎 AI 生成代码**：前提是代码已经过测试和验证。若 PR 中包含 AI 生成代码，请注明所用 coding agent 和 model（例如 “Generated with Claude Code using claude-opus-4-5-20251101”）。

### 开发

- 安装依赖：`pnpm install`
- 构建：`pnpm run build`
- 测试：`pnpm test`
- 本地开发 CLI：`pnpm run dev` 或 `pnpm run dev:cli`
- Conventional commits（单行）：`type(scope): subject`

## 其他

<details>
<summary><strong>Telemetry</strong></summary>

OpenSpec 会收集匿名使用统计。

我们只收集命令名和版本号，用来理解使用模式。不收集参数、路径、内容或 PII。在 CI 环境里会自动关闭。

**退出采集：** `export OPENSPEC_TELEMETRY=0` 或 `export DO_NOT_TRACK=1`

</details>

<details>
<summary><strong>Maintainers & Advisors</strong></summary>

维护者与顾问信息见 [MAINTAINERS.md](MAINTAINERS.md)，其中列出了帮助推动该项目的核心维护者与顾问。

</details>

## License

MIT
