---
name: migrate-to-shoehorn
description: 把测试文件里的 `as` 类型断言迁到 @total-typescript/shoehorn。当用户提到 shoehorn、想替换测试里的 `as`,或需要传部分测试数据时使用。
---

# Migrate to Shoehorn

> 原文:[skills/misc/migrate-to-shoehorn/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/misc/migrate-to-shoehorn/SKILL.md)

## 为什么用 shoehorn

`shoehorn` 让你在测试里**传部分数据**的同时让 TypeScript 满意。用类型安全的替代物替换 `as` 断言。

**只在测试代码**。**永远不要**在生产代码用 shoehorn。

测试里用 `as` 的问题:

- 大家被教育"别用 as"
- 必须手动指定目标类型
- 故意传错数据时要 double-as(`as unknown as Type`)

## 安装

```bash
npm i @total-typescript/shoehorn
```

## 迁移模式

### 大对象,只关心几个字段

之前:

```ts
type Request = {
  body: { id: string };
  headers: Record<string, string>;
  cookies: Record<string, string>;
  // ...还有 20 个字段
};

it("gets user by id", () => {
  // 只关心 body.id 但必须 fake 整个 Request
  getUser({
    body: { id: "123" },
    headers: {},
    cookies: {},
    // ...fake 全部 20 个字段
  });
});
```

之后:

```ts
import { fromPartial } from "@total-typescript/shoehorn";

it("gets user by id", () => {
  getUser(
    fromPartial({
      body: { id: "123" },
    }),
  );
});
```

### `as Type` → `fromPartial()`

之前:

```ts
getUser({ body: { id: "123" } } as Request);
```

之后:

```ts
import { fromPartial } from "@total-typescript/shoehorn";

getUser(fromPartial({ body: { id: "123" } }));
```

### `as unknown as Type` → `fromAny()`

之前:

```ts
getUser({ body: { id: 123 } } as unknown as Request); // 故意传错类型
```

之后:

```ts
import { fromAny } from "@total-typescript/shoehorn";

getUser(fromAny({ body: { id: 123 } }));
```

## 各函数何时用

| 函数            | 用法                                      |
| --------------- | ----------------------------------------- |
| `fromPartial()` | 传部分数据,仍然类型检查                  |
| `fromAny()`     | 故意传错类型的数据(保留自动补全)        |
| `fromExact()`   | 强制完整对象(以后可换回 fromPartial)    |

## 工作流

1. **采集需求** —— 问用户:
   - 哪些测试文件里 `as` 断言有问题?
   - 是不是大对象只关心几个字段?
   - 需不需要传故意错的数据做错误路径测试?

2. **安装 + 迁移**:
   - [ ] 装:`npm i @total-typescript/shoehorn`
   - [ ] 找测试里的 `as`:`grep -r " as [A-Z]" --include="*.test.ts" --include="*.spec.ts"`
   - [ ] `as Type` 换 `fromPartial()`
   - [ ] `as unknown as Type` 换 `fromAny()`
   - [ ] 加 `@total-typescript/shoehorn` 的 import
   - [ ] 跑类型检查验证
