# Pre-Landing Review Checklist

## 使用说明

针对 `git diff origin/main` 的输出，按下面列出的风险项做审查。要具体，给出 `file:line`，并提出修复建议。没问题的地方直接跳过。只报真实问题。

**两阶段审查：**
- **Pass 1（CRITICAL）：** 先跑 SQL & Data Safety、Race Conditions、LLM Output Trust Boundary、Shell Injection、Enum Completeness。这些是最高优先级。
- **Pass 2（INFORMATIONAL）：** 再跑下面其余类别。严重性更低，但仍然要处理。
- **Specialist categories（并行子 agent 负责，不走本清单）：** Test Gaps、Dead Code、Magic Numbers、Conditional Side Effects、Performance & Bundle Impact、Crypto & Entropy。见 `review/specialists/`。

所有 findings 最终都走 Fix-First Review：显然的机械修复自动落地，真正有歧义的问题再合并成一次用户提问。

**输出格式：**

```text
Pre-Landing Review: N issues (X critical, Y informational)

**AUTO-FIXED:**
- [file:line] 问题 -> 已应用修复

**NEEDS INPUT:**
- [file:line] 问题描述
  Recommended fix: 建议修复方案
```

如果没有发现问题：`Pre-Landing Review: No issues found.`

保持简洁。每个问题只要两行：一行说问题，一行说修法。不要加前言、总结，也不要说 “looks good overall”。

---

## 审查类别

### Pass 1 — CRITICAL

#### SQL & Data Safety
- SQL 中使用字符串插值，即便值已经 `.to_i` / `.to_f`，也要改成参数化查询（Rails：`sanitize_sql_array` / Arel；Node：prepared statements；Python：parameterized queries）
- TOCTOU races：先检查再写入的模式，如果本应使用原子 `WHERE` + `update_all`，就要指出
- 直接写 DB 绕过 model validation（Rails：`update_column`；Django：`QuerySet.update()`；Prisma：raw queries）
- N+1 queries：循环 / 视图里访问关联，但没做 eager loading（Rails：`.includes()`；SQLAlchemy：`joinedload()`；Prisma：`include`）

#### Race Conditions & Concurrency
- read-check-write，但既没有唯一约束，也没有捕获 duplicate key error 并重试（例如 `where(hash:).first` 然后 `save!`，却没处理并发插入）
- find-or-create 却没有 unique DB index，并发调用可能造出重复记录
- 状态流转没有使用原子 `WHERE old_status = ? UPDATE SET new_status`，并发更新可能跳过某个状态或重复执行
- 对用户可控数据做 unsafe HTML rendering（Rails：`.html_safe` / `raw()`；React：`dangerouslySetInnerHTML`；Vue：`v-html`；Django：`|safe` / `mark_safe`），存在 XSS 风险

#### LLM Output Trust Boundary
- LLM 生成的值（邮箱、URL、姓名等）直接写库或传给 mailer，但没有做格式校验。持久化前应补最轻量的 guard（如 `EMAIL_REGEXP`、`URI.parse`、`.strip`）
- 结构化 tool output（数组、哈希）在写 DB 前没有做 type / shape checks
- 没有 allowlist 就去抓取 LLM 生成的 URL，如果地址指向内网，会有 SSRF 风险（Python：`urllib.parse.urlparse` 后检查 hostname，再决定是否 `requests.get` / `httpx.get`）
- LLM 输出未经清洗就存进 knowledge base 或 vector DB，存在 stored prompt injection 风险

#### Shell Injection（Python 专项）
- `subprocess.run()` / `subprocess.call()` / `subprocess.Popen()` 使用了 `shell=True`，同时命令字符串里还有 f-string / `.format()` 插值，应该改成参数数组
- `os.system()` 拼接变量，应改成 `subprocess.run()` + 参数数组
- 对 LLM 生成的代码直接 `eval()` / `exec()`，且没有 sandbox

