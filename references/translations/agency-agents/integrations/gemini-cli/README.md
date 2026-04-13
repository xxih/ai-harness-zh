# Gemini CLI 集成

把全部 61 个 Agency agents 打包成一个 Gemini CLI extension。安装后，extension 会落到 `~/.gemini/extensions/agency-agents/`。

## 安装

```bash
# 先生成 Gemini CLI integration 文件
./scripts/convert.sh --tool gemini-cli

# 再安装 extension
./scripts/install.sh --tool gemini-cli
```

## 激活一个 Skill

在 Gemini CLI 中，按名称引用某个 agent：

```text
Use the frontend-developer skill to help me build this UI.
```

## Extension 结构

```text
~/.gemini/extensions/agency-agents/
  gemini-extension.json
  skills/
    frontend-developer/SKILL.md
    backend-architect/SKILL.md
    reality-checker/SKILL.md
    ...
```

## 重新生成

```bash
./scripts/convert.sh --tool gemini-cli
```
