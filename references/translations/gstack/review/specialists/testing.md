# Testing Specialist Review Checklist

适用范围：始终启用（每次 review 都跑）
输出格式：每行一个 JSON finding。Schema：
`{"severity":"CRITICAL|INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"testing","summary":"...","fix":"...","fingerprint":"path:line:testing","specialist":"testing"}`

如果没有发现：只输出 `NO FINDINGS`，不要输出别的内容。

---

## 审查类别

### 缺少负路径测试
- 新代码处理了 error、rejection 或 invalid input，但没有任何对应测试
- guard clause 与 early return 完全未测
- `try/catch`、`rescue` 或 error boundary 的失败分支没有 failure-path test
- 代码里写了 permission / auth check，但从没测过 “denied” 场景

### 缺少边界情况覆盖
- 边界值：`0`、负数、最大值、空字符串、空数组、`nil/null/undefined`
- 单元素集合（循环里常见 off-by-one）
- 面向用户输入中的 Unicode 和特殊字符
- 并发访问模式，但没有任何 race-condition test

### 测试隔离性违规
- 测试共享可变状态（类变量、全局单例、未清理 DB records）
- 测试依赖执行顺序（顺着跑能过，随机化后会挂）
- 测试依赖系统时钟、时区或 locale
- 测试直接打真实网络，而不是 stub / mock

### Flaky 测试模式
- 依赖时间的断言（`sleep`、`setTimeout`、超紧的 `waitFor`）
- 对无序结果顺序做断言（哈希键、`Set` 迭代、异步返回顺序）
- 依赖外部服务（API、数据库）且没有 fallback
- 随机测试数据没有 seed control

### 缺少安全强制测试
- controller 里的 auth / authz 校验，没有 “unauthorized” 场景测试
- rate limiting 逻辑没有测试证明它真的会拦截
- 输入净化没有恶意输入测试
- CSRF / CORS 配置缺 integration test

### Coverage Gaps
- 新的 public methods / functions 完全没有测试覆盖
- 被改动的方法，现有测试只覆盖旧行为，没覆盖新增分支
- 被多处调用的 utility functions 只被间接测试
