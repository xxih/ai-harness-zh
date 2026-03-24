# 验证记录：learning-evolution pressure scenario

## 2026-03-19

### 范围

- 验证对象：`packages/learning-evolution/skills/learning-evolution/SKILL.md`
- 同步对象：`packages/learning-evolution/targets/codex/skills/learning-evolution/SKILL.md`
- 验证方式：按 `writing-skills` 的 fail-first 验证循环执行一轮 baseline / rerun；当前未启用独立 agent，因此采用手工 pressure scenario + fresh 文本校验的降级做法

### 本轮执行命令

```bash
sed -n '1,240p' /Users/xxih/.codex/skills/writing-skills/references/validation-loop.md
sed -n '1,220p' /Users/xxih/.codex/skills/quality-verify/SKILL.md
sed -n '1,220p' packages/learning-evolution/skills/learning-evolution/SKILL.md
sed -n '1,220p' packages/learning-evolution/skills/learning-evolution/references/templates.md
rg -n "NanoSpec|nanospec|alignment\\.md|brief\\.md|prd\\.md|outputs/1-spec\\.md|outputs/2-plan\\.md|outputs/3-tasks\\.md|执行 align|\\balign\\b" packages/learning-evolution/skills/learning-evolution packages/learning-evolution/_AGENTS.md packages/learning-evolution/targets/codex/skills/learning-evolution packages/learning-evolution/targets/codex/_AGENTS.md
rg -n "当前任务容器|任务容器已有文件" packages/learning-evolution/skills/learning-evolution packages/learning-evolution/_AGENTS.md packages/learning-evolution/targets/codex/skills/learning-evolution packages/learning-evolution/targets/codex/_AGENTS.md
diff -u packages/learning-evolution/skills/learning-evolution/SKILL.md packages/learning-evolution/targets/codex/skills/learning-evolution/SKILL.md
```

### Baseline pressure scenario

场景：

- 用户说：“复盘一下最近几次翻译 / 改写流程，把值得长期保留的东西沉淀一下，但先不要改 skill、README 或规则文件。”

没有当前 skill 时，最容易出现的错误：

1. 跳过出口判断，直接把候选升级成正式资产。
2. 不区分 `keep-task-local`、`queue-support`、`rules`，把所有东西都塞进一个长期文件。
3. 把 task-local 经验误写成跨任务沉淀。
4. 因为看到“长期有价值”，就自动进入 `Evolution`。

### Rerun 结果

#### 检查点 1：触发条件是否清楚

- 证据：`description` 明确覆盖“复盘、沉淀经验、记录长期规则、整理 support 卡、继续 codify 正式资产”。
- 结果：通过。

#### 检查点 2：是否有显式出口

- 证据：正文明确给出 `drop`、`keep-task-local`、`queue-support`、`codify-now` 四个出口。
- 结果：通过。

#### 检查点 3：是否默认阻止误入 Evolution

- 证据：正文明确写明 `Evolution` 不是默认动作；只有用户明确要求演化 / codify 且目标资产明确、证据充分时才执行。
- 结果：通过。

#### 检查点 4：是否能区分 task-local 与长期沉淀

- 证据：`keep-task-local`、`.learned/rules.md`、`.learned/support.md` 三类去向分开描述；模板也给出 task-local 的独立写法。
- 结果：通过。

#### 检查点 5：是否仍把协作机制写成默认前提

- 证据：关键词搜索未再命中 `NanoSpec`、`alignment.md`、`align`、`任务容器` 等默认前提表述。
- 结果：通过。

### 近邻场景复验

#### 场景 A：只对当前工作有用

- 场景：“这次 shell workaround 只给当前工作后续步骤用，别跨任务保留。”
- 预期：走 `keep-task-local`。
- 证据：正文明确写“只影响当前工作后续动作，写回当前上下文已有记录位置，不进入 `.learned/`”。
- 结果：通过。

#### 场景 B：规则已足够明确

- 场景：“把最近 reviewer 反复指出的规范沉淀成长期规则；如果证据够了就直接写回对应规范。”
- 预期：规则进入 `.learned/rules.md` 或直接 `codify-now`。
- 证据：正文给出规则出口与 `codify-now` 条件。
- 结果：通过。

#### 场景 C：用户明确要求演化

- 场景：“把这些 support 候选继续演化成正式 skill / README 更新。”
- 预期：进入 `Evolution`，再判断是否 `codify-now`。
- 证据：正文给出明确的第二阶段门槛与正式沉淀步骤。
- 结果：通过。

### 风险项

- 本轮没有独立 agent replay；验证证据来自 fresh 文本检查与 pressure scenario 自查，不等同于真实会话行为回放。
- 当前结论只覆盖“prompt 结构是否足以支撑正确使用”，不覆盖未来 target 自动化入口的行为验证。

### 结论

- 质量结论：`ready`
- 结论边界：就当前 source / target prompt 结构而言，`learning-evolution` 已覆盖本轮 baseline 暴露的主要失败点，并通过一轮近邻场景复验；若后续引入 hooks / observer，再补一轮真实行为验证。
