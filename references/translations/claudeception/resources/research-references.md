# 研究参考资料

本文档汇总了影响 Claudeception 设计的学术研究。

## 核心论文

### Voyager: An Open-Ended Embodied Agent with Large Language Models

**作者**：Wang, Xie, Jiang, Mandlekar, Xiao, Zhu, Fan, Anandkumar  
**发布时间**：2023 年 5 月  
**URL**：https://arxiv.org/abs/2305.16291

**关键贡献**：首个由 LLM 驱动、具备 embodied lifelong learning 能力并采用 skill library 架构的 agent。

**实际采用的相关概念**：

1. **持续增长的 Skill Library**：Voyager 维护了一个“不断增长的、以可执行代码形式存储和检索复杂行为的 skill library”。这启发了我们把 Claude Code skills 作为可执行知识包来提取和保存。

2. **组合式 Skills**：“Voyager 开发出的 skills 具备时间延展性、可解释性和可组合性，因此能快速叠加 agent 的能力，并缓解灾难性遗忘。”我们的 skill 结构也追求类似的可组合性。

3. **自我验证**：Voyager 在把 skill 写入库之前，会先做“self-verification for program improvement”。我们在提炼前设置质量门槛，也借鉴了这一点。

4. **迭代式提示**：“将环境反馈、执行错误纳入其中的 iterative prompting mechanism” 影响了我们的复盘模式设计。

---

### CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution

**作者**：[Research Team]  
**发布时间**：2024 年 12 月  
**URL**：https://arxiv.org/abs/2512.23880

**关键贡献**：一个自演化的 agent 框架，展示了从 “LLM + tool use” 过渡到 “LLM + skill acquisition”。

**实际采用的相关概念**：

1. **用于学习的 Meta-Skills**：CASCADE 展示了“通过 web search 和 code extraction 的持续学习，以及通过 introspection 的自我反思”。我们的这个 skill 本身就是一个“获取 skills 的 meta-skill”。

2. **知识编纂**：“CASCADE accumulates executable skills that can be shared across agents”——这一原则推动了我们把知识提炼并存储成 skill 的做法。

3. **记忆整合**：该框架使用 memory consolidation 来防止遗忘并提升复用能力。我们的 skill library 也承担类似角色。

---

### SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience

**作者**：Sun et al.  
**发布时间**：2025 年 8 月  
**URL**：https://arxiv.org/abs/2508.04700

**关键贡献**：一个让 agent 能通过与陌生软件交互而自主演化的框架。

**实际采用的相关概念**：

1. **经验学习**：“SEAgent empowers computer-use agents to autonomously master novel software environments via experiential learning, where agents explore new software, learn through iterative trial-and-error.” 我们的复盘模式正是用来捕捉这种试错学习。

2. **从失败与成功中学习**：“The agent's policy is optimized through experiential learning from both failures and successes.” 我们既会从成功解法里提炼 skill，也会从调试过程里提炼。

3. **课程生成**：SEAgent 使用 “Curriculum Generator” 逐步生成更丰富的任务。我们的 skill 描述则通过语义匹配，在未来类似场景里把相关 skill 召回。

---

### Reflexion: Language Agents with Verbal Reinforcement Learning

**作者**：Shinn et al.  
**发布时间**：2023 年 3 月  
**URL**：https://arxiv.org/abs/2303.11366

**关键贡献**：一个通过语言反馈和自我反思进行 verbal reinforcement 的框架。

**实际采用的相关概念**：

1. **自我反思提示**：“Reflexion converts feedback from the environment into linguistic feedback, also referred to as self-reflection.” 我们的自我反思提示直接受到这一思路启发。

2. **为未来试验保留记忆**：“These experiences (stored in long-term memory) are leveraged by the agent to rapidly improve decision-making.” 在这里，skills 承担了长期记忆的角色。

3. **语言式强化**：Reflexion 不使用标量奖励，而是使用自然语言形式的“细粒度反馈”。我们的 skill 描述正是在承载这种细粒度知识。

---

### EvoFSM: Controllable Self-Evolution for Deep Research with Finite State Machines

**作者**：[Research Team]  
**发布时间**：2024

**关键贡献**：一个带经验池的自演化框架，用于持续学习。

**实际采用的相关概念**：

1. **自演化记忆**：“EvoFSM integrates a Self-Evolving Memory mechanism, which distills successful strategies and failure patterns into an Experience Pool to enable continuous learning and warm-starting for future queries.”

2. **经验池**：把策略保存起来、供之后检索的概念，直接影响了我们的 skill library 设计。

---

## 支撑性研究

### Professional Agents: Evolving LLMs into Autonomous Experts

**URL**：https://arxiv.org/abs/2402.03628

描述了一个通过持续学习让 agent 获得专业能力的框架。它影响了我们对于“什么样的知识值得提炼成 skill”的质量判断。

### Self-Reflection in LLM Agents: Effects on Problem-Solving Performance

**URL**：https://arxiv.org/abs/2405.06682

一项证明自我反思能提升效果的实证研究。它验证了我们通过反思提示识别可提炼知识的做法。

### Building Scalable and Reliable Agentic AI Systems

一份关于 agentic AI 的综合性综述，覆盖 memory architectures、tool use 和 continuous learning，为我们的设计提供了更宽的架构背景。

---

## Claude Code Skills 文档

### Anthropic Engineering Blog: Equipping Agents for the Real World with Agent Skills

**URL**：https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

**关键洞察**：

1. **渐进式披露**：“Skills let Claude load information only as needed”——这让系统可以扩展到很多 skills，而不会把上下文窗口撑爆。

2. **未来愿景**：“We hope to enable agents to create, edit, and evaluate Skills on their own, letting them codify their own patterns of behavior into reusable capabilities.” 这个 skill 正是在实现这条愿景。

3. **Skill 像 onboarding**：“Building a skill for an agent is like putting together an onboarding guide for a new hire.” 我们的模板就采用了这种心智模型。

### Claude Code Skills Documentation

**URL**：https://code.claude.com/docs/en/skills

**关键洞察**：

1. **SKILL.md 结构**：YAML frontmatter + markdown instructions
2. **Description 的重要性**：语义匹配高度依赖高质量描述
3. **Allowed Tools**：skill 可以限制或启用特定工具
4. **位置选项**：支持用户级与项目级安装

---

## 实际采用的设计模式

### 来自 Voyager
- 把 skill library 作为可执行代码
- 写入 skill library 前先做自我验证
- 以可组合 skill 的方式构建能力

### 来自 CASCADE
- 用 meta-skills 实现学习
- 把知识编纂成可共享格式
- 做记忆整合

### 来自 SEAgent
- 同时从成功与失败中学习
- 通过试错进行经验学习
- skill 复杂度渐进提升

### 来自 Reflexion
- 使用自我反思提示
- 用语言反馈替代标量奖励
- 把知识存入长期记忆

### 来自 EvoFSM
- 使用经验池
- 从会话中蒸馏策略
- 为未来任务提供 warm-start

---

## 引用格式

如果你需要在学术工作中引用这个 skill：

```
@misc{claudeception,
  title={Claudeception: Autonomous Skill Extraction for LLM Agents},
  author={Claude Code},
  year={2024},
  note={Implements continuous learning patterns from Voyager, CASCADE, SEAgent, and Reflexion research}
}
```
