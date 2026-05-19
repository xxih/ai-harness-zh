# Deepening(加深)

> 原文:[DEEPENING.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/DEEPENING.md)

考虑依赖之后,怎么安全地加深一簇浅模块。**假设你已经熟悉 [LANGUAGE.md](LANGUAGE.md) 的词表**——**module**、**interface**、**seam**、**adapter**。

## 依赖分类

评估一个加深候选时,**先给它的依赖分类**。类别决定加深后的模块怎么跨 seam 测试。

### 1. In-process(进程内)

纯计算、内存状态、无 I/O。**永远可加深**——合并模块、直接通过新接口测试。**不需要适配器**。

### 2. Local-substitutable(本地可替身)

依赖有本地测试替身(PGLite 替 Postgres、内存文件系统)。替身存在就可加深。加深后的模块用替身在测试套件里跑。**seam 在内部**;模块外部接口上不暴露 port。

### 3. Remote but owned(自有但跨网)——Ports & Adapters

自己跨网络边界的服务(微服务、内部 API)。**在 seam 处定义 port(接口)**。深模块拥有逻辑;传输层作为 **adapter** 注入。**测试用 in-memory adapter**。**生产用 HTTP/gRPC/queue adapter**。

推荐形状:*"在 seam 处定义 port,生产实现 HTTP adapter,测试用 in-memory adapter,这样虽然部署跨网络,逻辑仍在一个深模块里。"*

### 4. True external(真外部)—— Mock

你不控制的第三方服务(Stripe、Twilio 等)。加深后的模块把外部依赖作为注入 port;测试提供 mock adapter。

## Seam 纪律

- **一个适配器 = 假想 seam。两个适配器 = 真 seam**。除非至少有两个适配器有理由存在(通常生产 + 测试),不要引入 port。单适配器 seam 只是多了层间接。
- **内部 seam vs 外部 seam**。深模块可以同时有内部 seam(对实现私有,被自己的测试用)和外部 seam(在接口处)。**别只因为测试用了内部 seam 就把它暴露在接口里**。

## 测试策略:替换,不要叠层

- 加深后的模块接口上有测试存在以后,**老的浅模块单元测试就成了浪费——删掉**。
- 在加深后的模块接口处写新测试。**接口就是测试表面**。
- 测试**通过接口断言可观测结果**,不断言内部状态。
- 测试应该在内部重构中存活——**描述行为,不是实现**。如果一个测试在实现变化时也必须变,它在测"接口之外的东西"。
