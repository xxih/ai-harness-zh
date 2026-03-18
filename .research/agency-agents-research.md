# Research Note

## 目标

- 要解决的问题：把 `git@github.com:msitarzewski/agency-agents.git` 纳入 `references/repos/` 作为本地参考仓库，并提炼它对当前 `my-ai-harness` 的可复用模式，形成后续资产设计与分发适配的研究结论。
- 语言/框架：Markdown prompt 资产、YAML frontmatter、shell 转换/安装脚本。
- 约束：
  - 当前仓库默认中文沉淀，且核心资产以 `src/skills/`、`src/agents/`、`targets/` 为中心。
  - 当前仓库目标是“可版本化 prompt 资产工作区”，不是直接维护一个超大规模 agent 市场。
  - 外部参考仓库只放在 `references/repos/`，不直接改写其中内容。

## 本地候选

- 来源：`README.md`
  - 可复用点：当前仓库已经明确 `src/` 作为工具无关源资产、`targets/` 作为分发适配层、`.research/` 作为研究记录落点。
  - 风险：现阶段只有 `targets/codex/`，对多工具分发的脚本化流程还没有统一骨架。
- 来源：`targets/README.md`
  - 可复用点：已经确立“`src` 为源、`targets/<tool>` 为镜像/适配”的方向，和外部参考中的多工具分发思路存在可对接空间。
  - 风险：如果直接引入外部仓库的工具格式，容易把当前仓库从“源资产优先”拉回到“为某个平台直接写 prompt”。
- 来源：`src/skills/search-first/SKILL.md`
  - 可复用点：要求每次研究都沉淀为项目内记录，并给出 `adopt` / `adapt` / `build` 结论。
  - 风险：如果只做资料摘录，不把结论映射回当前仓库的资产结构，研究价值会偏低。
- 来源：`references/quality-agent-landscape.md`
  - 可复用点：仓库之前已经用外部参考仓库来校准质量角色粒度，说明“参考仓库 -> 提炼判断 -> 回写正式结论”的路径可行。
  - 风险：该文偏质量角色盘点，无法直接回答多工具分发、frontmatter 结构、编排文档如何借鉴。

## 外部候选

- 来源：`references/repos/agency-agents/README.md`
  - 可复用点：
    - 仓库定位清晰，是一个按业务域分组的 agent 资产库。
    - 原生源格式统一为 `.md + YAML frontmatter`。
    - 对使用者非常友好，直接给出 roster、激活方式和工具入口。
  - 风险：
    - 该仓库以大规模英文 agent roster 为中心，不适合直接映射到当前仓库的中文 skill-first 结构。
    - 角色数量很大，若照搬会迅速失控。
- 来源：`references/repos/agency-agents/CONTRIBUTING.md`
  - 可复用点：
    - 定义了比较完整的 agent 文件模板。
    - 明确区分 persona 与 operations 两组 section，便于后续转换脚本做结构化切分。
    - frontmatter 字段不仅有 `name`、`description`，还包含 `color`、`emoji`、`vibe`，必要时可扩展。
  - 风险：
    - 当前仓库的 skill/agent 资产还不需要这么重的“人格化包装”；过早引入会增加写作负担。
- 来源：`references/repos/agency-agents/strategy/QUICKSTART.md`
  - 可复用点：
    - 把大规模协作抽象成 `NEXUS-Full`、`NEXUS-Sprint`、`NEXUS-Micro` 三种模式。
    - 用户入口非常直接，适合作为“怎么启动一套编排流程”的参考写法。
  - 风险：
    - 该编排体系预设了大量 agent 常驻可用，和当前仓库“小而精”的资产策略不完全一致。
- 来源：`references/repos/agency-agents/strategy/coordination/handoff-templates.md`
  - 可复用点：
    - 对 handoff、QA PASS/FAIL、phase gate、escalation 都给了标准模板。
    - 很适合作为 `agent-orchestration` 类 skill 的 reference，而不是直接变成独立 agent。
  - 风险：
    - 如果原样引入，文档会显得偏重流程制度，不够贴近当前仓库的最小可复用风格。
