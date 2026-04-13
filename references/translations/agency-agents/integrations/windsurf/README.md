# Windsurf 集成

全部 61 个 Agency agents 会被合并成一个 `.windsurfrules` 文件。规则是**项目级作用域**，因此需要从你的项目根目录安装。

## 安装

```bash
# 在你的项目根目录执行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool windsurf
```

## 激活一个 Agent

在 Windsurf 中，直接在 prompt 里按名称引用 agent：

```text
Use the Frontend Developer agent to build this component.
```

## 重新生成

```bash
./scripts/convert.sh --tool windsurf
```
