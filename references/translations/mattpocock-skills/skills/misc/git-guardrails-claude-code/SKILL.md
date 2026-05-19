---
name: git-guardrails-claude-code
description: 设置 Claude Code hook 在执行前拦截危险 git 命令(push, reset --hard, clean, branch -D 等)。当用户想阻止破坏性 git 操作、加 git 安全 hook,或在 Claude Code 里拦 git push/reset 时使用。
---

# Setup Git Guardrails

> 原文:[skills/misc/git-guardrails-claude-code/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/misc/git-guardrails-claude-code/SKILL.md)

配置一个 PreToolUse hook,在 Claude 执行前拦截危险 git 命令。

## 拦截什么

- `git push`(所有变体,包括 `--force`)
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

被拦截时,Claude 会看到一条说"你没有权限执行这些命令"的消息。

## 步骤

### 1. 问范围

问用户:**只装本项目**(`.claude/settings.json`)还是**所有项目**(`~/.claude/settings.json`)?

### 2. 复制 hook 脚本

打包脚本在:[scripts/block-dangerous-git.sh](scripts/block-dangerous-git.sh)

按范围复制:

- **项目**:`.claude/hooks/block-dangerous-git.sh`
- **全局**:`~/.claude/hooks/block-dangerous-git.sh`

用 `chmod +x` 设可执行。

### 3. 把 hook 加到 settings

加到对应 settings 文件:

**项目**(`.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

**全局**(`~/.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

如果 settings 已存在,**把 hook 合并到 `hooks.PreToolUse` 数组**——别覆盖其它配置。

### 4. 问要不要定制

问用户要不要从拦截列表里加/去哪些模式。改复制后的脚本。

### 5. 验证

快速测试:

```bash
echo '{"tool_input":{"command":"git push origin main"}}' | <path-to-script>
```

应该以 exit code 2 退出,并在 stderr 打印 BLOCKED 信息。
