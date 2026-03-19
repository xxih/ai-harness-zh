---
name: prisma-connection-pool-exhaustion
description: |
  修复 Prisma 在 serverless 环境中的 “Too many connections” 和连接池耗尽错误，
  适用于 Vercel、AWS Lambda、Netlify。适用场景：
  (1) 报错 `P2024: Timed out fetching a new connection from the pool`，
  (2) PostgreSQL 报 `too many connections for role`，
  (3) 本地正常、生产 serverless 出错，(4) 有流量时出现间歇性数据库超时。
author: Claude Code
version: 1.0.0
date: 2024-02-20
---

# Serverless 中的 Prisma 连接池耗尽

## 问题

Serverless function 会在每次冷启动时新建一个 Prisma client 实例。每个实例都会打开多个数据库连接（默认每个实例 5 个）。当并发请求增多时，很快就会耗尽数据库连接上限（托管数据库通常只有 20-100 个）。

## 上下文 / 触发条件

当你看到下面情况时，这个 skill 适用：

- `P2024: Timed out fetching a new connection from the connection pool`
- PostgreSQL：`FATAL: too many connections for role "username"`
- MySQL：`Too many connections`
- 本地用 `npm run dev` 没问题，但生产环境失败
- 流量高峰时出现错误，随后又自行恢复
- 数据库面板显示连接数接近或达到上限

环境特征：
- 部署在 Vercel、AWS Lambda、Netlify Functions 或类似平台
- 使用 Prisma 配合 PostgreSQL、MySQL 或其他基于连接的数据库
- 数据库是托管服务（PlanetScale、Supabase、Neon、RDS 等）

## 解决方案

### 第 1 步：使用连接池服务

推荐方案是使用类似 PgBouncer 或 Prisma Accelerate 的连接池中间层，把 serverless functions 和数据库隔开。

**对于 Supabase：**
```
# .env
# Use the pooled connection string (port 6543, not 5432)
DATABASE_URL="postgresql://user:pass@db.xxx.supabase.co:6543/postgres?pgbouncer=true"
```

**对于 Neon：**
```
# .env  
DATABASE_URL="postgresql://user:pass@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require"
# Neon has built-in pooling
```

**对于 Prisma Accelerate：**
```bash
npx prisma generate --accelerate
```

### 第 2 步：配置 Prisma 连接限制

在你的 `schema.prisma` 里：

```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
  // Limit connections per Prisma instance
  relationMode = "prisma"
}
```

在连接 URL 或 Prisma client 里增加限制：

```typescript
// lib/prisma.ts
import { PrismaClient } from '@prisma/client'

const globalForPrisma = global as unknown as { prisma: PrismaClient }

export const prisma = globalForPrisma.prisma || new PrismaClient({
  datasources: {
    db: {
      url: process.env.DATABASE_URL + '?connection_limit=1'
    }
  }
})

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma
```

### 第 3 步：单例模式（开发环境）

避免热重载不断创建新 client：

```typescript
// lib/prisma.ts
import { PrismaClient } from '@prisma/client'

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

export const prisma = globalForPrisma.prisma ?? new PrismaClient()

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma
```

### 第 4 步：URL 参数

给连接串加上这些参数：

```
?connection_limit=1&pool_timeout=20&connect_timeout=10
```

- `connection_limit=1`：每个 serverless 实例只保留一个连接
- `pool_timeout=20`：最多等待 20 秒获取空闲连接
- `connect_timeout=10`：10 秒内连不上就快速失败

## 验证

应用修复后：

1. 部署到生产环境
2. 做一次压测：`npx autocannon -c 100 -d 30 https://your-app.com/api/test`
3. 查看数据库控制台，连接数应保持在上限以内
4. 日志里不再出现 P2024 错误

## 示例

**修复前**（负载下报错）：
```
[ERROR] PrismaClientKnownRequestError:
Invalid `prisma.user.findMany()` invocation:
Timed out fetching a new connection from the connection pool.
```

**修复后**（启用连接池）：
```
# Using Supabase pooler URL
DATABASE_URL="postgresql://...@db.xxx.supabase.co:6543/postgres?pgbouncer=true&connection_limit=1"
```

即使在高负载下，数据库连接数也稳定在 10-15 左右。

## 备注

- 不同托管数据库提供的连接池方案不同，先查你所用服务商文档
- PlanetScale（MySQL）采用不同架构，通常不会遇到同样的问题
- `connection_limit=1` 很激进，建议从这里开始，再根据延迟逐步调高
- 单例模式只对开发环境有帮助；在生产 serverless 中，每个实例彼此隔离
- 如果 Prisma 搭配 Next.js API routes 使用，每次 route 调用都可能对应独立的 serverless function
- 如需内建缓存和连接池，可考虑 Prisma Accelerate：https://www.prisma.io/accelerate
