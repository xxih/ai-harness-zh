# Security Specialist Review Checklist

适用范围：当 `SCOPE_AUTH=true`，或（`SCOPE_BACKEND=true` 且 diff > 100 行）
输出格式：每行一个 JSON finding。Schema：
`{"severity":"CRITICAL|INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"security","summary":"...","fix":"...","fingerprint":"path:line:security","specialist":"security"}`

如果没有发现：只输出 `NO FINDINGS`，不要输出别的内容。

---

这个 checklist 比主流程里的 CRITICAL pass 更深入。主 agent 已经覆盖 SQL injection、race conditions、LLM trust boundary 和 enum completeness。这个 specialist 进一步聚焦 auth / authz、crypto misuse 与 attack surface expansion。

## 审查类别

### 信任边界上的输入校验
- controller / handler 层直接接收用户输入，却没有 validation
- query params 直接进入数据库查询或文件路径
- request body 字段没有 type checking 或 schema validation
- 文件上传没有类型 / 大小 / 内容校验
- webhook payload 未做签名校验就处理

### Auth 与授权绕过
- endpoint 缺认证 middleware（检查 route definitions）
- 授权判断默认是 allow，而不是 deny
- 存在角色提升路径（用户可以改自己的角色 / 权限）
- 直接对象引用漏洞（用户 A 改个 ID 就能访问用户 B 的数据）
- session fixation 或 hijacking 机会
- token / API key 校验不检查过期时间

### 注入向量（不止 SQL）
- 用户可控参数进入 subprocess，造成 command injection
- 用户输入进入模板，造成 template injection（Jinja2、ERB、Handlebars）
- 目录查询里的 LDAP injection
- 用户可控 URL 造成 SSRF（fetch、redirect、webhook targets）
- 用户可控文件路径造成 path traversal（`../../etc/passwd`）
- 用户可控值进入 HTTP headers，造成 header injection

### Cryptographic Misuse
- 在安全敏感场景里使用弱哈希（MD5、SHA1）
- 用可预测随机源（`Math.random`、`rand()`）生成 token 或 secret
- 用非常量时间比较（`==`）比较 secrets、tokens 或 digests
- 硬编码 encryption key 或 IV
- 密码哈希缺 salt

### Secrets 暴露
- 源码里出现 API keys、tokens 或 passwords，即使只是在 comments 里
- 应用日志或错误信息里打印 secrets
- 凭证出现在 URL 中（query params 或 basic auth URL）
- 返回给用户的错误响应里包含敏感数据
- 本该加密的 PII 却明文存储

### XSS Escape Hatches
- Rails：对用户可控数据用 `.html_safe`、`raw()`
- React：`dangerouslySetInnerHTML` 注入用户内容
- Vue：`v-html` 注入用户内容
- Django：对用户输入使用 `|safe`、`mark_safe()`
- 通用情况：把未经清洗的数据塞进 `innerHTML`

### 反序列化
- 反序列化不可信数据（`pickle`、`Marshal`、`YAML.load`、可执行类型的 `JSON.parse`）
- 从用户输入或外部 API 接收序列化对象，但没有 schema validation