#### Enum & Value Completeness
当 diff 引入新的 enum value、status string、tier name 或 type constant 时：
- **顺着每个 consumer 读透。** 不只是 grep，要真正读每个 `switch`、filter、display 该值的文件。如果任一 consumer 没处理新值，就报。常见漏点：前端 dropdown 新增一个值，但后端 model / compute 方法没有持久化它。
- **检查 allowlists / filter arrays。** 搜包含相邻值的数组或 `%w[]` 列表。比如新加 `"revise"` 到 tiers，就去找所有 `%w[quick lfg mega]`，确认需要纳入的地方都加了。
- **检查 `case` / `if-elsif` 分支。** 现有分支逻辑遇到新值时，会不会悄悄掉进错误默认值？
为完成这一步：用 `Grep` 找相邻值的所有引用（例如搜 `"lfg"` 或 `"mega"`，找出所有 tier consumers），并逐个读。这个步骤要求阅读 diff 之外的代码。

### Pass 2 — INFORMATIONAL

#### Async/Sync Mixing（Python 专项）
- 在 `async def` endpoint 里直接调用同步 `subprocess.run()`、`open()`、`requests.get()`，会阻塞 event loop，应改成 `asyncio.to_thread()`、`aiofiles` 或 `httpx.AsyncClient`
- 在 async 函数里用 `time.sleep()`，应改成 `asyncio.sleep()`
- async 上下文里做同步 DB 调用，但没用 `run_in_executor()` 包装

#### Column / Field Name Safety
- 核对 ORM 查询里的列名（`.select()`、`.eq()`、`.gte()`、`.order()`）是否真的存在于 DB schema 里，错列名有时会静默返回空结果，或抛错后被吞掉
- 检查查询结果上的 `.get()` 是否取了真正被选出来的字段
- 有 schema 文档时，和文档交叉核对

#### Dead Code & Consistency（仅 version / changelog，其他可维护性问题由 specialist 处理）
- PR 标题与 `VERSION` / `CHANGELOG` 文件里的版本不一致
- `CHANGELOG` 描述与真实改动不符，比如写“从 X 改成 Y”，但 X 根本没出现过

#### LLM Prompt Issues
- prompt 里写 0-indexed lists，LLM 往往会按 1-indexed 返回
- prompt 文本列出的工具 / 能力，与实际接线到 `tool_classes` / `tools` 数组中的不一致
- 词数 / token 限制在多处重复声明，存在漂移风险

#### Completeness Gaps
- 走了 shortcut implementation，但要做成完整版本只需要不到 30 分钟 CC 时间，例如 enum handling 不完整、error path 漏补、边界情况没补齐
- 给出的 options 只有 human-team effort estimate，没有同时给 human 和 CC+gstack 两种时间估算
- 测试覆盖缺口属于 “lake” 不是 “ocean”，例如缺负路径测试、缺和 happy-path 结构平行的 edge case tests
- 功能只做到了 80-90%，但其实只要多写一点代码就能做到 100%

#### Time Window Safety
- 按日期 key 查“今天”的数据，但默认把“今天”当完整 24 小时，导致比如美西早上 8 点只能看到午夜到 8 点的数据
- 相关功能之间时间窗口不一致，一个用 hourly buckets，另一个却对同一份数据按 daily keys 读

#### Type Coercion at Boundaries
- 值跨 Ruby -> JSON -> JS 边界时类型可能变化（数字 vs 字符串），尤其影响 hash / digest 输入
- hash / digest 输入没有显式 `.to_s` 或等价标准化，像 `{ cores: 8 }` 和 `{ cores: "8" }` 会算出不同摘要

#### View / Frontend
- partial 里内联 `<style>`，每次 render 都会重复解析
- view 中出现 O(n*m) 查找，例如循环里不断 `Array#find`，本应先建 `index_by` 哈希
- 已经拿到 DB 结果后再在 Ruby 侧 `.select{}` 过滤，本可下推成 `WHERE` 子句，除非是有意规避 leading-wildcard `LIKE`

