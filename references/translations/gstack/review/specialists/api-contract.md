# API Contract Specialist Review Checklist

适用范围：当 `SCOPE_API=true`
输出格式：每行一个 JSON finding。Schema：
`{"severity":"CRITICAL|INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"api-contract","summary":"...","fix":"...","fingerprint":"path:line:api-contract","specialist":"api-contract"}`

如果没有发现：只输出 `NO FINDINGS`，不要输出别的内容。

---

## 审查类别

### Breaking Changes
- 从 response body 中删除字段，客户端可能已经依赖这些字段
- 字段类型发生变化（string -> number、object -> array）
- 给现有 endpoint 新增必填参数
- HTTP method 或 status code 发生变化（如 `GET -> POST`、`200 -> 201`）
- 重命名 endpoint，却没有保留旧路径作为 redirect / alias
- 认证要求变化（public -> authenticated）

### Versioning Strategy
- 发生 breaking change，却没有 version bump（`v1 -> v2`）
- 同一个 API 混用多种 versioning strategy（URL、header、query param）
- 弃用 endpoint 时没有 sunset timeline 或 migration guide
- version-specific logic 分散在 controllers 里，而不是集中管理

### Error Response Consistency
- 新 endpoint 返回的错误格式和现有接口不一致
- 错误响应缺标准字段（错误码、message、details）
- HTTP status code 与错误类型不匹配（例如错误却返回 `200`，validation 问题却返回 `500`）
- 错误信息泄漏内部实现细节（stack trace、SQL 等）

### Rate Limiting & Pagination
- 新 endpoint 缺 rate limiting，而同类 endpoint 已有
- 从 offset 改成 cursor，但没有 backwards compatibility
- 改了 page size 或默认 limit，却没更新文档
- 分页响应里缺 total count 或 next-page indicator

### Documentation Drift
- OpenAPI / Swagger spec 没跟新 endpoint 或参数变化同步
- README 或 API docs 仍描述旧行为
- 示例请求 / 响应已经无法工作
- 新 endpoint 或参数变化没有文档

### Backwards Compatibility
- 老版本客户端是否会直接 break？
- 无法强制更新的移动端应用是否还能继续调用？
- webhook payload 已变化，但没有通知订阅方
- 要使用新功能时，SDK / client library 是否也必须同步改？
