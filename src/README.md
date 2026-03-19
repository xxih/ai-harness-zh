# Source Asset Layout

`src/` 只负责保存**仍然属于当前总仓的共享源资产真相**。一旦某项能力已经能独立运行、独立安装、独立分发，就不应继续长期长在这里，而应升格成单主题 repo。

## 当前保留范围

- 跨 target 共享的 workflow 核心资产
- 仍然适合放在总仓内治理的通用资产治理能力
- 不直接承载某个工具独有的 hooks、settings、installer、发布脚本或完整运行包

## 当前约定

- 源资产统一放在 `src/domains/<domain>/`
- 每个领域内部按资产类型继续拆分，例如 `skills/`、`agents/`、`commands/`
- `skills/<name>/SKILL.md` 是 skill 主入口
- `agents/<name>.md` 是独立 agent prompt
- `commands/` 留给轻量任务入口；没有资产时保留空目录即可
- `targets/` 中的分发层可以为运行时需要做平铺、映射或打包，但真相仍以 `src/` 为准

## 毕业规则

以下资产应优先从 `src/` 毕业到独立 repo：

- 已经能独立安装、独立运行、独立分发的单主题能力
- 强绑定单一工具运行时的 hooks、settings、installer、发布脚本
- 需要自己的版本节奏、使用说明、验证矩阵和 issue 边界
- 用户理解它时，更像“一个工具包 / target 包 / 独立产品”

## 已毕业样例

- `learning-capture` -> `references/repos/learning-capture`
- `quality-workflows` -> `references/repos/quality-workflows`
