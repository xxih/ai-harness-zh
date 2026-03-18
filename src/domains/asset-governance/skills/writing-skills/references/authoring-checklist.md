# Writing Skills Checklist

## 1. 先判断资产类型

| 如果你要沉淀的是 | 优先落点 |
| --- | --- |
| 跨任务、靠判断执行、需要被模型主动发现的稳定能力 | `skills/<name>/SKILL.md` |
| 仓库级、领域级长期公共规则 | 对应目录的 `_AGENTS.md` |
| 目录结构说明、人工导览 | 对应目录的 `README.md` |
| 轻量入口、固定命令壳、显式 slash 路由 | `commands/` |
| 运行时 metadata、安装、hooks、平台 wiring | `targets/` |
| 还未稳定、只是候选经验 | `.learned/` |

判断不过关时，先不要写 skill。

## 2. frontmatter 检查

- [ ] 只包含 `name` 与 `description`
- [ ] `name` 使用稳定、可搜索的连字符命名
- [ ] `description` 只写触发条件、症状、上下文
- [ ] `description` 不偷跑 workflow、步骤数量或子 skill 链路
- [ ] `description` 不夹带平台特定 runtime 细节，除非这个 skill 天生就是平台专属

## 3. 正文最小结构

- [ ] 说明这个 skill 解决什么问题
- [ ] 明确何时使用 / 不适用
- [ ] 说明最小产物或落点
- [ ] 给出可执行工作流，而不是抽象口号
- [ ] 写清纪律约束与常见误用
- [ ] 只在必要时引用 `references/`、`scripts/`、`assets/`

## 4. 资源拆分规则

### 保留在 `SKILL.md`

- 核心目标
- 适用边界
- 最小流程
- 必须遵守的纪律

### 下沉到 `references/`

- 详细 checklist
- 长模板
- 长示例
- 大块参考资料

### 下沉到 `scripts/`

- 反复重写且适合确定性执行的脚本
- 需要减少手工出错率的生成 / 校验步骤

### 下沉到 `assets/`

- 输出阶段会直接消费的模板、素材、样板文件

## 5. 目录卫生

- [ ] skill 目录中没有额外 README、安装说明或 CHANGELOG
- [ ] 没有把一次性研究过程直接塞进正式资产
- [ ] 没有把 target-specific 文案写进 source 资产
- [ ] 仓库若维护分发快照，已同步对应 `targets/`
