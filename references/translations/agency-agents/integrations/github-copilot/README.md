# GitHub Copilot 集成

The Agency 开箱即用支持 GitHub Copilot，不需要转换。agents 直接使用现有的 `.md` + YAML frontmatter 格式。

## 安装

```bash
# 复制全部 agents 到你的 GitHub Copilot agents 目录
./scripts/install.sh --tool copilot

# 或手动复制某个 category
cp engineering/*.md ~/.github/agents/
cp engineering/*.md ~/.copilot/agents/
```

## 激活一个 Agent

在任意 GitHub Copilot 会话中，直接按名字引用 agent：

```text
Activate Frontend Developer and help me build a React component.
```

```text
Use the Reality Checker agent to verify this feature is production-ready.
```

## Agent 目录

这些 agents 按 division 组织。完整 roster 请看主仓库的 `README.md`。
