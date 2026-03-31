# Format Configuration Schema

本文档描述 `extract_format.py` 生成的格式配置文件 JSON schema。

## Overview

格式配置文件保存了从 Word 文档中提取出的格式信息，包括样式、编号、表格结构以及页眉 / 页脚信息。

## Schema Structure

```json
{
  "source_document": "string",
  "styles": {},
  "numbering": {},
  "tables": [],
  "headers_footers": {}
}
```

## Fields

### source_document

**Type**：`string`  
**Description**：被提取格式的源文档名称。

**示例：**

```json
"source_document": "template.docx"
```

### styles

**Type**：`object`  
**Description**：样式定义字典，以 style ID 为键。

每个 style 对象包含：

- `id`（string）：样式标识符
- `name`（string）：人类可读的样式名称
- `type`（string）：样式类型（paragraph、character、table、numbering）
- `fonts`（object）：字体属性
  - `ascii`（string）：ASCII 字体名
  - `hAnsi`（string）：High ANSI 字体名
  - `eastAsia`（string）：东亚字体名
  - `size`（string）：字号，单位为 half-points
- `paragraph`（object）：段落属性
  - `alignment`（string）：文本对齐方式（left、center、right、both）
  - `spacing`（object）：行距配置

**示例：**

```json
"styles": {
  "1": {
    "id": "1",
    "name": "Normal",
    "type": "paragraph",
    "fonts": {
      "ascii": "Times New Roman",
      "hAnsi": "Times New Roman",
      "eastAsia": "宋体",
      "size": "24"
    },
    "paragraph": {
      "alignment": "left",
      "spacing": {
        "line": "360",
        "lineRule": "auto"
      }
    }
  },
  "2": {
    "id": "2",
    "name": "heading 1",
    "type": "paragraph",
    "fonts": {
      "ascii": "Times New Roman",
      "size": "32"
    },
    "paragraph": {
      "alignment": "left"
    }
  }
}
```

### numbering

**Type**：`object`  
**Description**：自动编号定义，用于表示 1、1.1、1.1.1 等层级编号。

每个编号条目会把一个 numbering ID 映射到它的抽象编号定义。

**示例：**

```json
"numbering": {
  "1": {
    "abstractNumId": "0"
  },
  "2": {
    "abstractNumId": "1"
  }
}
```

### tables

**Type**：`array`  
**Description**：文档中发现的表格结构定义数组。

每个 table 对象包含：

- `index`（number）：表格的零基索引
- `rows`（number）：表格行数
- `columns`（array）：列宽数组
- `properties`（object）：表格属性
  - `width`（object）：表格宽度设置
  - `style`（string）：表格样式 ID

**示例：**

```json
"tables": [
  {
    "index": 0,
    "rows": 5,
    "columns": ["1984", "8076", "40"],
    "properties": {
      "width": {
        "value": "10100",
        "type": "dxa"
      },
      "style": "49"
    }
  }
]
```

### headers_footers

**Type**：`object`  
**Description**：文档页眉与页脚的信息。

包含：

- `headers`（array）：页眉文件列表
- `footers`（array）：页脚文件列表

**示例：**

```json
"headers_footers": {
  "headers": [
    {
      "file": "word/header1.xml",
      "exists": true
    }
  ],
  "footers": [
    {
      "file": "word/footer1.xml",
      "exists": true
    }
  ]
}
```

## Usage Notes

### Style IDs vs Style Names

Word 文档内部通常使用数字 style ID（如 `"1"`、`"2"`），它们再映射到具名样式（如 `"Normal"`、`"heading 1"`）。格式配置会同时保留这两类信息，以获得更好的兼容性。

### 宽度单位

OOXML 中的宽度通常使用 `dxa` 单位（point 的二十分之一）。常见换算如下：

- 1 inch = 1440 dxa
- 1 cm = 567 dxa
- 1 pt = 20 dxa

### 提取更多属性

当前 schema 覆盖的是最常见的格式属性。对于特殊文档，你可能需要：

1. 修改 `extract_format.py`，提取更多属性
2. 同步更新本 schema 文档
3. 更新 `generate_document.py`，使其能够应用这些属性

## Example Complete Configuration

```json
{
  "source_document": "research_task_template.docx",
  "styles": {
    "1": {
      "id": "1",
      "name": "Normal",
      "type": "paragraph",
      "fonts": {
        "ascii": "Times New Roman",
        "hAnsi": "Times New Roman",
        "eastAsia": "宋体",
        "size": "24"
      },
      "paragraph": {
        "alignment": "left"
      }
    }
  },
  "numbering": {
    "1": {
      "abstractNumId": "0"
    }
  },
  "tables": [
    {
      "index": 0,
      "rows": 8,
      "columns": ["2000", "8000"],
      "properties": {
        "width": {
          "value": "10000",
          "type": "dxa"
        },
        "style": "GridTable"
      }
    }
  ],
  "headers_footers": {
    "headers": [
      {"file": "word/header1.xml", "exists": true}
    ],
    "footers": [
      {"file": "word/footer1.xml", "exists": true}
    ]
  }
}
```
