# Greptile Comment Triage

供 `/review`（Step 2.5）与 `/ship`（Step 3.75）共用的参考文档，用来抓取、过滤并分类 GitHub PR 上的 Greptile review comments。

---

## 抓取

先运行下面两条命令，识别当前 PR 并取回评论。两次 API 调用并行执行。

```bash
REPO=$(gh repo view --json nameWithOwner --jq '.nameWithOwner' 2>/dev/null)
PR_NUMBER=$(gh pr view --json number --jq '.number' 2>/dev/null)
```

**如果任一命令失败或返回空值：** 静默跳过 Greptile triage。这个集成是增强项，没有它流程也能继续。

```bash
# 并行抓取行级 review comments 和顶层 PR comments
gh api repos/$REPO/pulls/$PR_NUMBER/comments \
  --jq '.[] | select(.user.login == "greptile-apps[bot]") | select(.position != null) | {id: .id, path: .path, line: .line, body: .body, html_url: .html_url, source: "line-level"}' > /tmp/greptile_line.json &
gh api repos/$REPO/issues/$PR_NUMBER/comments \
  --jq '.[] | select(.user.login == "greptile-apps[bot]") | {id: .id, body: .body, html_url: .html_url, source: "top-level"}' > /tmp/greptile_top.json &
wait
```

**如果 API 报错，或者两个端点总共 0 条 Greptile 评论：** 也静默跳过。

其中行级评论里的 `position != null` 过滤，会自动跳过那些因为 force-push 而过期的 comments。

---

## Suppressions Check

先推导项目级 history 文件路径：

```bash
REMOTE_SLUG=$(browse/bin/remote-slug 2>/dev/null || ~/.claude/skills/gstack/browse/bin/remote-slug 2>/dev/null || basename "$(git rev-parse --show-toplevel 2>/dev/null || pwd)")
PROJECT_HISTORY="$HOME/.gstack/projects/$REMOTE_SLUG/greptile-history.md"
```

如果 `$PROJECT_HISTORY` 存在，就读它。这里存的是项目级 suppressions。每一行记录一次历史 triage 结论：

```text
<date> | <repo> | <type:fp|fix|already-fixed> | <file-pattern> | <category>
```

**Categories**（固定集合）：
`race-condition`、`null-check`、`error-handling`、`style`、`type-safety`、`security`、`performance`、`correctness`、`other`

对每一条抓回来的 comment，检查是否匹配下面条件的历史记录：
- `type == fp`，也就是只 suppress 已知 false positives，不 suppress 之前修过的真实问题
- `repo` 与当前 repo 一致
- `file-pattern` 能匹配当前 comment 的文件路径
- `category` 与评论中对应的问题类型一致

匹配上的 comment 直接标记为 **SUPPRESSED** 并跳过。

如果 history 文件不存在，或里面有无法解析的行，就跳过这些行继续执行。绝不能因为 suppressions 文件格式坏了而让流程失败。

---

## 分类

对每一条未被 suppress 的 comment：

1. **行级评论：** 读取 `path:line` 以及前后各 10 行上下文
2. **顶层评论：** 直接通读整条 comment body
3. 把评论与完整 diff（`git diff origin/main`）以及 review checklist 交叉核对
4. 归类为：
   - **VALID & ACTIONABLE**：当前代码里确实存在的 bug、race condition、安全或正确性问题
   - **VALID BUT ALREADY FIXED**：这个问题是真实的，但已经在分支后续提交里修掉了；需要指出修复 commit SHA
   - **FALSE POSITIVE**：评论误解了代码、报了其他地方已处理的情况，或者只是样式噪音
   - **SUPPRESSED**：已在上一步 suppressions check 中过滤

---

## Reply APIs

回复 Greptile 评论时，要根据评论来源使用不同 API：

**行级评论**（来自 `pulls/$PR/comments`）：

```bash
gh api repos/$REPO/pulls/$PR_NUMBER/comments/$COMMENT_ID/replies \
  -f body="<reply text>"
```

**顶层评论**（来自 `issues/$PR/comments`）：

```bash
gh api repos/$REPO/issues/$PR_NUMBER/comments \
  -f body="<reply text>"
```

**如果回复 POST 失败**（比如 PR 已关闭、当前账号无写权限）：给出 warning 后继续。不要让失败回复阻断整个 workflow。

---

## 回复模板

所有 Greptile 回复都用下面的模板。必须带具体证据，不能发空泛回应。

### Tier 1（首次回复）— 友好、但证据充分

**FIXES（用户选择修复）**

