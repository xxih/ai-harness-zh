# 领域文档

> 原文:[domain.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/domain.md)

engineering skill 探索代码库时,应该怎么消费本仓库的领域文档。

## 探索之前,先读这些

- **根目录 `CONTEXT.md`**,或
- **根目录 `CONTEXT-MAP.md`** —— 如果存在,它指向每个 context 的 `CONTEXT.md`。读跟话题相关的那些。
- **`docs/adr/`** —— 读你即将动的区域的 ADR。多 context 仓库下也要看 `src/<context>/docs/adr/` 的 context 内决策。

如果这些文件**有缺**,**安静地继续**。不要标记缺失;不要提议预先创建。**生产者 skill(`/grill-with-docs`)在术语或决策真正被定义时才懒加载创建**。

## 文件结构

单 context 仓库(大部分):

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

多 context 仓库(根目录有 `CONTEXT-MAP.md` 标志):

```
/
├── CONTEXT-MAP.md
├── docs/adr/                          ← 系统级决策
└── src/
    ├── ordering/
    │   ├── CONTEXT.md
    │   └── docs/adr/                  ← context 内决策
    └── billing/
        ├── CONTEXT.md
        └── docs/adr/
```

## 用术语表的词汇

输出里点名领域概念时(issue 标题、重构方案、假设、测试名),**用 `CONTEXT.md` 定义的词**。不要漂到术语表明确禁用的同义词。

如果你需要的概念还不在术语表里,**那是一个信号**——要么你在发明项目没用的语言(重新考虑),要么这是真空隙(为 `/grill-with-docs` 记一笔)。

## 标出 ADR 冲突

输出和已有 ADR 矛盾时,**明确摆出来**,别默默覆盖:

> _与 ADR-0007(event-sourced orders)矛盾——但值得重开,因为……_
