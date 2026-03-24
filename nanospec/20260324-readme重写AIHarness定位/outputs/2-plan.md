# 方案：20260324-readme重写AIHarness定位

## 方案概览

本次不做结构调整，只重写 README 的开头叙事，并把任务过程按 NanoSpec 落盘。整体采用“先看成熟 harness 已做到什么，再看 AI Harness 定义与仓库定位，最后看推荐参考对象”的顺序，让新读者先看到能力差距，再理解仓库边界。

## 实施步骤

1. 读取现有 `README.md` 与仓库中的参考资料，确认当前对 AI Harness 的已有表述和可用参考对象。
2. 新建本次 `nanospec` 任务容器，补充 brief / spec / plan / tasks，固定交付范围与验收口径。
3. 先梳理一张分类能力对照：
   - 成熟 harness 已覆盖的代表能力
   - 当前仓库已沉淀的 package
   - 仍未系统化覆盖的运行时 / hook / 平台能力
4. 重写 `README.md` 开头四部分：
   - 成熟 harness 能力对照
   - AI Harness 的定义
   - 本仓库聚焦的可定制层
   - 推荐参考的 harness 与原因
5. 保留并衔接已有的目录说明、packages 清单、target 同步与 references 约定，避免让 README 断层。
6. 检查 diff，回写 `outputs/3-tasks.md` 的完成状态。

## 关键决策

### 1. 定义优先直白，不追求学术化

采用“AI Harness = 除了 LLM 外的一切”作为第一句定义，再用一组具体组成把口号展开。这样既满足用户对简明表达的要求，也避免读者误以为 harness 只是 prompt。

### 2. 仓库定位优先写“可定制层”

README 不强调“我们能研究所有层”，而是强调“我们主要沉淀 coding agent 暴露给我们的扩展口子”。这更符合当前仓库以 `packages/` 为中心的资产定位。

### 3. 推荐对象只写三类代表

优先推荐：

- `everything-claude-code`：适合作为全栈 harness 与跨平台适配参考
- `superpowers`：适合作为 skill-first workflow 与工程节奏参考
- `oh-my-opencode`：适合作为运行时编排、上下文治理与工具链设计参考

这样能覆盖 “完整系统 / 最小工作流 / 运行时内核” 三个角度，且都已在仓库中有参考材料。

### 4. 用“能力类别”替代“仓库导览”

新增要求不是简单再列几个仓库名字，而是要先回答“成熟 harness 到底已经做到了什么”。因此 README 前部改为能力类别视角，每类再嵌入具体仓库和 skill / command / hook 示例。
