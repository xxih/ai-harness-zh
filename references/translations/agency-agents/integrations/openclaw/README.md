# OpenClaw 集成

OpenClaw agents 会以 workspace 形式安装，包含 `SOUL.md`、`AGENTS.md` 和 `IDENTITY.md` 三个文件。安装器会把每个 workspace 复制到 `~/.openclaw/agency-agents/`，并在检测到 `openclaw` CLI 可用时完成注册。

安装前，先生成 OpenClaw workspaces：

```bash
./scripts/convert.sh --tool openclaw
```

## 安装

```bash
./scripts/install.sh --tool openclaw
```

## 激活一个 Agent

安装完成后，这些 agents 会以 `agentId` 的形式出现在 OpenClaw 会话中。

如果 OpenClaw gateway 已经在运行，安装后需要重启：

```bash
openclaw gateway restart
```

## 重新生成

```bash
./scripts/convert.sh --tool openclaw
```
