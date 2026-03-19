---
name: nextjs-server-side-error-debugging
description: |
  调试 Next.js 中的 getServerSideProps 和 getStaticProps 错误。适用于：
  (1) 页面显示通用错误，但浏览器控制台为空，(2) API route 返回 500 却没有细节，
  (3) 服务端代码静默失败，(4) 只在刷新时出错，客户端导航时不出错。
  这种情况下应查看终端/服务端日志，而不是浏览器中的报错。
author: Claude Code
version: 1.0.0
date: 2024-01-15
---

# Next.js 服务端错误调试

## 问题

Next.js 的服务端错误不会显示在浏览器控制台里。如果你一直盯着错误的地方看，调试过程就会非常痛苦。浏览器通常只会显示通用错误页或 500 状态，但 DevTools 里没有堆栈，也没有有用的错误信息。

## 上下文 / 触发条件

当出现下面情况时，这个 skill 适用：

- 页面显示 `Internal Server Error` 或自定义错误页
- 浏览器控制台没有错误，或者只有一个很泛的 fetch 失败
- 你在使用 `getServerSideProps`、`getStaticProps` 或 API routes
- 错误只在页面刷新或直接访问时出现（客户端切换路由时不出现）
- 错误是间歇性的，很难在浏览器里复现

常见的误导性症状：
- 出现 `Unhandled Runtime Error` 弹层，但没有显示真正原因
- Network 面板看到 500，但响应体为空或只有通用信息
- 一加 `console.log` 错误就消失（时序问题）

## 解决方案

### 第 1 步：先看终端

真正的错误和完整堆栈会出现在运行 `npm run dev` 或 `next dev` 的终端里。这是**第一优先级排查点**。

```bash
# If you don't see the terminal, find the process
ps aux | grep next
# Or restart with visible output
npm run dev
```

### 第 2 步：加上显式错误处理

如果需要持续调试，把服务端代码包上 try-catch：

```typescript
export async function getServerSideProps(context) {
  try {
    const data = await fetchSomething();
    return { props: { data } };
  } catch (error) {
    console.error('getServerSideProps error:', error);
    // Return error state instead of throwing
    return { props: { error: error.message } };
  }
}
```

### 第 3 步：处理生产环境错误

去看你的托管平台日志：
- **Vercel**：Dashboard -> Project -> Logs（Functions tab）
- **AWS**：CloudWatch Logs
- **Netlify**：Dashboard 里的 Functions tab
- **Self-hosted**：查看 Node.js 进程日志

### 第 4 步：常见根因

1. **环境变量**：生产环境缺失，本地却存在
2. **数据库连接**：连接串问题、冷启动
3. **导入错误**：本该只在服务端运行的代码被错误导入到客户端
4. **Async/await**：异步操作漏写 `await`
5. **JSON 序列化**：对象无法被序列化（如日期、函数）

## 验证

看过终端之后，你应该能看到：
- 带文件名和行号的完整堆栈
- 真正的错误信息（而不是通用 500）
- 如果你加了 `console.log`，也能看到对应变量值

## 示例

**症状**：用户反馈点击链接后页面显示 `Internal Server Error`。

**排查过程**：
1. 打开浏览器 DevTools -> Console：空的
2. Network 面板显示：`GET /dashboard -> 500`
3. 查看运行 `npm run dev` 的终端：

```
Error: Cannot read property 'id' of undefined
    at getServerSideProps (/app/pages/dashboard.tsx:15:25)
    at renderToHTML (/app/node_modules/next/dist/server/render.js:428:22)
```

**最终原因**：数据库查询返回了 `null`，而不是用户对象。

## 备注

- 在开发环境里，Next.js 有时会弹错误 overlay，但细节往往还是不如终端日志完整
- `next.config.js` 里的 `reactStrictMode: true` 会导致开发环境下服务端函数双执行，让调试更容易混淆
- 对 API routes 来说，错误会出现在和页面错误同一个终端里
- 客户端错误（例如 `useEffect`、事件处理器里的错误）**会**显示在浏览器控制台——这个 skill 只适用于服务端代码
- 如果你本地跑的是 `next start`（生产模式），错误可能没那么详细；检查 `NODE_ENV`，必要时加上自定义错误日志
