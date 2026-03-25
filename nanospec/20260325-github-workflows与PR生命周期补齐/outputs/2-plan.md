# 方案：20260325-github-workflows与PR生命周期补齐

## 方案概览

本次不重做实现，只做两件事：

1. 为当前 staged 改动补齐 nanospec 文档。
2. 在确认文档与 staged 内容一致后，把这一波改动提交。

## 实施步骤

1. 盘点当前 staged 改动，确认哪些文件属于同一波交付。
2. 新建本次 nanospec 任务容器，补 `brief`、`spec`、`plan`、`tasks`。
3. 在文档里明确这波交付的三层内容：
   - `github-workflows` 新包与 Codex target
   - 支撑研究文档
   - README / package 边界与 `.learned` 更新
4. 将 nanospec 文档加入本轮提交范围。
5. 提交当前暂存区。

## 关键决策

### 1. 以 staged 改动为任务边界

用户明确说的是“把暂存区的改动，这一波改动，没有落 nanospec 文档的落一下”。因此本任务边界以当前 staged 内容为准，而不是只围绕某一个单独 package。

### 2. `github-workflows` 是这波交付主轴

虽然 staged 内容包含 `.research` 和 `.learned`，但从产品上看，这波交付的主轴仍然是新增 `packages/github-workflows/`，其余文件都在为这个方向提供研究、说明或长期沉淀。

### 3. 文档只描述已交付内容

本次 nanospec 文档不把未实现的 `gh` 执行面、hooks、state machine 写成“已完成”，而是只记录当前包定位和边界变化。
