---
name: write-a-skill
description: 用正确结构、渐进披露、资源打包写新的 agent skill。当用户想创建、撰写或构建一个新 skill 时使用。
---

# 写 Skill

> 原文:[skills/productivity/write-a-skill/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/write-a-skill/SKILL.md)

## 流程

1. **收集需求** —— 问用户:
   - 这个 skill 覆盖什么任务/领域?
   - 它要处理哪些具体 use case?
   - 需要可执行脚本,还是只要指令?
   - 有要包含的参考材料吗?

2. **起草 skill** —— 创建:
   - **`SKILL.md`** 含简洁指令
   - 如果内容超过 500 行,加额外的参考文件
   - 如果有确定性操作,加工具脚本

3. **跟用户复核** —— 展示草稿,问:
   - 覆盖了你的 use case 吗?
   - 缺了什么或不清楚的吗?
   - 哪些节该更详/更简?

## Skill 结构

```
skill-name/
├── SKILL.md           # 主指令(必需)
├── REFERENCE.md       # 详细文档(如需要)
├── EXAMPLES.md        # 使用样例(如需要)
└── scripts/           # 工具脚本(如需要)
    └── helper.js
```

## SKILL.md 模板

```md
---
name: skill-name
description: 能力的简短描述。当 [具体触发条件] 时使用。
---

# Skill 名

## 快速开始

[最小可运行例子]

## 工作流

[复杂任务的逐步流程 + checklist]

## 高级功能

[链接到独立文件:见 [REFERENCE.md](REFERENCE.md)]
```

## description 要求

description 是**你的 agent 在决定加载哪个 skill 时看到的唯一东西**。它和所有已安装 skill 的 description 一起出现在系统提示里。**你的 agent 读这些 description,根据用户请求挑相关 skill**。

**目标**:给 agent 刚好够的信息知道:

1. 这个 skill 提供什么能力
2. 何时/为何触发它(具体关键词、上下文、文件类型)

**格式**:

- 最多 1024 字符
- 用**第三人称**写
- **第一句**:它做什么
- **第二句**:"当 [具体触发] 时使用"

**好例子**:

```
Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction.
```

**差例子**:

```
Helps with documents.
```

差例子让 agent 没法把这个和别的文档 skill 区分开。

## 什么时候加脚本

加工具脚本的条件:

- 操作是确定性的(校验、格式化)
- 同样代码会被反复生成
- 错误需要显式处理

**脚本相比生成代码,省 token 且更可靠**。

## 什么时候拆文件

拆成独立文件的条件:

- `SKILL.md` 超过 100 行
- 内容有清晰的不同领域(金融 vs 销售 schema)
- 高级功能很少被需要

## 复核 checklist

起草后核对:

- [ ] description 含触发条件("Use when...")
- [ ] `SKILL.md` 在 100 行以内
- [ ] 没时间敏感信息
- [ ] 术语一致
- [ ] 含具体例子
- [ ] 引用只下一层
