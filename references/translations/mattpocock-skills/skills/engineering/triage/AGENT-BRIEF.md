# 写 Agent Brief

> 原文:[AGENT-BRIEF.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/AGENT-BRIEF.md)

Agent brief 是一份结构化评论,在 issue 进入 `ready-for-agent` 时贴在 GitHub issue 上。它是 AFK agent 实际开工依据的**权威规格**。原 issue body 和讨论是上下文——agent brief 才是**合同**。

## 原则

### 经久 > 精确

Issue 可能在 `ready-for-agent` 状态躺上几天甚至几周。其间代码库会变。**写 brief 时让它在文件被重命名、移动、重构后依然有用**。

- **要**描述接口、类型、行为契约
- **要**点名 agent 应该去找或修改的具体类型、函数签名、配置形状
- **不要**引用文件路径——会过时
- **不要**引用行号
- **不要**假设当前的实现结构会保持不变

### 行为优先,不写步骤

描述系统**应该做什么**,不是**怎么实现**。Agent 会自己重新探索代码库,自己做实现决策。

- **好**:"`SkillConfig` 类型应该接受一个可选的 `schedule` 字段,类型是 `CronExpression`"
- **差**:"打开 src/types/skill.ts 在 42 行加一个 schedule 字段"
- **好**:"用户输 `/triage` 不带参数时,应该看到需要关注的 issue 摘要"
- **差**:"在 main handler 函数里加个 switch case"

### 完整的验收标准

Agent 得知道什么算"做完"。**每个 agent brief 都必须有具体、可测的验收标准**。每条标准独立可验证。

- **好**:"跑 `gh issue list --label needs-triage` 返回经过初步分类的 issue"
- **差**:"triage 应该正常工作"

### 显式的范围边界

**写出什么不在范围内**。这能阻止 agent 镀金或对相邻功能瞎猜。

## 模板

```markdown
## Agent Brief

**Category:** bug / enhancement
**Summary:** 一行话描述要做啥

**Current behavior:**
描述现在发生什么。Bug 就是坏掉的行为。
Enhancement 就是这次功能要基于的现状。

**Desired behavior:**
描述 agent 做完后应该发生什么。
对边界情况和错误条件具体说明。

**Key interfaces:**
- `TypeName` —— 要改什么、为什么
- `functionName()` 返回类型 —— 当前返回啥 vs 应该返回啥
- 配置形状 —— 需要的新配置项

**Acceptance criteria:**
- [ ] 具体、可测的标准 1
- [ ] 具体、可测的标准 2
- [ ] 具体、可测的标准 3

**Out of scope:**
- 这次 issue 里**不该**被改或被处理的事
- 看起来相关但其实是另一回事的相邻功能
```

## 例子

### 好的 agent brief(bug)

```markdown
## Agent Brief

**Category:** bug
**Summary:** Skill description 在词中间被截断,产出破损输出

**Current behavior:**
当 skill description 超过 1024 字符时,会在第 1024 字符处硬截断,
不管词边界。结果就是描述以半个词结尾(比如 "Use when the user wants to confi")。

**Desired behavior:**
截断应该发生在 1024 字符之前的最后一个词边界,并追加 "..." 以表示被截断。

**Key interfaces:**
- `SkillMetadata` 类型的 `description` 字段 —— 类型不用改,但填充它的
  validation/processing 逻辑要尊重词边界
- 任何读 SKILL.md frontmatter 并提取 description 的函数

**Acceptance criteria:**
- [ ] <1024 字符的 description 不变
- [ ] >1024 字符的 description 在 1024 字符前的最后词边界截断
- [ ] 被截断的 description 以 "..." 结尾
- [ ] 包含 "..." 的总长度不超过 1024 字符

**Out of scope:**
- 改 1024 字符上限本身
- 多行 description 支持
```

### 好的 agent brief(enhancement)

```markdown
## Agent Brief

**Category:** enhancement
**Summary:** 加 `.out-of-scope/` 目录支持,用来追踪被拒的 feature request

**Current behavior:**
Feature request 被拒时,issue 关闭并打 `wontfix` 标签 + 一条评论。
没有持久记录决策或理由。以后类似请求来时,维护者得靠记忆或搜索去翻
之前的讨论。

**Desired behavior:**
被拒的 feature request 应该被记录在 `.out-of-scope/<concept>.md` 文件里,
含决策、理由、以及所有请求该功能的 issue 链接。在 triage 新 issue 时,
应该检查这些文件是否匹配。

**Key interfaces:**
- `.out-of-scope/` 下的 markdown 文件格式 —— 每个文件应有
  `# Concept Name` 标题、`**Decision:**` 一行、`**Reason:**` 一行,
  以及带 issue 链接的 `**Prior requests:**` 列表
- Triage 工作流应该早期就读所有 `.out-of-scope/*.md` 文件,
  并按"概念相似度"把新 issue 和它们匹配

**Acceptance criteria:**
- [ ] 把一个 feature 关成 wontfix 时会创建/更新 `.out-of-scope/` 里的文件
- [ ] 文件包含决策、理由、关闭 issue 的链接
- [ ] 如果匹配的 `.out-of-scope/` 文件已存在,新 issue 追加到它的
      "Prior requests" 而不是建重复文件
- [ ] Triage 时,现有的 `.out-of-scope/` 文件会被检查;新 issue
      匹配上之前拒绝时会浮出来

**Out of scope:**
- 自动匹配(由人来确认匹配)
- 重开之前被拒的功能
- Bug 报告(只有 enhancement 拒绝才进 `.out-of-scope/`)
```

### 差的 agent brief

```markdown
## Agent Brief

**Summary:** 修一下 triage 的 bug

**What to do:**
triage 那块儿坏了。看下主文件修一下。
150 行附近那个函数有问题。

**Files to change:**
- src/triage/handler.ts (line 150)
- src/types.ts (line 42)
```

差在哪:
- 没 category
- 描述模糊("triage 那块儿坏了")
- 引用了会过时的文件路径和行号
- 没验收标准
- 没范围边界
- 没说当前 vs 期望行为
