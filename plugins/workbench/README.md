# workbench

个人日常使用的 Claude Code plugin。把自己最常用的 skill / command / agent 沉淀在这里，按需扩充。

## 目录结构

```
workbench/
├── .claude-plugin/
│   └── plugin.json
├── README.md
└── skills/
    ├── architecture-decision-records/
    │   └── SKILL.md
    └── quality-tdd/
        ├── SKILL.md
        └── references/
            └── testing-anti-patterns.md
```

## 当前内容

| 类型 | 名称 | 来源 | 说明 |
|------|------|------|------|
| skill | `architecture-decision-records` | everything-claude-code | 在编码会话中捕捉架构决策，生成 ADR 文档 |
| skill | `quality-tdd` | packages/quality-workflows | 测试先行硬约束：没看到测试先失败就不算完成 TDD |

## 使用

### 方式 A：临时加载（单次会话）

直接在启动 Claude Code 时通过 `--plugin-dir` 指向本目录：

```bash
claude --plugin-dir /Users/xxih/workspace/ai-harness-zh/plugins/workbench
```

`--plugin-dir` 可以重复传，加载多个本地 plugin：

```bash
claude --plugin-dir ./plugins/workbench --plugin-dir ./plugins/another
```

仅对本次会话生效，不会写入任何配置。

### 方式 B：持久安装（通过本地 marketplace）

如果想长期启用、并能 `/plugin` 管理，需要先在某个目录建立 `marketplace.json` 把 workbench 注册进去，然后：

```bash
# 把 marketplace 加进来（user 作用域，仅本机）
claude plugin marketplace add /path/to/marketplace-dir

# 安装 workbench
claude plugin install workbench@<marketplace-name>
```

> 当前仓库还没有配 marketplace。要走这条路就再告诉我，我把 `.claude-plugin/marketplace.json` 也建出来。

### 验证 plugin 合法性

```bash
claude plugin validate /Users/xxih/workspace/ai-harness-zh/plugins/workbench
```

加载成功后，`architecture-decision-records` skill 会在检测到决策时刻时被激活，详见 `skills/architecture-decision-records/SKILL.md`。

## 添加新内容

* skill：在 `skills/<skill-name>/SKILL.md` 创建，frontmatter 至少包含 `name`、`description`
* command：在 `commands/<name>.md` 创建，frontmatter 包含 `description`
* agent：在 `agents/<name>.md` 创建，frontmatter 包含 `name`、`description`、`tools`、`model`
* hook：在 `hooks/` 内放置 JSON 配置

新增内容后，记得更新本 README 的"当前内容"表格。
