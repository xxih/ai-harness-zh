# 重构候选

> 原文:[refactoring.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/refactoring.md)

一轮 TDD 之后,找下面这些信号:

- **重复** → 抽函数 / 类
- **方法太长** → 拆成私有 helper(测试仍挂在公共接口上)
- **浅模块** → 合并或加深
- **Feature envy(羡慕特征)** → 把逻辑挪到数据所在的地方
- **原始类型迷恋(Primitive obsession)** → 引入值对象
- **新代码暴露出**有问题的**现有代码**