#### Distribution & CI/CD Pipeline
- CI/CD workflow 改动（`.github/workflows/`）：检查 build tool 版本是否符合项目要求、artifact 名称 / 路径是否正确、secrets 是否用 `${{ secrets.X }}` 而不是写死
- 新增 artifact 类型（CLI binary、library、package）：确认是否存在 publish / release workflow，且目标平台正确
- 跨平台构建：确认 CI matrix 覆盖了所有目标 OS / arch，或者明确写了哪些平台没测
- 版本 tag 格式一致性：`v1.2.3` vs `1.2.3`，必须在 `VERSION`、git tags、publish scripts 中一致
- publish step 的幂等性：workflow 重跑时不应直接失败，例如 `gh release create` 前是否先 `gh release delete`

**不要报：**
- 已经有自动部署流水线的 web services（Docker build + K8s deploy）
- 只在团队内部使用、不对外分发的内部工具
- 仅测试相关的 CI 改动（新增 test steps，而不是 publish steps）

---

## 严重性分类

```text
CRITICAL（最高优先级）：         INFORMATIONAL（主 agent）：        SPECIALIST（并行子 agent）：
├─ SQL & Data Safety            ├─ Async/Sync Mixing             ├─ Testing specialist
├─ Race Conditions & Concurrency├─ Column/Field Name Safety      ├─ Maintainability specialist
├─ LLM Output Trust Boundary    ├─ Dead Code (version only)      ├─ Security specialist
├─ Shell Injection              ├─ LLM Prompt Issues             ├─ Performance specialist
└─ Enum & Value Completeness    ├─ Completeness Gaps             ├─ Data Migration specialist
                                ├─ Time Window Safety            ├─ API Contract specialist
                                ├─ Type Coercion at Boundaries   └─ Red Team (conditional)
                                ├─ View/Frontend
                                └─ Distribution & CI/CD Pipeline

所有 findings 最终都走 Fix-First Review。
严重性决定展示顺序，也影响 AUTO-FIX 与 ASK 的归类：
critical findings 更偏向 ASK，informational findings 更偏向 AUTO-FIX。
```

---

## Fix-First Heuristic

这个启发式规则同时被 `/review` 和 `/ship` 引用，用来决定 agent 是自动修复，还是交给用户判断。

```text
AUTO-FIX（无需询问直接修）：        ASK（需要人工判断）：
├─ Dead code / unused variables   ├─ Security（auth、XSS、injection）
├─ N+1 queries                    ├─ Race conditions
├─ 过时且与代码矛盾的注释           ├─ Design decisions
├─ Magic numbers -> named const   ├─ Large fixes（>20 lines）
├─ 缺失的 LLM output validation   ├─ Enum completeness
├─ Version / path mismatches      ├─ 删除已有功能
├─ 赋值后从未读取的变量             └─ 任何改变用户可见行为的修改
└─ Inline styles、O(n*m) 查找
```

**经验法则：** 如果修复是机械性的，而且资深工程师一般不会犹豫，归到 `AUTO-FIX`。如果合理的工程师可能会对方案有分歧，归到 `ASK`。

**Critical findings 默认更偏 `ASK`**，因为风险更高。
**Informational findings 默认更偏 `AUTO-FIX`**，因为通常更机械。

---

## Suppressions — 这些不要报

- “X 和 Y 冗余”，但这种冗余是无害的、还能提升可读性，例如 `present?` 与 `length > 20` 同时存在
- “给这个阈值 / 常量加个注释解释原因”，这类阈值会在调参时不断变，注释很容易腐烂
- “这个 assertion 可以更 tight”，但它已经覆盖了实际行为
- 只为追求“统一风格”的建议，比如让某个值也包上一层条件判断，只是为了和另一个常量长得一样
- “Regex 没处理边界情况 X”，但输入约束保证现实里不会出现 X
- “测试一次覆盖了多个 guard”，这没问题，测试不需要强行把每个 guard 都拆开验证
- Eval 阈值变化（`max_actionable`、最小分数等），这类参数本来就会频繁经验性调优
- 无害 no-op，例如对一个永远不会在数组里的元素调用 `.reject`
- **你正在 review 的 diff 里已经解决过的任何问题**，先把完整 diff 读完再评论
