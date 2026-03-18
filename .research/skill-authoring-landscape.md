# Skill Authoring Landscape Research

## 目标

- 评估当前主流 AI coding agent / harness 社区里，谁的 skill 编写与迭代实践最成熟。
- 重点比较：Anthropic 官方 Claude Skills 指南、Superpowers 的 `writing-skills`、Codex 内置 `skill-creator`、Everything Claude Code 的 `skill-create`、Oh My OpenCode / OpenCode 的 skills 机制。
- 输出一个可执行判断：如果要在当前仓库沉淀自己的 skill 编写方法，最值得 adopt / adapt 谁的方案。

## 比较维度

1. 发现机制是否清晰：skill 如何被触发、description 如何写。
2. 结构设计是否成熟：是否明确区分 `SKILL.md` / references / scripts / assets。
3. 迭代闭环是否成熟：是否有明确的验证、回归、反漏洞补洞方法。
4. 平台绑定程度：方法是否只适用于单一工具，还是可跨工具迁移。
5. 社区可复用性：是否已经形成被大量复用的公共模式，而不是单仓库私货。

## 候选与观察

### 1. Anthropic 官方 Claude Skills best practices

来源：
- https://docs.claude.com/en/docs/agents-and-tools/agent-skills
- https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices

优点：
- 是最权威的底层规范，明确定义了 `SKILL.md`、frontmatter、`name` / `description` 约束。
- progressive disclosure 讲得非常清楚：metadata 常驻、正文按需加载、references 再按需加载。
- 对 concise、degrees of freedom、命名、description 写法都有强约束，适合做“底座规则”。
- 可迁移性很强，因为 OpenCode、Codex 等生态都在兼容或借鉴这套格式。

短板：
- 更像“authoring best practices”，不是“如何持续迭代 skill”的完整闭环。
- 验证部分偏原则，不像 Superpowers 那样把 skill 迭代写成明确的 RED-GREEN-REFACTOR 文档流程。

判断：
- 适合作为基础规范。
- 不足以单独构成最佳“迭代方法论”。

### 2. Superpowers `writing-skills`

来源：
- https://github.com/obra/superpowers
- https://skills.sh/obra/superpowers/writing-skills
- 本地文件：`references/repos/superpowers/skills/writing-skills/SKILL.md`

优点：
- 是目前最强的“skill 迭代方法”文档：直接把 skill 编写定义为“对流程文档做 TDD”。
- 核心闭环非常清楚：先构造 pressure scenario，让 agent 在没有 skill 时失败，再写 skill，再验证通过，再根据新漏洞补洞。
- 特别强调 description 不能偷跑 workflow，否则模型会只读 description 不读正文，这属于非常实战的经验。
- 对 discovery、命名、token 成本、反 shortcut 都有大量真实踩坑后的规则。
- 社区性强：它不只是一篇官方说明，而是一个被真实工作流反复锤过的技能库元技能。

短板：
- 带有明显 Claude / subagent 工作流假设，迁移到不支持强 subagent 验证的环境时，需要裁剪。
- 文风很强，方法论带有 Jesse / Superpowers 的工程哲学色彩，不是所有团队都会全盘接受。

判断：
- 如果目标是“写得出、并且能持续把 skill 打磨好”，它目前是最强的社区实践。
- 最适合 adopt 为“迭代闭环”，再用官方 Claude best practices 约束格式层。

### 3. Codex 内置 `skill-creator`

来源：
- 本地文件：`/Users/xxih/.codex/skills/.system/skill-creator/SKILL.md`
- 补充：`/Users/xxih/.codex/skills/.system/skill-creator/references/openai_yaml.md`

优点：
- 结构设计最系统：明确区分 `SKILL.md`、`references/`、`scripts/`、`assets/`、`agents/openai.yaml`。
- 对 progressive disclosure、token economy、variant 拆分、UI metadata 都讲得比大多数社区方案更完整。
- 很适合做“仓库级技能资产工程化”的蓝图，尤其适合需要 UI 展示、依赖声明、隐式调用策略的环境。
- 对 skill 目录卫生要求高，能有效防止 README / 安装指南泛滥。

短板：
- 它更强在“如何把 skill 设计成一个好产品/好目录结构”，不是最强的“如何迭代验证这个 skill 真有用”。
- 虽然提到可以用 subagent 做 validation，但没有 Superpowers 那么强的 fail-first 实战闭环。

判断：
- 在“skill 结构工程化”层面，它比 Superpowers 更成熟。
- 在“skill 迭代方法论”层面，它不如 Superpowers 狠。

### 4. Everything Claude Code `skill-create`

