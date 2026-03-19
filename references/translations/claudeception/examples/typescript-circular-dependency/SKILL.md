---
name: typescript-circular-dependency
description: |
  检测并解决 TypeScript/JavaScript 的循环导入依赖。适用于：
  (1) 运行时报 `Cannot access 'X' before initialization`，
  (2) import 意外得到 undefined，
  (3) `ReferenceError: Cannot access X before initialization`，
  (4) 调整 import 顺序后类型错误消失，(5) Jest/Vitest 测试里 import 是 undefined，浏览器里却正常。
author: Claude Code
version: 1.0.0
date: 2024-03-10
---

# TypeScript 循环依赖检测与修复

## 问题

循环依赖是指模块 A 从模块 B 导入，而模块 B 又直接或间接地从模块 A 导入。TypeScript 往往可以顺利编译，但到了运行时，其中一个 import 会变成 `undefined`，因为对应模块还没有完成初始化。

## 上下文 / 触发条件

常见报错：

```
ReferenceError: Cannot access 'UserService' before initialization
```

```
TypeError: Cannot read properties of undefined (reading 'create')
```

```
TypeError: (0 , _service.doSomething) is not a function
```

暗示循环导入的症状：

- export 明明存在，但 import 结果却是 `undefined`
- TypeScript 编译阶段没问题，运行时才报错
- 挪动 import 语句后，变成另一个 import 是 `undefined`
- 测试失败，但应用能跑（或反过来）
- 在文件顶部加个 `console.log` 就会改变行为

## 解决方案

### 第 1 步：检测循环

使用工具可视化依赖关系：

```bash
# Install madge
npm install -g madge

# Find circular dependencies
madge --circular --extensions ts,tsx src/

# Generate visual graph
madge --circular --image graph.svg src/
```

也可以借助 TypeScript 编译器：

```bash
# Check for cycles (requires tsconfig setting)
npx tsc --listFiles | head -50
```

### 第 2 步：识别模式

常见循环依赖模式：

**模式 A：Service-to-Service**
```
services/userService.ts -> services/orderService.ts -> services/userService.ts
```

**模式 B：Type imports**
```
types/user.ts -> types/order.ts -> types/user.ts
```

**模式 C：Index barrel files**
```
components/index.ts -> components/Button.tsx -> components/index.ts
```

### 第 3 步：选择修复策略

**策略 1：提取共享依赖**

Before:
```typescript
// userService.ts
import { OrderService } from './orderService';
export class UserService { ... }

// orderService.ts  
import { UserService } from './userService';
export class OrderService { ... }
```

After:
```typescript
// types/interfaces.ts (new file - no imports from services)
export interface IUserService { ... }
export interface IOrderService { ... }

// userService.ts
import { IOrderService } from '../types/interfaces';
export class UserService implements IUserService { ... }
```

**策略 2：依赖注入**

```typescript
// orderService.ts
export class OrderService {
  constructor(private userService: IUserService) {}
  
  // Instead of importing UserService directly
}

// main.ts
const userService = new UserService();
const orderService = new OrderService(userService);
```

**策略 3：动态导入**

```typescript
// Only import when needed, not at module level
async function processOrder() {
  const { UserService } = await import('./userService');
  // ...
}
```

**策略 4：使用 type-only imports**

如果你只需要类型、不需要运行时值，使用 type-only import：

```typescript
// This doesn't create a runtime dependency
import type { User } from './userService';
```

**策略 5：重构 barrel files**

Before（有问题）：
```typescript
// components/index.ts
export * from './Button';
export * from './Modal';  // Modal imports Button from './index'
```

After：
```typescript
// components/Modal.tsx
import { Button } from './Button';  // Direct import, not from index
```

### 第 4 步：防止将来再出现循环

加入 CI / build 检查：

```json
// package.json
{
  "scripts": {
    "check:circular": "madge --circular --extensions ts,tsx src/"
  }
}
```

或者配置 ESLint：

```javascript
// .eslintrc.js
module.exports = {
  plugins: ['import'],
  rules: {
    'import/no-cycle': ['error', { maxDepth: 10 }]
  }
}
```

## 验证

1. 运行 `madge --circular src/`，应不再报告循环
2. 跑测试套件，之前的 undefined import 应恢复正常
3. 删除 `node_modules` 后重新安装，应用仍然能跑
4. 做一次生产构建，不再出现运行时错误

## 示例

**问题**：在 `UserService` 中导入 `OrderService` 时，`OrderService` 是 `undefined`

**检测**：
```bash
$ madge --circular src/
Circular dependencies found!
  src/services/userService.ts -> src/services/orderService.ts -> src/services/userService.ts
```

**修复**：提取共享接口

```typescript
// NEW: src/types/services.ts
export interface IOrderService {
  createOrder(userId: string): Promise<Order>;
}

// MODIFIED: src/services/userService.ts
import type { IOrderService } from '../types/services';

export class UserService {
  constructor(private orderService: IOrderService) {}
}
```

## 备注

- 循环依赖在 barrel exports 和大型 service 层里尤其常见
- `import type` 只能解决纯类型依赖，解决不了运行时值依赖
- 某些 bundler 会掩盖问题，直到测试、SSR 或生产环境才暴露
- 如果循环很深，优先从架构边界下手，而不是继续堆 workaround
