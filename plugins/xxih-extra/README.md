# xxih-extra

xxih 个人补全包。

## 定位

- 在公司团队统一 plugin 已经覆盖的能力之外，把 xxih 个人日常依赖、但团队 plugin 没有的 skill 补回来
- **不上传公司渠道**，仅在 xxih 个人机器上安装
- 是 `workbench` 的子集：`workbench` 是一套完整的"外网无团队 plugin 时用的备份"，本包是"在公司有团队 plugin 时，再叠一层补口"

> 公司团队 plugin 已经够强的能力（quality、review、release 等）就别重复进这里；这里只放公司 plugin 没有、且不适合推给团队的东西。

## 当前 skill

- `skills/worktree-flow/`：建立、使用、收尾、销毁临时 worktree + 临时分支的全生命周期 SOP

## 安装

私有，本机直接装：

```bash
# 假设 Claude Code 的本地 plugin 目录是 ~/.claude/plugins/
ln -s "$(pwd)/plugins/xxih-extra" ~/.claude/plugins/xxih-extra
```

具体安装路径以本机 Claude Code 配置为准。

## 维护

每加一个 skill：

1. `plugins/xxih-extra/skills/<skill-name>/SKILL.md`
2. 在本 README 的"当前 skill"一节补一行
