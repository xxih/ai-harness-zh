# Skill Discovery Contract

> 用于扫描、盘点和渲染 GSD skills 的规范规则。

## 根目录分类

### 项目级根目录

相对于项目根目录扫描以下路径：

- `.claude/skills/`
- `.agents/skills/`
- `.cursor/skills/`
- `.github/skills/`
- `./.codex/skills/`

这些根目录用于项目级 skills，以及项目 `CLAUDE.md` 里的 skills 区段。

### 托管式全局根目录

相对于用户 home 目录扫描以下路径：

- `~/.claude/skills/`
- `~/.codex/skills/`

这些根目录用于托管式运行时安装和盘点报告。

### 已废弃的仅导入根目录

- `~/.claude/get-shit-done/skills/`

这个根目录只为旧版迁移保留。盘点代码可以报告它，但新的安装流程不应再往这里写入。

### 旧版 Claude Commands

- `~/.claude/commands/gsd/`

这里不是 skills 根目录。发现逻辑只会检查它是否存在，以便盘点结果能报告旧版 Claude 安装。

## 归一化规则

- 只扫描包含 `SKILL.md` 的子目录。
- 从 YAML frontmatter 读取 `name` 和 `description`。
- 如果缺少 `name`，就使用目录名。
- 从匹配 `TRIGGER when: ...` 的正文行中提取触发提示。
- 将 `gsd-*` 目录视为已安装的框架 skills。
- 将 `~/.claude/get-shit-done/skills/` 下的条目标记为已废弃 / 仅导入。
- 将 `~/.claude/commands/gsd/` 视为旧版 command 安装元数据，而不是 skills。

## 扫描器行为

### `sdk/src/query/skills.ts`

- 返回去重后的已发现 skill 名称列表。
- 扫描项目级根目录和托管式全局根目录。
- 不扫描已废弃的仅导入根目录。

### `get-shit-done/bin/lib/profile-output.cjs`

- 构建项目 `CLAUDE.md` 的 skills 区段。
- 只扫描项目级根目录。
- 跳过 `gsd-*` 目录，保证项目区段聚焦在用户 / 项目自己的 skills 上。
- 将 `.codex/skills/` 纳入项目发现集合。

### `get-shit-done/bin/lib/init.cjs`

- 为 `skill-manifest` 生成 skill 盘点对象。
- 报告 `skills`、`roots`、`installation` 和 `counts`。
- 只要发现任意 skill 名称以 `gsd-` 开头，就把 `gsd_skills_installed` 标记为 true。
- 当 `~/.claude/commands/gsd/` 中包含 `.md` command 文件时，把 `legacy_claude_commands_installed` 标记为 true。

## 盘点结构

`skill-manifest` 会返回一个 JSON 对象，包含：

- `skills`：归一化后的 skill 条目
- `roots`：实际检查过的规范根目录
- `installation`：已安装 GSD skills 与旧版 Claude commands 的汇总布尔值
- `counts`：提供给下游消费者使用的小型盘点计数

每个 skill 条目都包含：

- `name`
- `description`
- `triggers`
- `path`
- `file_path`
- `root`
- `scope`
- `installed`
- `deprecated`
