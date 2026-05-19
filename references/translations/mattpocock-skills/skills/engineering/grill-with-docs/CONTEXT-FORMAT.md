# CONTEXT.md 格式

> 原文:[CONTEXT-FORMAT.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/CONTEXT-FORMAT.md)

## 结构

```md
# {Context 名}

{一两句话:这个 context 是什么、为什么存在。}

## Language(术语)

**Order**:
{对术语的简洁说明}
_Avoid_: Purchase, transaction

**Invoice**:
交付后发给客户的付款请求。
_Avoid_: Bill, payment request

**Customer**:
下 order 的人或组织。
_Avoid_: Client, buyer, account

## Relationships(关系)

- 一个 **Order** 产出一到多个 **Invoice**
- 一个 **Invoice** 属于且仅属于一个 **Customer**

## Example dialogue(示例对话)

> **Dev:** "**Customer** 下 **Order** 的时候我们要立刻开 **Invoice** 吗?"
> **Domain expert:** "不——**Invoice** 只在 **Fulfillment** 被确认后才生成。"

## Flagged ambiguities(标记的歧义)

- "account" 之前同时被用来指 **Customer** 和 **User** —— 已解决:这是两个不同概念。
```

## 规则

- **要有立场**。同一个概念有多个词时,选一个最好的,其它列为"应避免的别名"。
- **明确标记冲突**。一个词被歧义地使用时,在 "Flagged ambiguities" 里写出来并给出明确结论。
- **定义要紧**。最多一句话。**定义"它是什么"**,不是"它做什么"。
- **展现关系**。用粗体术语名,在明显处表达基数(cardinality)。
- **只收录这个项目 context 特有的术语**。通用编程概念(超时、错误类型、工具模式)不属于这里——哪怕项目里大量使用。加术语前先问:这是这个 context 独有的概念,还是通用编程概念?**只有前者才该进来。**
- **自然分组时用子标题**。如果所有术语属于同一个连贯领域,扁平列表也 OK。
- **写一段示例对话**。Dev 和 domain expert 的对话,演示术语怎么自然交互,以及相关概念之间的边界。

## 单 context 还是多 context 仓库

**单 context(大多数仓库)**:仓库根放一份 `CONTEXT.md`。

**多 context**:仓库根放 `CONTEXT-MAP.md`,列出各 context、位置、彼此关系:

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) — 接收和追踪客户 order
- [Billing](./src/billing/CONTEXT.md) — 生成 invoice 并处理付款
- [Fulfillment](./src/fulfillment/CONTEXT.md) — 仓库捡货和发货

## Relationships

- **Ordering → Fulfillment**:Ordering 发 `OrderPlaced` 事件,Fulfillment 消费它开始捡货
- **Fulfillment → Billing**:Fulfillment 发 `ShipmentDispatched`,Billing 消费它生成发票
- **Ordering ↔ Billing**:共享 `CustomerId` 和 `Money` 类型
```

Skill 自己推断哪种结构适用:

- 有 `CONTEXT-MAP.md` → 读它找 context
- 只有根 `CONTEXT.md` → 单 context
- 都没有 → 在第一个术语定义时懒创建根 `CONTEXT.md`

多 context 存在时,推断当前话题归哪个。不清楚就问。
