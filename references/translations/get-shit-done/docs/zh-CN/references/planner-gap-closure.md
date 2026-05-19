# Gap Closure Mode - Planner Reference

由 `--gaps` flag 触发。用于创建计划，以处理 verification 或 UAT 失败。

**重要：跳过 deferred 项。** 读取 `VERIFICATION.md` 时，只有 `gaps:` 段落里的项目才是需要制定 closure plan 的可执行事项。`deferred:` 段落（若存在）列出的是已经明确安排到后续 milestone phase 处理的项目，它们**不是** gap，必须忽略。为 deferred 项创建计划只会把已经安排到未来的工作又重复做一遍。

**1. 查找 gap 来源：**

使用 init context（由 `load_project_state` 提供），其中包含 `phase_dir`：

```bash
# 检查 VERIFICATION.md（代码验证缺口）
ls "$phase_dir"/*-VERIFICATION.md 2>/dev/null

# 检查状态为 diagnosed 的 UAT.md（用户测试缺口）
grep -l "status: diagnosed" "$phase_dir"/*-UAT.md 2>/dev/null
```

**2. 解析 gaps：** 每个 gap 都包含：truth（失败的行为）、reason、artifacts（有问题的文件）、missing（需要补充/修复的内容）。

**3. 读取现有 SUMMARY**，了解当前已经构建了什么。

**4. 找到下一个计划编号：** 如果已有 01-03，则下一个是 04。

**5. 按以下方式把 gaps 分组到 plans 中：** 相同 artifact、相同关注点、依赖顺序（如果某个 artifact 还是 stub，就不能先做 wiring，必须先修 stub）。

**6. 创建 gap closure tasks：**

```xml
<task name="{fix_description}" type="auto">
  <files>{artifact.path}</files>
  <action>
    {For each item in gap.missing:}
    - {missing item}

    Reference existing code: {from SUMMARYs}
    Gap reason: {gap.reason}
  </action>
  <verify>{How to confirm gap is closed}</verify>
  <done>{Observable truth now achievable}</done>
</task>
```

**7. 用标准依赖分析分配 wave**（与 `assign_waves` 步骤相同）：
- 没有依赖的 plans -> wave 1
- 依赖其他 gap closure plans 的 plans -> `max(dependency waves) + 1`
- 也要考虑该 phase 中对现有（非 gap）plans 的依赖

**8. 写入 PLAN.md 文件：**

```yaml
---
phase: XX-name
plan: NN              # 接在现有计划之后顺序编号
type: execute
wave: N               # 根据 depends_on 计算（见 assign_waves）
depends_on: [...]     # 该计划依赖的其他计划（gap 或既有计划）
files_modified: [...]
autonomous: true
gap_closure: true     # 用于跟踪的标记
---
```
