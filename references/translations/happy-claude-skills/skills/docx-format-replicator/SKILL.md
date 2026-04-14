---
name: docx-format-replicator
description: 从现有 Word 文档中提取格式，并基于相同格式生成内容不同的新文档。当用户需要批量生成格式一致的文档、复刻文档模板，或在不同内容之间保持企业文档标准时使用。
metadata:
  author: iamzhihuix
  version: "1.0.0"
---

# DOCX Format Replicator

## Overview

从现有 Word 文档（`.docx`）中提取格式信息，并用它生成格式完全一致但内容不同的新文档。这个 skill 适合制作文档模板、在多份文档间保持一致格式，以及复刻复杂的 Word 文档结构。

## When to Use This Skill

当用户出现以下需求时使用此 skill：

- 想从现有 Word 文档里提取格式
- 需要创建多份格式相同的文档
- 已有模板文档，想基于新内容生成类似文档
- 提到 “replicate”、“copy format”、“use the same style” 或 “create a document like”
- 提到文档模板、企业标准或格式一致性

## Workflow

### Step 1: 从模板中提取格式

从已有 Word 文档中提取格式信息，生成可复用的格式配置文件。

```bash
python scripts/extract_format.py <template.docx> <output.json>
```

**示例**：

```bash
python scripts/extract_format.py "HY研制任务书.docx" format_template.json
```

**提取内容包括：**

- 样式定义（字体、字号、颜色、对齐）
- 段落样式与字符样式
- 编号方案（1、1.1、1.1.1 等）
- 表格结构与样式
- 页眉与页脚配置

**输出**：包含全部格式信息的 JSON 文件（详见 `references/format_config_schema.md`）

### Step 2: 准备内容数据

创建一个 JSON 文件，用来描述新文档的实际内容。该文件必须遵循 `references/content_data_schema.md` 中定义的结构。

**内容结构：**

```json
{
  "metadata": {
    "title": "Document Title",
    "author": "Author Name",
    "version": "1.0",
    "date": "2025-01-15"
  },
  "sections": [
    {
      "type": "heading",
      "content": "Section Title",
      "level": 1,
      "number": "1"
    },
    {
      "type": "paragraph",
      "content": "Paragraph text content."
    },
    {
      "type": "table",
      "rows": 3,
      "cells": [
        ["Header 1", "Header 2"],
        ["Data 1", "Data 2"]
      ]
    }
  ]
}
```

**支持的 section 类型：**

- `heading`：带可选编号的标题
- `paragraph`：普通文本段落
- `table`：可配置行列的表格
- `page_break`：分页符

完整示例见 `assets/example_content.json`。

### Step 3: 生成新文档

使用提取出的格式配置和准备好的内容数据生成新的 Word 文档。

```bash
python scripts/generate_document.py <format.json> <content.json> <output.docx>
```

**示例**：

```bash
python scripts/generate_document.py format_template.json new_content.json output_document.docx
```

**结果**：生成一个新的 `.docx` 文件，其中模板格式会应用到新的内容上。

## Complete Example Workflow

用户说：“我有一个研制任务书，需要再生成 5 份格式相同但内容不同的文档。”

1. **提取格式**：

```bash
python scripts/extract_format.py research_task_template.docx template_format.json
```

2. **为每份新文档准备内容文件**（`content1.json`、`content2.json` 等）

3. **生成文档**：

```bash
python scripts/generate_document.py template_format.json content1.json document1.docx
python scripts/generate_document.py template_format.json content2.json document2.docx
# ... 为所有文档重复执行
```

## Common Use Cases

### 企业文档模板

从公司模板中提取格式，然后生成报告、提案或规格说明，统一品牌与版式。

```bash
# 一次性提取公司模板
python scripts/extract_format.py "Company Template.docx" company_format.json

# 每次生成新文档
python scripts/generate_document.py company_format.json new_report.json "Monthly Report.docx"
```

### 技术文档系列

为多份技术文档（规格书、测试计划、手册）保持统一格式。

```bash
# 从规格书模板提取格式
python scripts/extract_format.py spec_template.docx spec_format.json

# 批量生成多份规格书
python scripts/generate_document.py spec_format.json product_a_spec.json "Product A Spec.docx"
python scripts/generate_document.py spec_format.json product_b_spec.json "Product B Spec.docx"
```

### 研制任务书

随附示例模板（`assets/hy_template_format.json`）展示了一套完整的研制任务书格式，其中包含：

- 页眉中的审批 / 审核表
- 多级编号（1、1.1、1.1.1）
- 技术规格表格
- 结构化章节

可把它作为同类技术文档的起点。

## Advanced Usage

### 自定义提取内容

如需提取默认未覆盖的更多属性，可修改 `scripts/extract_format.py`，例如：

- 自定义 XML 元素
- 高级表格特性（合并单元格、边框）
- 嵌入对象
- 自定义属性

### 扩展内容类型

在 `scripts/generate_document.py` 中添加新的 section 类型：

- 带标题的图片
- 项目符号或编号列表
- 脚注与尾注
- 自定义内容块

扩展建议见 `references/content_data_schema.md`。

### 批量处理

可以写一个包装脚本，批量生成多份文档：

```python
import json
import subprocess

format_file = "template_format.json"
content_files = ["content1.json", "content2.json", "content3.json"]

for i, content_file in enumerate(content_files, 1):
    output = f"document_{i}.docx"
    subprocess.run([
        "python", "scripts/generate_document.py",
        format_file, content_file, output
    ])
```

## Dependencies

脚本依赖：

- Python 3.7+
- `python-docx`：`pip install python-docx`

核心功能不需要其他额外依赖。

## Resources

### scripts/

- **extract_format.py**：从 Word 文档中提取格式
- **generate_document.py**：根据“格式 + 内容”生成新文档

两个脚本都内置帮助信息：

```bash
python scripts/extract_format.py --help
python scripts/generate_document.py --help
```

### references/

- **format_config_schema.md**：格式配置文件的完整 schema
- **content_data_schema.md**：内容数据文件的完整 schema

需要详细了解文件结构与可选项时，先读这两份文档。

### assets/

- **hy_template_format.json**：从技术研制任务书中提取的示例格式
- **example_content.json**：展示全部 section 类型的示例内容数据

创建自定义格式文件与内容文件时，可以直接参考这些样例。

## Troubleshooting

**输出中缺少样式**：确认内容数据里的 style ID 与格式配置中的 style ID 一致。可先检查 `format.json` 里有哪些可用 style ID。

**表格格式异常**：确认内容数据中的表格行列数与格式配置一致。表格结构详见 `format_config_schema.md`。

**字体显示不正确**：部分字体在某些系统上可能不存在。确认引用字体已安装。

**依赖缺失**：安装所需 Python 包：

```bash
pip install python-docx
```

## Tips

1. **先用示例验证流程**：先试用内置的 `hy_template_format.json` 和 `example_content.json`，再开始提取自己的模板。
2. **先从简单内容开始**：先做基础标题和段落，再逐步加表格和复杂格式。
3. **校验 JSON**：生成文档前，先用 JSON 校验工具检查内容文件。
4. **保留格式配置**：提取出的格式配置建议长期保存，便于跨项目复用。
5. **纳入版本控制**：将格式配置和内容数据一起纳入版本管理，确保文档可复现。
