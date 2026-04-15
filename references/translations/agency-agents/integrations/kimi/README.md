# Kimi Code CLI 集成

把全部 Agency agents 转成 Kimi Code CLI 的 agent 规格。每个 agent 都会变成一个目录，里面包含 `agent.yaml`（agent spec）和 `system.md`（system prompt）。

## 安装

### 前置条件

- 已安装 [Kimi Code CLI](https://github.com/MoonshotAI/kimi-cli)

### 安装步骤

```bash
# 全新 clone 时必须先生成 integration 文件
./scripts/convert.sh --tool kimi

# 安装 agents
./scripts/install.sh --tool kimi
```

这会把 agents 复制到 `~/.config/kimi/agents/`。

## 使用

### 激活一个 Agent

使用 `--agent-file` 参数加载某个 agent：

```bash
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml
```

### 在某个项目中使用

```bash
cd /your/project
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml \
     --work-dir /your/project \
     "Review this React component for performance issues"
```

### 列出已安装的 Agents

```bash
ls ~/.config/kimi/agents/
```

## Agent 结构

每个 agent 目录都包含：

```text
~/.config/kimi/agents/frontend-developer/
├── agent.yaml    # Agent 规格（tools、subagents）
└── system.md     # system prompt，包含人格与指令
```

### `agent.yaml` 格式

```yaml
version: 1
agent:
  name: frontend-developer
  extend: default  # 继承 Kimi 内置的 default agent
  system_prompt_path: ./system.md
  tools:
    - "kimi_cli.tools.shell:Shell"
    - "kimi_cli.tools.file:ReadFile"
    # ... 所有默认工具
```

## 重新生成

修改源 agents 后：

```bash
./scripts/convert.sh --tool kimi
./scripts/install.sh --tool kimi
```

## 排查问题

### 找不到 agent 文件

确认你已经先运行 `convert.sh`，再运行 `install.sh`：

```bash
./scripts/convert.sh --tool kimi
```

### 未检测到 Kimi CLI

确认 `kimi` 在你的 `PATH` 里：

```bash
which kimi
kimi --version
```

### YAML 无效

可用下面的命令校验生成文件：

```bash
python3 -c "import yaml; yaml.safe_load(open('integrations/kimi/frontend-developer/agent.yaml'))"
```
