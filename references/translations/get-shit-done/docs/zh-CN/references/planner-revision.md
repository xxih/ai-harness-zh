# Revision Mode - Planner Reference

当 orchestrator 提供包含 checker issues 的 `<revision_context>` 时触发。这不是从头开始，而是对现有计划做定向更新。

**思维方式：** 像外科医生，而不是架构师。针对具体问题做最小修改。

### 第 1 步：加载现有计划

```bash
cat .planning/phases/$PHASE-*/$PHASE-*-PLAN.md
```

建立当前计划结构、现有 tasks 与 `must_haves` 的心智模型。

### 第 2 步：解析 checker issues

issues 会以结构化格式提供：

```yaml
issues:
  - plan: "16-01"
    dimension: "task_completeness"
    severity: "blocker"
    description: "Task 2 missing <verify> element"
    fix_hint: "Add verification command for build output"
```

按 plan、dimension、severity 进行分组。

### 第 3 步：制定 revision 策略

| Dimension | 策略 |
|-----------|------|
| requirement_coverage | 为缺失的 requirement 增加 task |
| task_completeness | 给现有 task 补充缺失元素 |
| dependency_correctness | 修正 `depends_on`，重新计算 wave |
| key_links_planned | 增加 wiring task，或更新 action |
| scope_sanity | 拆分为多个 plans |
| must_haves_derivation | 从前置材料推导并补入 `frontmatter` 的 `must_haves` |

### 第 4 步：做定向更新

**要做：** 编辑被标记的问题段落，保留已经有效的部分；如果依赖变化了，要同步更新 wave。

**不要做：** 为了小问题重写整套计划；添加不必要的 tasks；破坏现有可工作的计划。

### 第 5 步：验证修改

- [ ] 所有被标记的问题都已处理
- [ ] 没有引入新的问题
- [ ] wave 编号仍然有效
- [ ] 依赖关系仍然正确
- [ ] 磁盘上的文件已更新

### 第 6 步：提交

```bash
node "$HOME/.claude/get-shit-done/bin/gsd-tools.cjs" commit "fix($PHASE): revise plans based on checker feedback" --files .planning/phases/$PHASE-*/$PHASE-*-PLAN.md
```

### 第 7 步：返回 revision 摘要

```markdown
## REVISION COMPLETE

**Issues addressed:** {N}/{M}

### Changes Made

| Plan | Change | Issue Addressed |
|------|--------|-----------------|
| 16-01 | Added <verify> to Task 2 | task_completeness |
| 16-02 | Added logout task | requirement_coverage (AUTH-02) |

### Files Updated

- .planning/phases/16-xxx/16-01-PLAN.md
- .planning/phases/16-xxx/16-02-PLAN.md

{If any issues NOT addressed:}

### Unaddressed Issues

| Issue | Reason |
|-------|--------|
| {issue} | {why - needs user input, architectural change, etc.} |
```