````text
**Fixed** in `<commit-sha>`.

```diff
- <old problematic line(s)>
+ <new fixed line(s)>
```

**Why:** <用 1 句话说明原问题，以及修复为什么有效>
````

**ALREADY FIXED（问题已在本分支先前提交中修掉）**

```text
**Already fixed** in `<commit-sha>`.

**What was done:** <1-2 句话说明现有提交是如何覆盖这个问题的>
```

**FALSE POSITIVE（评论判断错误）**

```text
**Not a bug.** <用 1 句话直接说明为什么这条判断不成立>

**Evidence:**
- <具体代码引用，证明这段模式是安全 / 正确的>
- <例如："The nil check is handled by `ActiveRecord::FinderMethods#find` which raises RecordNotFound, not nil">

**Suggested re-rank:** This appears to be a `<style|noise|misread>` issue, not a `<what Greptile called it>`. Consider lowering severity.
```

### Tier 2（Greptile 在已有回复后继续追打）— 更强硬，证据拉满

当下面的 escalation detection 发现同一线程里已经有过 GStack 回复时，使用 Tier 2 模板，目标是彻底结束争议。

````text
**This has been reviewed and confirmed as [intentional/already-fixed/not-a-bug].**

```diff
<full relevant diff showing the change or safe pattern>
```

**Evidence chain:**
1. <file:line permalink，指向安全模式或修复点>
2. <对应 commit SHA，如果适用>
3. <architecture rationale 或 design decision，如果适用>

**Suggested re-rank:** Please recalibrate — this is a `<actual category>` issue, not `<claimed category>`. [如有帮助，可附具体文件变更 permalink]
````

---

## Escalation Detection

在真正组装回复前，先检查这个 comment thread 里是否已经有过 GStack 回复：

1. **行级评论：** 通过 `gh api repos/$REPO/pulls/$PR_NUMBER/comments/$COMMENT_ID/replies` 取回 replies，检查其中是否存在带 GStack 标记的内容，例如 `**Fixed**`、`**Not a bug.**`、`**Already fixed**`
2. **顶层评论：** 在抓回来的 issue comments 里查找 Greptile 评论之后、且带 GStack 标记的回复
3. **如果已经有过 GStack 回复，并且 Greptile 又在同一 file + category 上继续追：** 使用 Tier 2
4. **如果没有历史 GStack 回复：** 使用 Tier 1

如果 escalation detection 本身失败（API 报错、线程归属不清），默认用 Tier 1。不要在模糊情况下升级语气。

---

## Severity Assessment & Re-ranking

在分类评论时，同时要判断 Greptile 暗示的严重性是否符合现实：

- 如果 Greptile 把某个问题说成 **security / correctness / race-condition**，但实际只是 **style / performance** 级别的提示，要在回复里带上 `**Suggested re-rank:**`
- 如果 Greptile 把低严重度的样式问题包装得像 critical，也要明确 push back
- 重排级别时必须给出具体理由，引用代码和行号，而不是表达观点

---

## History File Writes

写历史前，先确保两个目录都存在：

```bash
REMOTE_SLUG=$(browse/bin/remote-slug 2>/dev/null || ~/.claude/skills/gstack/browse/bin/remote-slug 2>/dev/null || basename "$(git rev-parse --show-toplevel 2>/dev/null || pwd)")
mkdir -p "$HOME/.gstack/projects/$REMOTE_SLUG"
mkdir -p ~/.gstack
```

每条 triage 结论都要追加写入 **两个** 文件：
- `~/.gstack/projects/$REMOTE_SLUG/greptile-history.md`（项目级，用于 suppressions）
- `~/.gstack/greptile-history.md`（全局汇总，供 retro 使用）

格式：

```text
<YYYY-MM-DD> | <owner/repo> | <type> | <file-pattern> | <category>
```

示例：

```text
2026-03-13 | garrytan/myapp | fp | app/services/auth_service.rb | race-condition
2026-03-13 | garrytan/myapp | fix | app/models/user.rb | null-check
2026-03-13 | garrytan/myapp | already-fixed | lib/payments.rb | error-handling
```

---

## 输出格式

在最终输出头部加入 Greptile 摘要：

```text
+ N Greptile comments (X valid, Y fixed, Z FP)
```

对每条分类后的 comment，展示：
- 分类标签：`[VALID]`、`[FIXED]`、`[FALSE POSITIVE]`、`[SUPPRESSED]`
- `file:line`（行级评论）或 `[top-level]`（顶层评论）
- 一行 body 摘要
- Permalink URL（也就是 `html_url` 字段）
