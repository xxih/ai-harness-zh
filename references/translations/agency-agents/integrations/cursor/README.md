# Cursor 集成

该集成会把完整的 Agency roster 转成 Cursor 的 `.mdc` rule 文件。规则是**项目级作用域**，需要从项目根目录安装。

## 安装

```bash
# 在你的项目根目录执行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool cursor
```

执行后会在项目中生成 `.cursor/rules/<agent-slug>.mdc` 文件。

## 激活一条 Rule

在 Cursor 中，在 prompt 里引用某个 agent：

```text
@frontend-developer Review this React component for performance issues.
```

也可以通过修改 frontmatter 把一条 rule 设为 always-on：

```yaml
---
description: Expert frontend developer...
globs: "**/*.tsx,**/*.ts"
alwaysApply: true
---
```

## 重新生成

```bash
./scripts/convert.sh --tool cursor
```
