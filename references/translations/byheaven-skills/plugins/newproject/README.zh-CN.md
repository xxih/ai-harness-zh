# newproject

`newproject` 是一个自包含的项目初始化 skill，以 Claude Code 插件形式打包。它既可以从零搭起一个仓库，也可以把已有项目升级到可用于生产的基线，覆盖 CI、代码质量、发布自动化、GitHub 仓库配置、依赖管理与安全扫描。

## 它做什么

`newproject` 是这个插件唯一的主入口。
它把所需的模板、工作流、脚本和参考资料都 vendored 在自身目录里，因此整套初始化流程集中在一个地方。

```text
Tier 1 — Foundation
  脚手架与仓库基线
  发布工作流
  CI pipeline

Tier 2 — Quality and Governance
  代码质量
  GitHub 仓库配置
  依赖管理

Tier 3 — Security
  安全扫描
```

为了兼容旧用法和高级场景，插件仍然打包了早期更细粒度的 setup skills，但在常规 `newproject` 使用路径下已经不再要求额外安装它们。

## 安装

### Claude Code 插件

```text
/plugin marketplace add byheaven/byheaven-skills
/plugin install newproject
```

### Codex 与其他基于 skill 的工具

```bash
npx skills add byheaven/byheaven-skills
```

直接使用 `newproject` 即可。它是自包含的，不依赖同级 setup skills 一起安装。

## 用法

### 完整项目初始化

直接自然描述即可：

```text
Set up my new project
/newproject
```

这个 skill 会先识别项目类型，盘点当前仓库已经存在的内容，向用户展示一份检查清单，然后按依赖顺序执行所选初始化部分。

## 支持的项目类型

- **Web**（Next.js、Nuxt、Astro、Remix、SvelteKit 及类似项目）
- **Node.js**（库、API、CLI）
- **Python**（应用、库、数据工具）
- **Go**（服务、CLI、库）
- **Rust**（系统项目、CLI、库）
- **Generic**（其他任意语言）

## 许可证

MIT
