# harness分层吸收与最小skill化

背景：

- `references/repos/` 中的 `everything-claude-code`、`superpowers`、`oh-my-opencode` 都是成熟 harness，但体量大、耦合高、平台假设重。
- 当前仓库目标是沉淀可复用的 prompt 资产，不适合一次性整体移植完整 harness。
- 需要先把参考仓库按能力类别拆开，识别哪些能力适合沉淀为“最小 skill”，哪些应继续保留为参考、不立即吸收。

目标：

- 建立三个参考仓库中 coding 相关能力的分类图，而不是按仓库逐个照搬。
- 形成“最小化 coding skill 吸收”策略，明确优先级、边界、非目标和落地顺序。
- 直接落地两类第一波最小 coding skill：研究检索与质量保障，并说明应如何以 eval-first 方式推进。

约束：

- 不做一个大一统、平台强绑定的新 harness。
- 优先保留工具无关、意图清晰、边界稳定的 coding skill 资产。
- 对非平凡 skill 落地，遵循先 eval、后资产、再校验的节奏。
- 暂不优先吸收重运行时能力，如多 agent 调度、复杂 hooks、深度工具集成、平台安装脚本。
