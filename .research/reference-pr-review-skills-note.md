# reference 中与 PR / review / 评论处理相关能力的调研

检查时间：2026-03-24

## 目标

- 判断当前几个主要 reference 是否已经包含：
  - 建 PR / 收尾分支的 skill 或规则
  - 请求 code review 的 skill / agent / command
  - 收到 review 评论后的处理 skill
  - PR 后自动记录、检查、清理的辅助能力

## 检查范围

- `references/repos/superpowers`
- `references/repos/everything-claude-code`
- `references/repos/oh-my-opencode`
- `references/repos/claudeception`
- 对应的中文翻译镜像

## 结论先行

### 最完整：`superpowers`

`superpowers` 是当前几份 reference 里，对“请求评审 -> 接收评审反馈 -> 分支收尾/开 PR”覆盖最完整的一份，而且大多是稳定、可复用的 skill。

明确命中：

- `requesting-code-review`
  - 路径：`references/repos/superpowers/skills/requesting-code-review/SKILL.md`
  - 作用：完成任务后请求 reviewer subagent，按 Critical / Important / Minor 处理结果
- `receiving-code-review`
  - 路径：`references/repos/superpowers/skills/receiving-code-review/SKILL.md`
  - 作用：收到 review feedback 后先验证、再实现；允许技术性反驳；还明确写了 GitHub inline comment 应回复原线程
- `finishing-a-development-branch`
  - 路径：`references/repos/superpowers/skills/finishing-a-development-branch/SKILL.md`
  - 作用：测试通过后，结构化给出 merge / create PR / keep / discard 四种出口，并处理 worktree 清理
- `verification-before-completion`
  - 路径：`references/repos/superpowers/skills/verification-before-completion/SKILL.md`
  - 作用：commit / push / PR 前先拿 fresh evidence

可以认为：

- “建 PR” 在 `superpowers` 里主要由 `finishing-a-development-branch` 承担
- “review 评论怎么处理” 由 `receiving-code-review` 承担
- “什么时候请求 review” 由 `requesting-code-review` 承担

### 次完整：`everything-claude-code`

ECC 有很多和 PR / review 强相关的资产，但主要分散在 `rules`、`commands`、`hooks`、`agents`、`loops` 中，不像 `superpowers` 那样有一个明确的“收到评论后怎么处理”的独立 skill。

明确命中：

- `rules/common/git-workflow.md`
  - 路径：`references/repos/everything-claude-code/rules/common/git-workflow.md`
  - 作用：规定 PR 创建前的 git diff、PR 摘要、测试计划、`git push -u`
- `hooks/README.md` + `scripts/hooks/post-bash-pr-created.js`
  - 路径：`references/repos/everything-claude-code/hooks/README.md`
  - 作用：`gh pr create` 后记录 PR URL 和 review 命令
- `commands/quality-gate.md`
  - 路径：`references/repos/everything-claude-code/commands/quality-gate.md`
  - 作用：PR 前的质量门
- `commands/verify.md` / `skills/verification-loop/SKILL.md`
  - 作用：PR 前验证循环
- `commands/code-review.md` 与多语言 reviewer agents
  - 路径：`references/repos/everything-claude-code/commands/code-review.md`
  - 作用：发起 code review
- `skills/blueprint/SKILL.md`
  - 作用：为多 PR 项目做分步计划，内置 branch / PR / CI workflow
- `skills/autonomous-loops/SKILL.md`
  - 作用：持续 PR 循环，包含 push、create PR、wait CI、auto-fix、merge

但 ECC 当前未看到一个与 `superpowers/receiving-code-review` 对等的独立 skill：

- 没有专门讲“review comment 收到后如何分类、核实、逐条处理、回帖”的单一 skill
- 更偏向：
  - 先做 review
  - 用 rule / hook / command 约束 PR 前后的动作
  - 通过 loops 做自动 PR / CI

### 弱相关：`oh-my-opencode`

`oh-my-opencode` 当前更强的是 orchestration、delegation、verify，以及 runtime/tooling 层设计；没有看到成型的“建 PR + 处理 review 评论”的 skill 体系。

只找到弱相关内容：

- orchestration / atlas / sisyphus prompt 中反复强调 `verify`
- `CONTRIBUTING.md` 有普通仓库层面的 Pull Request Process
- `features.md` 提到 Oracle 可做 code review

但没有看到：

- 独立的 `request-code-review` skill
- 独立的 `receive-review-feedback` skill
- 独立的 PR 创建/收尾 workflow skill

### 基本没有：`claudeception`

当前 `claudeception` 更聚焦知识提炼、skill 抽取与演化，没有看到与 PR / review comment workflow 直接对应的专门资产。

## 对仓库吸纳的意义

如果要沉淀“建 PR -> 收 review -> 回评审意见 -> 清理分支”的闭环，最值得借鉴的是：

1. `superpowers:requesting-code-review`
2. `superpowers:receiving-code-review`
3. `superpowers:finishing-a-development-branch`
4. `everything-claude-code: git-workflow / quality-gate / PR logger / autonomous-loops`

更具体地说：

- “review 评论怎么处理”：
  - `superpowers/receiving-code-review` 最强，已经有处理顺序、反驳边界、GitHub 线程回复方式
- “建 PR 前后怎么约束”：
  - ECC 的 `git-workflow`、`verify`、`quality-gate`、`PR logger` 更系统
- “多 PR / 自动 PR 循环”：
  - ECC 的 `blueprint`、`autonomous-loops` 更强

## 对当前仓库的建议

- 若目标是补“收到 review 评论后如何处理”的仓库自有能力：
  - 直接优先参考 `superpowers/receiving-code-review`
- 若目标是补“PR 创建与收尾”：
  - `superpowers/finishing-a-development-branch` + ECC `git-workflow`
- 若目标是补“PR 前 gate 与自动记录”：
  - ECC 的 `quality-gate`、`verify`、`PR logger`

## 决策

- 结论：`adapt`
- 不建议整套搬运某个 reference
- 建议按闭环拆三类能力吸收：
  - `request-review`
  - `review-feedback`
  - `pr-finish / pr-gate`

