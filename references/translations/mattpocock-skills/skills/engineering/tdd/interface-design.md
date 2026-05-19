# 为可测试性设计接口

> 原文:[interface-design.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/interface-design.md)

好接口让测试自然:

1. **接受依赖,而不是自己造**

   ```typescript
   // 可测
   function processOrder(order, paymentGateway) {}

   // 难测
   function processOrder(order) {
     const gateway = new StripeGateway();
   }
   ```

2. **返回结果,而不是产生副作用**

   ```typescript
   // 可测
   function calculateDiscount(cart): Discount {}

   // 难测
   function applyDiscount(cart): void {
     cart.total -= discount;
   }
   ```

3. **小接口面**
   - 方法越少 → 要写的测试越少
   - 参数越少 → 测试 setup 越简单
