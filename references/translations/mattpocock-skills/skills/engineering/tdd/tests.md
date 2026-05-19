# 好测试与坏测试

> 原文:[tests.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/tests.md)

## 好测试

**集成风格**:通过真实接口测,不 mock 内部部件。

```typescript
// 好:测可观测行为
test("user can checkout with valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

特征:

- 测用户/调用方关心的行为
- 只用公共 API
- 能在内部重构中存活
- 描述 WHAT,不是 HOW
- 每个测试一个逻辑断言

## 坏测试

**实现细节测试**:和内部结构耦合。

```typescript
// 坏:测实现细节
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

警告信号:

- mock 内部协作方
- 测私有方法
- 断言调用次数 / 顺序
- 重构(没改行为)就让测试坏
- 测试名描述 HOW 而不是 WHAT
- 不走接口、通过外部手段验证

```typescript
// 坏:绕过接口验证
test("createUser saves to database", async () => {
  await createUser({ name: "Alice" });
  const row = await db.query("SELECT * FROM users WHERE name = ?", ["Alice"]);
  expect(row).toBeDefined();
});

// 好:走接口验证
test("createUser makes user retrievable", async () => {
  const user = await createUser({ name: "Alice" });
  const retrieved = await getUser(user.id);
  expect(retrieved.name).toBe("Alice");
});
```
