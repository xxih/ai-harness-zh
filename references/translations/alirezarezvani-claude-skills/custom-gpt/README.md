# Custom GPTs — 面向 ChatGPT 的 Agent Skills

> 基于 Agent Skills 库构建的 **6 个 Custom GPTs**。可在 ChatGPT 中免费使用，无需安装、无需 API key、无需额外 setup。

这些 GPTs 把 [Agent Skills](https://github.com/alirezarezvani/claude-skills) 仓库中的生产级专业能力直接带进 ChatGPT。每个 GPT 都把特定领域的 workflows、frameworks 与决策工具打包成可对话的界面。

---

## 可用 GPTs

### Solo Founder

**最适合：** 独自做产品的技术型创始人。覆盖架构决策、go-to-market、招聘、融资与时间管理，全部从 solo operator 视角出发。

**它能做什么：**

- 面向一人团队的产品路线图优先级排序
- 带 build-vs-buy 分析的技术架构决策
- 在有限预算与时间内做 go-to-market 规划
- 融资准备与 pitch deck 审阅

[**→ 在 ChatGPT 中打开**](https://chatgpt.com/g/g-69b3157947e8819180c8e4ac609d5041-solo-founder)

---

### SEO Audit Expert

**最适合：** 想拿到可执行 SEO 改进建议的开发者、营销人员与创始人。不是泛泛建议，而是带具体修复动作的结构化审计工作流。

**它能做什么：**

- 完整的技术 SEO 审计（Core Web Vitals、crawlability、indexing）
- On-page 优化与关键词布局策略
- 面向竞品的内容缺口分析
- 站点架构与内部链接评审

[**→ 在 ChatGPT 中打开**](https://chatgpt.com/g/g-69b3b0a690ac819189c127be7d1deb03-seo-audit-expert)

---

### Content Strategist

**最适合：** 内容团队、独立创作者和营销人员，用来规划“写什么”和“怎么分发”。先做策略，再做写作。

**它能做什么：**

- 以 pillar / spoke 结构规划 topic clusters
- 设计内容日历与发布节奏
- 受众研究与 persona mapping
- 跨渠道分发策略（SEO、social、email、community）

[**→ 在 ChatGPT 中打开**](https://chatgpt.com/g/g-69b3afc41c608191a6ee30941c5bdddb-content-strategist)

---

### Product Manager Toolkit

**最适合：** 需要结构化框架来做产品决策、用户研究和 sprint planning 的产品经理与创始人。

**它能做什么：**

- 带 acceptance criteria 的 user story 编写
- 生成带清晰范围与成功指标的 PRD
- Sprint planning 与 backlog prioritization
- 功能影响评分（RICE、ICE、weighted scoring）
- 带定位框架的竞品分析

[**→ 在 ChatGPT 中打开**](https://chatgpt.com/g/g-69b32caad22c81919522ca21062adec8-product-manager-toolkit)

---

### Conversion Copywriter

**最适合：** 写需要转化的文案的人，例如 landing page、pricing page、email sequence、CTA、headline。重点不是泛写作，而是 conversion-first 框架。

**它能做什么：**

- Landing page 文案，含 headline 变体与 CTA 优化
- 邮件序列设计（welcome、nurture、re-engagement）
- 带异议处理的 pricing page 文案
- 带理由说明的 A/B test 文案变体

[**→ 在 ChatGPT 中打开**](https://chatgpt.com/g/g-69b327d9545c8191b3711b75b4a88a94-conversion-copywriter)

---

### CTO Advisor

**最适合：** CTO、VP Engineering 以及需要做架构、团队和技术决策的技术负责人。适合拿来处理困难取舍。

**它能做什么：**

- 带优先级矩阵的技术债评估
- 团队扩张模型（何时招人、招什么角色、如何组织）
- 带 trade-off 分析的 ADR
- 技术评估框架（build vs buy、vendor selection）
- 工程指标与 DORA benchmarks

[**→ 在 ChatGPT 中打开**](https://chatgpt.com/g/g-69b32673238c8191ba3a0d1627f0e8a7-cto-advisor)

---

## 使用方式

1. 点击上面的任意 **“在 ChatGPT 中打开”** 链接
2. 直接开始对话，无需额外配置
3. GPT 会调用 Agent Skills 库中的结构化 workflows

**适用计划：** ChatGPT Plus、Pro 和 Team。

## Want More?

这些 GPT 来自开源 [Agent Skills](https://github.com/alirezarezvani/claude-skills) 库，该库提供 **177 个 skills、16 个 agents、3 个 personas**，适用于多种 AI 编码工具。

如果你使用 Claude Code、Codex、Gemini CLI、Cursor 或其他 AI 编码工具，可以直接安装完整 skill 库：

```bash
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills && ./scripts/install.sh
```

上面的 GPT 只是一个小样本。完整库还覆盖 engineering、product、marketing、compliance、finance、healthcare 等领域。

---

## Links

- **Repository:** [github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
- **Documentation:** [alirezarezvani.github.io/claude-skills](https://alirezarezvani.github.io/claude-skills/)
- **Skills Browse:** [Full skill catalog](https://alirezarezvani.github.io/claude-skills/skills/)

## License

这些 GPT 配置本身是专有的；底层 Agent Skills 库使用 [MIT license](https://github.com/alirezarezvani/claude-skills/blob/main/LICENSE)。
