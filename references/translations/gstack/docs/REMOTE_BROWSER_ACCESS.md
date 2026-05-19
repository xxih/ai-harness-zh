# Remote Browser Access：如何配对一台 GStack Browser

GStack Browser server 可以共享给任何能发 HTTP 请求的 AI agent。
agent 会获得对真实 Chromium browser 的受限访问能力：访问页面、读取内容、
点击元素、填写表单、截图。每个 agent 都有自己的 tab。

这份文档是给 remote agents 用的参考说明。面向实际使用的 quick-start 指令由
`$B pair-agent` 生成，其中会内嵌真实凭证。

## 架构

```
Your Machine                          Remote Agent
─────────────                         ────────────
GStack Browser Server                 Any AI agent
  ├── Chromium (Playwright)           (OpenClaw, Hermes, Codex, etc.)
  ├── HTTP API on localhost:PORT           │
  ├── ngrok tunnel (optional)              │
  │     https://xxx.ngrok.dev ─────────────┘
  └── Token Registry
        ├── Root token (local only)
        ├── Setup keys (5 min, one-time)
        └── Session tokens (24h, scoped)
```

## 连接流程

1. **用户运行** `$B pair-agent`（或在 Claude Code 里运行 `/pair-agent`）
2. **Server 创建**一次性 setup key（5 分钟过期）
3. **用户复制**指令块到另一个 agent 的聊天里
4. **Remote agent 调用** `POST /connect`，携带 setup key
5. **Server 返回**一个受限的 session token（默认 24 小时）
6. **Remote agent 创建**自己的 tab，方式是向 `POST /command` 发送 `newtab`
7. **Remote agent 浏览**时，通过 `POST /command` 携带 session token + `tabId`

## API Reference

### Authentication

除 `/connect` 和 `/health` 外，所有 endpoints 都需要 Bearer token：

```
Authorization: Bearer gsk_sess_...
```

### Endpoints

#### POST /connect

把 setup key 换成 session token。无需 auth。限流为 3 次/分钟。

```json
Request:  {"setup_key": "gsk_setup_..."}
Response: {"token": "gsk_sess_...", "expires": "ISO8601", "scopes": ["read","write"], "agent": "agent-name"}
```

#### POST /command

发送 browser command。需要 Bearer auth。

```json
Request:  {"command": "goto", "args": ["https://example.com"], "tabId": 1}
Response: (plain text result of the command)
```

#### GET /health

返回 server status。无需 auth。会返回 status、tabs、mode、uptime。

### Commands

#### Navigation

| Command | Args | Description |
|---------|------|-------------|
| `goto` | `["URL"]` | 跳转到一个 URL |
| `back` | `[]` | 返回上一页 |
| `forward` | `[]` | 前进 |
| `reload` | `[]` | 刷新页面 |

#### Reading Content

| Command | Args | Description |
|---------|------|-------------|
| `snapshot` | `["-i"]` | 带 `@ref` 标签的交互式快照（最有用） |
| `text` | `[]` | 整页纯文本 |
| `html` | `["selector?"]` | 某个元素或整页的 HTML |
| `links` | `[]` | 页面上的全部链接 |
| `screenshot` | `["/tmp/s.png"]` | 截图 |
| `url` | `[]` | 当前 URL |

#### Interaction

| Command | Args | Description |
|---------|------|-------------|
| `click` | `["@e3"]` | 点击元素（使用 `snapshot` 里的 `@ref`） |
| `fill` | `["@e5", "text"]` | 填写表单字段 |
| `select` | `["@e7", "option"]` | 选择下拉框值 |
| `type` | `["text"]` | 键盘输入文本 |
| `press` | `["Enter"]` | 按一个按键 |
| `scroll` | `["down"]` | 滚动页面 |

#### Tabs

| Command | Args | Description |
|---------|------|-------------|
| `newtab` | `["URL?"]` | 创建一个新 tab（写操作前必须先做） |
| `tabs` | `[]` | 列出所有 tabs |
| `closetab` | `["id?"]` | 关闭一个 tab |

## Snapshot → @ref 模式

这是最强的浏览模式。不再去猜 CSS selector，而是：

1. 先运行 `snapshot -i`，拿到带标签的交互式快照
2. 快照会返回类似这样的文本：
   ```
   [Page Title]
   @e1 [link] "Home"
   @e2 [button] "Sign In"
   @e3 [input] "Search..."
   ```
3. 直接在命令里使用这些 `@e` refs：`click @e2`、`fill @e3 "search query"`

这就是 snapshot system 的工作方式，比猜 CSS selector 可靠得多。
默认先 `snapshot -i`，再使用 refs。

## Scopes

| Scope | 允许的内容 |
|-------|------------|
| `read` | `snapshot`、`text`、`html`、`links`、`screenshot`、`url`、`tabs`、`console` 等 |
| `write` | `goto`、`click`、`fill`、`scroll`、`newtab`、`closetab` 等 |
| `admin` | `eval`、`js`、`cookies`、`storage`、`cookie-import`、`useragent` 等 |
| `meta` | `tab`、`diff`、`frame`、`responsive`、`watch` |

默认 token 会带 `read` + `write`。只有在配对时显式使用 `--admin`，才会授予
`admin`。

## Tab Isolation

每个 agent 只拥有自己创建的 tabs。规则如下：

- **Read：** 任意 agent 都能读取任意 tab（`snapshot`、`text`、`screenshot`）
- **Write：** 只有 tab owner 能执行写操作（`click`、`fill`、`goto` 等）
- **Unowned tabs：** 预先存在的 tabs 只有 root 才能写
- **First step：** 想交互之前，先 `newtab`

## Error Codes

| Code | Meaning | What to do |
|------|---------|------------|
| 401 | Token 无效、过期或已撤销 | 让用户重新运行 `/pair-agent` |
| 403 | command 不在 scope 内，或该 tab 不归你所有 | 改用 `newtab`，或申请 `--admin` |
| 429 | 超过限流（>10 req/s） | 等待 `Retry-After` header |

## Security Model

- Setup keys 5 分钟后过期，且只能使用一次
- Session tokens 默认 24 小时后过期（可配置）
- Root token 永远不会出现在 instruction block 或 connection string 中
- `admin` scope（JS execution、cookie access）默认拒绝
- Tokens 可以即时撤销：`$B tunnel revoke agent-name`
- 所有 agent 活动都会记录 attribution（`clientId`）

## Same-Machine Shortcut

如果两个 agents 在同一台机器上，跳过复制粘贴流程：

```bash
$B pair-agent --local openclaw    # writes to ~/.openclaw/skills/gstack/browse-remote.json
$B pair-agent --local codex       # writes to ~/.codex/skills/gstack/browse-remote.json
$B pair-agent --local cursor      # writes to ~/.cursor/skills/gstack/browse-remote.json
```

不需要 tunnel。直接使用 localhost。

## ngrok Tunnel Setup

当 remote agent 在另一台机器上时：

1. 到 [ngrok.com](https://ngrok.com) 注册（free tier 足够）
2. 从 dashboard 复制你的 auth token
3. 保存它：`echo 'NGROK_AUTHTOKEN=your_token' > ~/.gstack/ngrok.env`
4. 如果想固定域名：`echo 'NGROK_DOMAIN=your-name.ngrok-free.dev' >> ~/.gstack/ngrok.env`
5. 用 tunnel 启动：`BROWSE_TUNNEL=1 $B restart`
6. 运行 `$B pair-agent`，它会自动使用 tunnel URL
