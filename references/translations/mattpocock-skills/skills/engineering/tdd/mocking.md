# 什么时候 mock

> 原文:[mocking.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/mocking.md)

**只在系统边界 mock**:

- 外部 API(支付、邮件等)
- 数据库(有时——优先用 test DB)
- 时间 / 随机
- 文件系统(有时)

**不要 mock**:

- 你自己的类 / 模块
- 内部协作方
- 你能控制的任何东西

## 为可 mock 而设计

在系统边界设计容易 mock 的接口:

**1. 用依赖注入**

把外部依赖传进来,不要在内部造:

```typescript
// 好 mock
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// 不好 mock
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

**2. 偏好 SDK 风格接口,而不是通用 fetcher**

为每个外部操作做具体函数,不要用一个带条件分支的通用函数:

```typescript
// 好:每个函数独立可 mock
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};

// 坏:mock 时要在 mock 内部加条件
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

SDK 风格的好处:

- 每个 mock 返回一个特定形状
- 测试 setup 里没有条件逻辑
- 容易看出测试演练了哪些 endpoint
- 每个 endpoint 有类型安全
