# `TODOS.md` 格式参考

供 `/ship`（Step 5.5）与 `/plan-ceo-review`（`TODOS.md` updates 部分）共享使用的规范参考，用来确保 TODO 条目的结构一致。

---

## 文件结构

```markdown
# TODOS

## <Skill/Component>     ← 例如：## Browse、## Ship、## Review、## Infrastructure
<items sorted P0 first, then P1, P2, P3, P4>

## Completed
<finished items with completion annotation>
```

**Sections：** 按 skill 或 component 组织（如 `## Browse`、`## Ship`、`## Review`、`## QA`、`## Retro`、`## Infrastructure`）。每个 section 内部再按优先级排序，`P0` 放最前。

---

## TODO 条目格式

每个条目在所属 section 下使用一个 H3：

```markdown
### <Title>

**What:** 对这项工作的单行描述。

**Why:** 它解决的具体问题，或它解锁的实际价值。

**Context:** 要让 3 个月后接手的人也能看懂动机、当前状态和起手点。

**Effort:** S / M / L / XL
**Priority:** P0 / P1 / P2 / P3 / P4
**Depends on:** <prerequisites, or "None">
```

**必填字段：** `What`、`Why`、`Context`、`Effort`、`Priority`
**可选字段：** `Depends on`、`Blocked by`

---

## 优先级定义

- **P0**：Blocking，下一次发布前必须完成
- **P1**：Critical，本周期应该完成
- **P2**：Important，等 `P0/P1` 清掉后优先处理
- **P3**：Nice-to-have，等有 adoption / usage data 后再回看
- **P4**：Someday，是好想法，但没有紧迫性

---

## 已完成条目格式

当某个条目完成后，把它移动到 `## Completed` 区域，保留原有内容，并追加：

```markdown
**Completed:** vX.Y.Z (YYYY-MM-DD)
```
