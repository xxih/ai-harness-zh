---
name: obsidian-vault
description: 在 Obsidian vault 里搜索、创建、管理笔记(wikilink + index 笔记)。当用户想在 Obsidian 找、建、组织笔记时使用。
---

# Obsidian Vault

> 原文:[skills/personal/obsidian-vault/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/personal/obsidian-vault/SKILL.md)

## Vault 位置

`/mnt/d/Obsidian Vault/AI Research/`

根级**基本是平铺的**。

## 命名约定

- **Index 笔记**:聚合相关话题(如 `Ralph Wiggum Index.md`、`Skills Index.md`、`RAG Index.md`)
- 所有笔记名用 **Title Case**
- **不用文件夹做组织** —— 用链接和 index 笔记代替

## 链接

- 用 Obsidian `[[wikilink]]` 语法:`[[Note Title]]`
- 笔记在底部链到依赖/相关笔记
- Index 笔记就是 `[[wikilink]]` 列表

## 工作流

### 搜笔记

```bash
# 按文件名搜
find "/mnt/d/Obsidian Vault/AI Research/" -name "*.md" | grep -i "keyword"

# 按内容搜
grep -rl "keyword" "/mnt/d/Obsidian Vault/AI Research/" --include="*.md"
```

也可以直接在 vault 路径上用 Grep / Glob 工具。

### 建新笔记

1. 文件名用 **Title Case**
2. 把内容写成**一个学习单元**(按 vault 规则)
3. 在底部加链到相关笔记的 `[[wikilink]]`
4. 如果属于编号序列,**用层级编号**

### 找相关笔记

在 vault 里搜 `[[Note Title]]` 找反向链接:

```bash
grep -rl "\\[\\[Note Title\\]\\]" "/mnt/d/Obsidian Vault/AI Research/"
```

### 找 index 笔记

```bash
find "/mnt/d/Obsidian Vault/AI Research/" -name "*Index*"
```
