# 分发适配层

`src/` 下保存按领域组织的核心 prompt 源资产；`targets/` 下保存面向具体 AI 工具的分发快照与适配层。

约定：

- `src/domains/<domain>/` 是源资产真相来源
- `targets/<tool>/skills/`、`agents/`、`commands/` 可以按运行时要求收集、平铺或重组领域资产
- 在运行时分发资产之外，再叠加该工具需要的配置、包装说明和角色注册
- `targets/` 内容应与 `src/` 保持同步；当前阶段按需手动维护分发快照
- 如果未来某个工具需要真正可发布的打包产物，再额外生成到 `dist/`，不要手改生成物

当前已落地：

- `targets/codex/`：Codex CLI 的分发目录，收集 `src/domains/*` 资产并叠加项目级 `.codex/` 适配基线