- 来源：`references/repos/agency-agents/specialized/agents-orchestrator.md`
  - 可复用点：
    - 把 orchestrator 的职责写得非常清楚：阶段推进、上下文传递、QA loop、失败重试、状态汇报。
    - 对“主 agent 负责什么，不负责什么”有较强示范价值。
  - 风险：
    - 它偏“执行总控代理”，而当前仓库的 `agent-orchestration` 更像“让主 agent 遵守的一套工作纪律”，抽象层级不同。
- 来源：`references/repos/agency-agents/testing/testing-evidence-collector.md`
  - 可复用点：
    - 强调 evidence-based QA，报告结构具体，可作为质量角色 prompt 写法参考。
  - 风险：
    - 该 agent 深度依赖特定截图流程和“默认找出 3-5 个问题”的人格化设定，不适合直接迁入当前仓库。
- 来源：`references/repos/agency-agents/testing/testing-reality-checker.md`
  - 可复用点：
    - 对“默认不轻易放行”的验证门禁写得非常鲜明。
    - 能为当前仓库的 `quality-verify` / `quality-review` 提供语气和门禁标准上的参考。
  - 风险：
    - 仓库内已有质量 skill 体系，直接再抽一个同类独立 agent 会造成角色重复。
- 来源：`references/repos/agency-agents/scripts/convert.sh`
  - 可复用点：
    - 明确做到了“源格式一次维护，多工具生成产物”。
    - 覆盖 `claude-code`、`copilot`、`antigravity`、`gemini-cli`、`opencode`、`openclaw`、`cursor`、`aider`、`windsurf`、`qwen` 等目标。
    - 转换逻辑依赖 frontmatter 与 section 约定，而不是手工维护多份副本。
  - 风险：
    - 当前仓库的资产类型不止 agent，还有 skill、command、eval；不能简单复刻它的 agent-only 转换器。
- 来源：`references/repos/agency-agents/scripts/install.sh`
  - 可复用点：
    - 把“生成产物”和“安装到用户环境”拆成两层脚本，边界清楚。
    - 区分 home-scoped 与 project-scoped 工具，安装说明相对完备。
  - 风险：
    - 当前仓库还没有进入“对外安装分发”阶段，过早建设 installer 容易超前设计。

## 关键观察

### 1. 这是一个“大量 agent + 少量 doctrine”的仓库

- 统计上，`agency-agents` 在业务域目录下共有约 156 个 agent Markdown 文件，分布在 `engineering/`、`marketing/`、`testing/`、`specialized/` 等 13 个分类中。
- 同时它还有 `strategy/` 下的 NEXUS 协调文档、`examples/` 示例工作流，以及 `scripts/` 下的转换/安装脚本。
- 也就是说，它的核心不是单个 prompt 写得多精致，而是形成了“角色库 + 编排手册 + 分发脚本”的完整资产层次。

### 2. 它的源资产格式非常适合做多工具转换

- 原仓库主要用统一的 `.md + YAML frontmatter` 作为源格式。
- `CONTRIBUTING.md` 进一步要求 section 命名稳定，便于 `convert.sh` 把同一份源资产切到不同工具目标。
- 这和当前仓库“`src/` 为源、`targets/` 为分发”的方向是同向的，只是它更偏 agent-only，而我们是 skill/agent/command/eval 并存。

### 3. 它对多 agent 协作的沉淀比当前仓库更制度化

- `strategy/QUICKSTART.md` 给出不同规模的编排模式。
- `specialized/agents-orchestrator.md` 把 orchestrator 的职责写成明确阶段与质量回路。
- `strategy/coordination/handoff-templates.md` 则把 handoff、FAIL 重试、升级等写成模板。
- 当前仓库已有 `src/skills/agent-orchestration/`，但更强调“主 agent 如何组织工作”，没有把 handoff 模板和 phase gate 模板沉淀得这么显式。

### 4. 它的质量角色写法值得参考，但不适合整套照搬

