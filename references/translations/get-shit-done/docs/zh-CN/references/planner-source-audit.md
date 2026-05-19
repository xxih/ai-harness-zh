# Planner Source Audit 与权限边界

供 `agents/gsd-planner.md` 参考，补充多来源覆盖审计规则与 planner 权限限制。

## 多来源覆盖审计格式

在最终确定 plans 之前，要产出一份 **source audit**，覆盖全部四类工件：

```
SOURCE    | ID      | Feature/Requirement          | Plan  | Status    | Notes
--------- | ------- | ---------------------------- | ----- | --------- | ------
GOAL      | —       | {phase goal from ROADMAP.md}  | 01-03 | COVERED   |
REQ       | REQ-14  | OAuth login with Google + GH | 02    | COVERED   |
REQ       | REQ-22  | Email verification flow      | 03    | COVERED   |
RESEARCH  | —       | Rate limiting on auth routes | 01    | COVERED   |
RESEARCH  | —       | Refresh token rotation       | NONE  | ⚠ MISSING | No plan covers this
CONTEXT   | D-01    | Use jose library for JWT     | 02    | COVERED   |
CONTEXT   | D-04    | 15min access / 7day refresh  | 02    | COVERED   |
```

### 四类来源

1. **GOAL**：该 phase 在 `ROADMAP.md` 中的 `goal:` 字段。这是首要成功条件
2. **REQ**：`phase_req_ids` 中的每一个 REQ-ID。需要回到 `REQUIREMENTS.md` 查其描述
3. **RESEARCH**：`RESEARCH.md` 中识别出的技术方案、发现的约束与功能点。明确被 researcher 标记为 “out of scope” 或 “future work” 的项要排除
4. **CONTEXT**：`CONTEXT.md` 的 `<decisions>` 段落中每一个 D-XX 决策

### 什么不算 Gap

不要把以下内容标记为 `MISSING`：
- `CONTEXT.md` 中 `## Deferred Ideas` 下的项目，这些是开发者明确选择延后的
- 通过 `phase_req_ids` 归属到其他 phase 的项目，不属于当前 phase
- `RESEARCH.md` 中被 researcher 明确标记为 “out of scope” 或 “future work” 的项目

### 如何处理 `MISSING` 项

如果**任何一行**是 `⚠ MISSING`，不要悄悄完成整套计划。应向 orchestrator 返回：

```
## ⚠ Source Audit: Unplanned Items Found

The following items from source artifacts have no corresponding plan:

1. **{SOURCE}: {item description}** (from {artifact file}, section "{section}")
   - {why this was identified as required}

   Options:
   A) Add a plan to cover this item
   B) Split phase: move to a sub-phase
   C) Defer explicitly: add to backlog with developer confirmation

   → Awaiting developer decision before finalizing plan set.
```

如果所有行都为 `COVERED`，再正常返回 `## PLANNING COMPLETE`。

---

## 权限边界：约束示例

planner 唯一有正当理由去拆分或标记某个 feature 的原因只能是**约束**，而不能是对难度的主观判断：

**有效（约束）：**
- ✓ “这个任务会触及 9 个文件，预计会消耗约 45% 上下文，需要拆成两个 task”
- ✓ “任何来源工件里都没有定义 API key 或 endpoint，需要开发者补充输入”
- ✓ “这个功能依赖于尚未完成的 Phase 03 身份认证系统”

**无效（难度判断）：**
- ✗ “这很复杂，可能很难正确实现”
- ✗ “集成外部服务可能会花很长时间”
- ✗ “这是个有挑战的功能，也许更适合留到未来 phase”

如果某个 feature 不存在这三类正当约束之一（上下文成本、信息缺失、依赖冲突），那它就应该被规划进去。没有例外。
