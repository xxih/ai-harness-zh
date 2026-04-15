# Aider 集成

完整的 Agency roster 会被汇总成一个 `CONVENTIONS.md` 文件。只要它位于项目根目录，Aider 就会自动读取它。

## 安装

```bash
# 在你的项目根目录执行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool aider
```

## 激活一个 Agent

在 Aider 会话里，直接按名字引用 agent：

```text
Use the Frontend Developer agent to refactor this component.
```

```text
Apply the Reality Checker agent to verify this is production-ready.
```

## 手动使用

也可以直接把 conventions 文件传给 Aider：

```bash
aider --read CONVENTIONS.md
```

## 重新生成

```bash
./scripts/convert.sh --tool aider
```
