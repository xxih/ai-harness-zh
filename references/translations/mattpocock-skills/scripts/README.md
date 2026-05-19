# Scripts(中文说明)

> 原文目录:[scripts/](https://github.com/mattpocock/skills/tree/main/scripts)

仓库自带两个**仓库管理工具**(不是 skill 本体)。**这里只做用途说明,代码本体不翻**——它们短小,直接读原文最准。

## `link-skills.sh`

把仓库所有非 deprecated 的 skill **软链到 `~/.claude/skills/<skill-name>`**,这样本机 Claude CLI 能直接用。

行为:

- 遍历 `skills/**/SKILL.md`,跳过 `node_modules/` 和 `deprecated/`
- 每个 skill 目录在 `~/.claude/skills/` 下建一个 `ln -sfn` 软链
- 如果 `~/.claude/skills` 自己是指向**本仓库**的 symlink(会产生自指),**报错并退出**——避免污染工作副本
- 目标已是真目录(非 symlink)时,**会先 `rm -rf` 再链**——注意

## `list-skills.sh`

打印仓库中所有 `SKILL.md` 路径,按字母排序。**纯辅助**,用来 `npx skills@latest` 安装器之类的场景列清单。

## 中文实践提示

如果你不想直接用 Matt 的 link-skills(它会清掉同名真目录,而你的 `~/.claude/skills/` 已经有 `my-cc-plugins` 的本地 skill),**就别跑它**。这俩脚本是 Matt 本人的工作流,不是核心资产——核心资产是 `skills/**/SKILL.md`。
