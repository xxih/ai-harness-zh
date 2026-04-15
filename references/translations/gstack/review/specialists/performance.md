# Performance Specialist Review Checklist

适用范围：当 `SCOPE_BACKEND=true` 或 `SCOPE_FRONTEND=true`
输出格式：每行一个 JSON finding。Schema：
`{"severity":"CRITICAL|INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"performance","summary":"...","fix":"...","fingerprint":"path:line:performance","specialist":"performance"}`

如果没有发现：只输出 `NO FINDINGS`，不要输出别的内容。

---

## 审查类别

### N+1 Queries
- ActiveRecord / ORM 关联在循环里被遍历，却没有 eager loading（`.includes`、`joinedload`、`include`）
- iteration block（`each`、`map`、`forEach`）内部继续查数据库，本可批量化
- 嵌套 serializer 触发 lazy-loaded associations
- GraphQL resolver 按字段逐个查，而不是批处理（检查 DataLoader 使用）

### 缺失数据库索引
- 新增 `WHERE` 条件所用列没有索引
- 新增 `ORDER BY` 落在未索引列上
- 复合查询（`WHERE a AND b`）却没复合索引
- 新增 foreign key 列没有索引

### 算法复杂度
- O(n^2) 或更差的模式：集合嵌套循环、`Array.map` 里再 `Array.find`
- 重复线性查找，本可改成 hash / map / set lookup
- 循环里做字符串拼接，本可 `join` 或 StringBuilder
- 大集合被重复排序 / 过滤，多次遍历本可合并成一次

### Bundle Size Impact（前端）
- 新引入重量级生产依赖（如 `moment.js`、整包 lodash、jquery）
- 使用 barrel import（`import from 'library'`）而非 deep import
- 大型静态资源（图片、字体）未经优化直接提交
- 路由级 chunk 缺 code splitting

### Rendering Performance（前端）
- Fetch waterfall，本可 `Promise.all` 并行
- render 中反复创建新对象 / 数组，导致不必要 rerender
- 昂贵计算缺 `React.memo`、`useMemo`、`useCallback`
- 循环中先读 DOM 再写 DOM，造成 layout thrashing
- 折叠以下图片缺 `loading="lazy"`

### 缺少分页
- 列表接口无上限返回结果，没有 `LIMIT` 或 pagination params
- 查询不带 `LIMIT`，会随数据量线性膨胀
- API 返回完整嵌套对象，而不是 ID + expansion 机制

### Async 上下文中的阻塞
- async 函数里做同步 I/O（文件读写、subprocess、HTTP 请求）
- event-loop handler 中直接 `time.sleep()` / `Thread.sleep()`
- CPU 重任务阻塞主线程，未卸载到 worker
