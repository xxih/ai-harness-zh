# Alignment Log

## 2026-03-17

- [变更] 用户校验当前 `learning-capture` 样例后，认为三份产物里只有 `project-rules.md` 稍有价值，对现有 skill 的默认产出质量不满意。
- [变更] 用户补充了一个更能暴露问题的真实场景：把 `0316 AI 时代的词汇量.md` 改写成小红书风格并导出图文；在该场景下，学习沉淀的理想结果更接近“把整条流程整理成 skill”，而不是分散在几个细小记录点上。
- [缺失] 当前 skill 虽然区分了 `learnings.md`、`promote-candidates.md`、`project-rules.md`，但没有把“什么时候该沉淀成流程型共享资产”说清楚，也没有把三类文件的主次关系说清楚。
- [变更] 当前任务先不急着直接改写 skill，先完成三类文件定位澄清、问题诊断与优化方案，再决定是否修改 `src/skills/learning-capture/`。
- [变更] 用户进一步要求把入口收敛成两个：`rules` 与 `other`，并压缩模板字段，避免为了结构写出低价值条目。
- [变更] 当前实现已将默认文件改为 `.learned/rules.md` 与 `.learned/notes.md`，不再默认拆分 `learnings.md` 与 `promote-candidates.md`。