来源：
- https://github.com/affaan-m/everything-claude-code
- 本地文件：`references/repos/everything-claude-code/commands/skill-create.md`

优点：
- 很适合从现有仓库里“挖”出团队规范：分析 git history、找 commit 模式、共变文件、测试习惯，再生成 `SKILL.md`。
- 对已有团队资产做 bootstrap 很有帮助，尤其适合“我们有很多隐性规范，但没写出来”。

短板：
- 它本质是“从 repo 历史提炼技能草稿”的工具，不是成熟的 skill authoring / iteration 方法论。
- 生成结果偏总结型，容易变成 repo pattern 文档，而不是高触发率、高执行力的 skill。
- 没有像 Superpowers 那样把 discovery、pressure-testing、反漏洞补洞做成闭环。

判断：
- 更像“技能素材采集器”或“初稿生成器”。
- 不适合直接拿来当最佳实践主线。

### 5. OpenCode / Oh My OpenCode

来源：
- https://opencode.ai/docs/skills
- https://github.com/code-yeongyu/oh-my-opencode
- 本地文件：`references/repos/oh-my-opencode/docs/reference/features.md`

优点：
- runtime 能力很强：原生 `skill` 工具、按需加载、Claude 兼容路径、skill-embedded MCP，这在执行层很先进。
- 说明它对“skill 作为运行时能力包”这件事理解很深，尤其是 skill 携带 MCP 的能力非常领先。

短板：
- 公开资料里更强调 runtime / orchestration / embedded MCP，而不是“如何写出一个好 skill 并持续迭代它”。
- 至少在当前可见资料里，没有看到能与 Superpowers `writing-skills` 或 Codex `skill-creator` 对位的 authoring 方法文档。

判断：
- OpenCode / OMO 在 skill runtime 能力上很强。
- 但在“skill authoring best practice”这个问题上，目前不是最强样板。

## 结论

### 总排名（按“写 skill + 迭代 skill”的实践成熟度）

1. **Superpowers `writing-skills`**：最强的迭代方法论，尤其是 fail-first / pressure scenario / 补漏洞闭环。
2. **Anthropic 官方 Claude Skills best practices**：最强的底层规范与 discoverability 规则，适合作为基础约束。
3. **Codex `skill-creator`**：最强的结构工程化方案，适合做目录规范、资源分层、UI metadata 和长期维护。
4. **Everything Claude Code `skill-create`**：适合从 git 历史挖模式，适合作为辅助工具，不适合作为主方法论。
5. **OpenCode / Oh My OpenCode**：runtime 很强，但公开 skill authoring 方法论不够成熟。

### 对用户问题的直接回答

- **“谁家的实践最好？”**
  - 如果你问的是“怎么把 skill 写好、并持续迭代好”，**Superpowers 目前最好**。
  - 如果你问的是“skill 底层规范和发现机制”，**Anthropic 官方文档最好**。
  - 如果你问的是“skill 目录结构工程化和产品化”，**Codex `skill-creator` 最完整**。

- **“Claude Code 自己的写 skill / 迭代 skill prompt，和 Superpowers 比怎么样？”**
  - Claude 官方 best practices 更像“规范层 + discoverability 层”，很强，但偏基础设施。
  - Superpowers 明显更像“实战迭代打法”，尤其在如何验证 skill 真能改变 agent 行为这件事上更领先。
  - 最好的做法不是二选一，而是：**Anthropic 负责底层格式规范，Superpowers 负责迭代闭环。**

- **“比起其他更多社区的 skill create 方案怎么样？”**
  - ECC 的 `skill-create` 适合提炼隐性规范，但不像 Superpowers 那样能持续打磨 skill 质量。
  - Codex 的 `skill-creator` 适合做稳定、整洁、长期可维护的 skill 目录，但验证闭环不如 Superpowers。
  - OpenCode / OMO 的强项在 runtime，不在 authoring discipline。

## 建议给当前仓库的 adopt / adapt 方向

- **adopt Anthropic**：采用它的 `SKILL.md` 基本规范、description discoverability、progressive disclosure 原则。
- **adapt Superpowers**：采用它的 fail-first / pressure scenario / loophole plugging 作为 skill 迭代方法，但不要机械搬整套 Claude 工作流。
- **adapt Codex**：采用它的目录工程化思想，只保留当前仓库真正需要的 `references/` / `assets/` / metadata 分层。
- **不要 adopt ECC `skill-create` 作为主线**：可以把它当作“发现可沉淀模式”的辅助入口。
- **不要 adopt OMO 的整套 runtime 设定**：skill-embedded MCP 可以继续关注，但当前仓库先别被 runtime 花活带偏。
