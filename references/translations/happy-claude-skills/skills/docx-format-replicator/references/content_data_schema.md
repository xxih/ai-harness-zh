# Content Data Schema

本文档描述 `generate_document.py` 所使用的内容数据文件 JSON schema。

## Overview

内容数据文件定义了将要写入 Word 文档的实际内容（文本、标题、表格）。这些内容会结合格式配置中的规则一起生成最终文档。

## Schema Structure

```json
{
  "metadata": {},
  "sections": []
}
```

## Fields

### metadata

**Type**：`object`  
**Description**：文档内容的可选元数据。

**字段：**

- `title`（string）：文档标题
- `author`（string）：文档作者
- `version`（string）：版本号
- `date`（string）：文档日期

**示例：**

```json
"metadata": {
  "title": "Product Research Task Specification",
  "author": "Engineering Team",
  "version": "1.0",
  "date": "2025-01-15"
}
```

### sections

**Type**：`array`  
**Description**：构成文档的内容 section 数组，按顺序处理。

每个 section 都是一个对象，包含 `type` 字段以及该类型对应的专用属性。

## Section Types

### Heading Section

创建带可选编号的标题。

**字段：**

- `type`（string）：必须为 `"heading"`
- `content`（string）：标题文本
- `level`（number）：标题级别（1-9）
- `number`（string，可选）：编号前缀（如 `"1"`、`"1.1"`、`"1.1.1"`）

**示例：**

```json
{
  "type": "heading",
  "content": "Introduction",
  "level": 1,
  "number": "1"
}
```

### Paragraph Section

创建普通文本段落。

**字段：**

- `type`（string）：必须为 `"paragraph"`
- `content`（string）：段落文本
- `style_id`（string，可选）：要应用的样式 ID，取自格式配置

**示例：**

```json
{
  "type": "paragraph",
  "content": "This document outlines the technical requirements for the product.",
  "style_id": "1"
}
```

### Table Section

创建表格。

**字段：**

- `type`（string）：必须为 `"table"`
- `rows`（number）：行数
- `columns`（array）：列宽定义（来自格式配置）
- `table_index`（number，可选）：使用哪一个表格配置的索引
- `cells`（array）：二维数组形式的单元格内容

**示例：**

```json
{
  "type": "table",
  "rows": 3,
  "columns": ["2000", "8000"],
  "table_index": 0,
  "cells": [
    ["Header 1", "Header 2"],
    ["Row 1 Col 1", "Row 1 Col 2"],
    ["Row 2 Col 1", "Row 2 Col 2"]
  ]
}
```

### Page Break Section

插入分页符。

**字段：**

- `type`（string）：必须为 `"page_break"`

**示例：**

```json
{
  "type": "page_break"
}
```

## Complete Example

下面是一份技术文档内容数据文件的完整示例：

```json
{
  "metadata": {
    "title": "New Product Research Task Specification",
    "author": "Research Team",
    "version": "1.0",
    "date": "2025-01-15"
  },
  "sections": [
    {
      "type": "heading",
      "content": "Introduction",
      "level": 1,
      "number": "1"
    },
    {
      "type": "paragraph",
      "content": "This document defines the research and development tasks for the new product initiative."
    },
    {
      "type": "heading",
      "content": "Product Name and Code",
      "level": 1,
      "number": "2"
    },
    {
      "type": "paragraph",
      "content": "Product Name: Advanced Control System"
    },
    {
      "type": "paragraph",
      "content": "Product Code: ACS-2025-01"
    },
    {
      "type": "heading",
      "content": "Technical Specifications",
      "level": 1,
      "number": "3"
    },
    {
      "type": "heading",
      "content": "Electrical Requirements",
      "level": 2,
      "number": "3.1"
    },
    {
      "type": "table",
      "rows": 4,
      "columns": ["3000", "7000"],
      "cells": [
        ["Parameter", "Specification"],
        ["Input Voltage", "220V AC ± 10%"],
        ["Power Consumption", "≤ 500W"],
        ["Frequency", "50Hz ± 2Hz"]
      ]
    },
    {
      "type": "page_break"
    },
    {
      "type": "heading",
      "content": "Testing Requirements",
      "level": 1,
      "number": "4"
    },
    {
      "type": "paragraph",
      "content": "All products must undergo comprehensive testing according to industry standards."
    }
  ]
}
```

## Usage Patterns

### 多级编号

适用于包含嵌套章节（1、1.1、1.1.1）的文档：

```json
[
  {"type": "heading", "content": "First Section", "level": 1, "number": "1"},
  {"type": "heading", "content": "Subsection A", "level": 2, "number": "1.1"},
  {"type": "heading", "content": "Sub-subsection", "level": 3, "number": "1.1.1"},
  {"type": "heading", "content": "Subsection B", "level": 2, "number": "1.2"},
  {"type": "heading", "content": "Second Section", "level": 1, "number": "2"}
]
```

### 复杂表格

对于需要合并单元格或特殊格式的表格，你可能需要扩展 schema：

```json
{
  "type": "table",
  "rows": 3,
  "columns": ["2000", "4000", "4000"],
  "cells": [
    ["Header 1", "Header 2", "Header 3"],
    ["Data 1", "Data 2", "Data 3"],
    ["Data 4", "Data 5", "Data 6"]
  ],
  "merge_cells": [
    {"row": 0, "col": 1, "row_span": 1, "col_span": 2}
  ]
}
```

### 审批表

适用于带审批 / 审核表的文档（技术文档中较常见）：

```json
{
  "type": "table",
  "table_index": 0,
  "cells": [
    ["Version", "1.0"],
    ["Author", "John Doe"],
    ["Reviewer", "Jane Smith"],
    ["Approver", "Manager Name"],
    ["Date", "2025-01-15"]
  ]
}
```

## Tips
