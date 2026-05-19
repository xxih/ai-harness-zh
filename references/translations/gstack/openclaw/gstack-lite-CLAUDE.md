# gstack-lite Planning Discipline

由 orchestrator 注入到被 spawn 的 Claude Code sessions 中。请追加到现有
`CLAUDE.md` 之后。

## Planning Discipline

1. 读完你将要修改的每个文件。先理解现有模式。
2. 写代码前先说明计划：做什么、为什么、改哪些文件、测试用例、风险。
3. 出现歧义时，优先：完整性胜过捷径，沿用现有模式胜过发明新模式，
   可逆选择胜过不可逆选择，安全默认值胜过聪明技巧。
4. 汇报完成前先 self-review：检查是否漏文件、import 是否损坏、
   路径是否未测试、风格是否不一致。
5. 完成后汇报：交付了什么、做了哪些决策、还有哪些不确定点。
