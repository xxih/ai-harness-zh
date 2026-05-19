# Language(语言)

> 原文:[LANGUAGE.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/LANGUAGE.md)

本 skill 所有建议共享的词表。**精确使用这些术语**——别替换为 "component"、"service"、"API"、"boundary"。**一致的语言就是这一切的目的**。

## 术语

**Module(模块)**
任何有接口和实现的东西。**故意做到尺度无关**——同样适用于函数、类、包、跨层切片。
_避免_:unit、component、service。

**Interface(接口)**
调用方为正确使用模块必须知道的一切。包含类型签名,**也**包含不变量、顺序约束、错误模式、必需配置、性能特征。
_避免_:API、signature(太窄——它们只指类型层面的表面)。

**Implementation(实现)**
模块的内部 —— 它的代码主体。与 **Adapter** 不同:一个东西可以是"小适配器 + 大实现"(Postgres repo),也可以是"大适配器 + 小实现"(in-memory fake)。**话题是 seam 时用 "adapter";其它时候用 "implementation"**。

**Depth(深度)**
接口上的杠杆 —— 调用方(或测试)对每一份接口知识能演练出的行为量。**深** = 大量行为藏在小接口背后。**浅** = 接口几乎和实现一样复杂。

**Seam(接缝)** _(取自 Michael Feathers)_
**不修改原地代码就能改变行为**的地方。模块接口**所在的位置**。"seam 放在哪"是独立的设计决策,和"seam 背后是什么"不同。
_避免_:boundary(被 DDD 的 bounded context 重载了)。

**Adapter(适配器)**
在 seam 上满足接口的具体物件。描述**角色**(填什么槽),不是**本质**(里面是什么)。

**Leverage(杠杆)**
调用方从深度中获得的东西。每一份要学的接口换来更多能力。**一份实现回报 N 个调用点 + M 个测试**。

**Locality(局部性)**
维护者从深度中获得的东西。变更、bug、知识、验证集中在**一处**,而不是分散在调用方。**修一次,处处都修了**。

## 原则

- **深度是接口的属性,不是实现的属性**。一个深模块**内部**可以由小、可 mock、可换的部件组成——它们只是不在**接口**上。一个模块可以同时有**内部 seam**(对实现私有,被它自己的测试用)和**外部 seam**(在它的接口处)。
- **删除测试**。想象删掉这个模块。复杂度消失 → 它没藏任何东西(是透传)。复杂度在 N 个调用方那里重新冒出 → 它在干活。
- **接口就是测试表面**。调用方和测试穿过同一个 seam。如果你想测**超过接口的东西**,模块形状大概错了。
- **一个适配器 = 假想的 seam。两个 = 真实的**。除非有东西在 seam 两侧真的变,不要引入 seam。

## 关系

- 一个 **Module** 恰有一个 **Interface**(它展现给调用方和测试的表面)。
- **Depth** 是 **Module** 的属性,度量是相对它的 **Interface**。
- 一个 **Seam** 是某个 **Module** 的 **Interface** 所在的位置。
- 一个 **Adapter** 坐在 **Seam** 上、满足 **Interface**。
- **Depth** 给调用方产出 **Leverage**,给维护者产出 **Locality**。

## 被拒绝的提法

- **Depth = 实现行数 / 接口行数比**(Ousterhout):鼓励往实现里塞水。我们用"深度 = 杠杆"代替。
- **"Interface" = TypeScript `interface` 关键字或类的 public 方法**:太窄——这里的 interface 包括调用方必须知道的**每一条事实**。
- **"Boundary"**:被 DDD 的 bounded context 重载。说 **seam** 或 **interface**。
