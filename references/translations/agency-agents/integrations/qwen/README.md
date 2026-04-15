# Qwen Code 集成

Qwen Code 使用项目级 `.md` SubAgent 文件，路径在 `.qwen/agents/`。

生成文件来自 `scripts/convert.sh --tool qwen`，它会为每个 agency agent 在 `integrations/qwen/agents/` 下写出一个 SubAgent Markdown 文件。

## 生成

从仓库根目录执行：

```bash
./scripts/convert.sh --tool qwen
```

## 安装

从目标项目根目录运行安装器：

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool qwen
```

这会把生成好的 SubAgent 文件复制到：

```text
.qwen/agents/
```

## 在 Qwen Code 中刷新

安装完成后：

- 在 Qwen Code 中运行 `/agents manage` 刷新 agent 列表，或
- 重启当前的 Qwen Code 会话

## 说明

- Qwen Code 是项目级作用域，不是 home 级作用域
- 生成的 Qwen 文件只使用最小 frontmatter：`name`、`description`，以及可选的 `tools`
- 如果你更新了这个仓库中的 agents，需要重新生成 Qwen 输出后再安装