- `engineering/engineering-code-reviewer.md`、`testing/testing-evidence-collector.md`、`testing/testing-reality-checker.md` 的共同特点是：
  - 角色边界鲜明；
  - checklist 和报告模板具体；
  - 门禁态度很清楚。
- 这些都适合用来提升当前仓库已有质量资产的表达强度。
- 但当前仓库已经明确选择“少量独立 agent + 更多 skill 内流程”的路线，因此不应因为这个参考仓库角色丰富，就回退到“大量平铺 agent 文件”。

### 5. 它对当前仓库最大的启发，不是新增多少角色，而是补齐资产层次

- 当前仓库现状：
  - 核心资产规模小，`src/skills/` 约 10 个目录，`src/agents/` 仅 1 个文件；
  - 分发侧目前只有 `targets/codex/`；
  - 对多工具分发还主要停留在目录同构层面。
- `agency-agents` 的参考价值主要有三类：
  1. 源资产元数据设计
  2. 编排与 handoff reference
  3. 转换脚本与安装脚本分层

## 对当前仓库的整合判断

### 可以吸收的部分

- `targets/` 演进方向
  - 可以参考 `convert.sh` / `install.sh` 的分层方式，把“生成目标工具产物”和“安装到工具目录”视为两层独立能力。
  - 当后续不止支持 `codex` 时，这个结构尤其有价值。
- `agent-orchestration` 的参考资料
  - 可以把 `handoff-templates.md`、`QUICKSTART.md` 这种文档形式当作 reference 输入，增强当前仓库的编排 skill。
  - 重点是吸收阶段切分、失败升级、handoff 模板，而不是照抄 NEXUS 名词体系。
- 质量资产表达方式
  - `code-reviewer`、`reality-checker` 这类 prompt 写法很适合参考其“角色边界 + checklist + 输出模板”的组织方式。
  - 但应继续服务于当前已有的 `quality-*` skill 和唯一 reviewer agent。
- 源资产元数据
  - 若未来要做自动化转换，可考虑为 `src/agents/` 或 `src/skills/` 增加更稳定的 frontmatter 约定。
  - 但只应增加真正被转换链路消费的字段，不要先为“可能会用到”堆字段。

### 不建议吸收的部分

- 不建议引入它的大规模 agent 分类法。
  - 当前仓库不是 agent marketplace，没必要复制 156 个角色的组织方式。
- 不建议把当前 skill-first 结构改造成 agent-first。
  - 当前仓库很多能力本质上更适合表达为 workflow / skill，而不是人格化独立 agent。
- 不建议立即建设完整 installer。
  - 在目标工具数量和发布方式还不稳定时，先把 `src -> targets` 的同步做清楚，比提前做安装器更重要。

## 决策

- `adapt`
- 理由：
  - `agency-agents` 提供了很强的参考价值，但主要体现在结构和方法，而不是具体角色内容。
  - 当前仓库应吸收它在多工具转换、编排 handoff、质量角色写法上的骨架经验。
  - 当前仓库不应采用它的“大量 agent 文件平铺”策略，否则会偏离“少量高价值、可评估、可版本化 prompt 资产”的目标。

## 下一步

- 研究建议：
  - 后续若开始扩展 `targets/codex/` 之外的新工具，可先单独研究“当前仓库自己的 `convert/install` 最小骨架”，并以 `agency-agents/scripts/convert.sh`、`agency-agents/scripts/install.sh` 作为主要外部参考。
  - 后续若增强 `src/skills/agent-orchestration/`，可优先参考 `strategy/coordination/handoff-templates.md` 的模板化写法。
  - 后续若改进质量资产文案，可参考 `engineering/engineering-code-reviewer.md` 与 `testing/testing-reality-checker.md` 的输出结构和门禁语气。
- 实现建议：
  - 保持 `references/repos/agency-agents/` 作为长期本地参考仓库。
  - 不把该仓库内容直接复制进 `src/`；只在需要的任务里按文件路径定点引用。
- 测试建议：
  - 当前仅新增参考仓库与研究文档，不涉及 `src/` 资产行为修改。
  - 仍按仓库规则执行一次 `python3 scripts/validate_assets.py`，确认结构性校验未受影响。
