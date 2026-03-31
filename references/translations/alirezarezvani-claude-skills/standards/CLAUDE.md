# Standards Library - Claude Code Guidance

本指南说明如何使用 standards library，让所有 skills 与 agents 都保持一致质量。

## Standards 总览

**位置：** `standards/`

**可用标准：**

1. **communication/**：沟通原则与响应协议
2. **quality/**：代码质量、测试与验证标准
3. **git/**：Git 工作流、conventional commits、分支策略
4. **documentation/**：Markdown 质量、结构一致性、持续维护文档
5. **security/**：secret 检测、依赖安全、输入校验

## 什么时候引用 Standards

### Communication Standards

**适用场景：**

- 编写 agent 文档
- 创建 `SKILL.md`
- 撰写面向用户的内容
- 提供技术指导

**核心原则：**

- 绝对诚实，不做缓冲式粉饰
- 零废话，去掉模糊表达
- 务实导向，只给可执行建议
- 文件节约，优先编辑现有文件而不是新增

**位置：** `communication/communication-standards.md`

### Quality Standards

**适用场景：**

- 创建 Python 自动化工具
- 编写 agent workflows
- 实现 skill 特性
- 测试集成点

**重点领域：**

- Python 工具质量（PEP 8、type hints、docstrings）
- Agent workflow 清晰度（至少 3 个 workflows）
- 测试要求（功能、集成、文档）
- 完成标准（零缺陷交接、验证要求）

**位置：** `quality/quality-standards.md`

### Git Workflow Standards

**适用场景：**

- 提交代码变更
- 创建 feature branches
- 打 release tag
- 编写 commit message

**提交格式：**

```bash
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**类型：** `feat`、`fix`、`docs`、`style`、`refactor`、`perf`、`test`、`chore`、`ci`

**示例：**

```bash
feat(agents): implement cs-content-creator agent
fix(seo-optimizer): correct keyword density calculation
docs(README): add agent catalog section
```

**位置：** `git/git-workflow-standards.md`

### Documentation Standards

**适用场景：**

- 写 `SKILL.md`
- 创建 agent 文档
- 更新 `README.md`
- 编写 reference guides

**最佳实践：**

- 单个 `CLAUDE.md` 最多 200 行
- 统一 Markdown 格式规范（标题、列表、代码块）
- 维护活文档（`README`、`CLAUDE`、`AGENTS`）
- 链接校验，不能出现 404 或断链

**位置：** `documentation/documentation-standards.md`

### Security Standards

**适用场景：**

- 编写 Python 脚本
- 处理用户输入
- 管理依赖
- 提交代码

**关键检查：**

- 不得硬编码 API keys、密码或 tokens
- 敏感数据必须走环境变量
- 所有用户输入都要校验
- 执行依赖安全审计

**位置：** `security/security-standards.md`

## Standards 应用工作流

### 新建 Skills 时

```bash
# 1. 参考 communication standards
cat standards/communication/communication-standards.md

# 2. 查看 quality standards，编写 Python tools
cat standards/quality/quality-standards.md

# 3. 按 documentation standards 写 SKILL.md
cat standards/documentation/documentation-standards.md

# 4. 对脚本应用 security standards
cat standards/security/security-standards.md

# 5. 提交时使用 git standards
cat standards/git/git-workflow-standards.md
```

### 新建 Agents 时

```bash
# 1. Communication：写清晰、可执行的 agent 文档
# 2. Quality：至少 3 个 workflows，并验证相对路径
# 3. Documentation：遵循 agent template 结构
# 4. Git：使用 feat(agents) scope 的 conventional commit
```

## Standards 层级

**优先级顺序：**

1. **Security**：不可协商，始终强制
2. **Quality**：必须做到零缺陷交接
3. **Git**：所有变更都用 conventional commits
4. **Documentation**：活文档必须保持最新
5. **Communication**：清晰、务实、可执行

## Standards 合规检查表

### 提交代码前

- [ ] Communication：文档清晰、可执行
- [ ] Quality：所有测试通过，代码已审查
- [ ] Git：commit message 符合 conventional 格式
- [ ] Documentation：必要时已更新活文档
- [ ] Security：无 secrets、输入已校验、依赖安全

### 创建 PR 前

- [ ] 全部 standards 检查已通过
- [ ] 已更新相关文档
- [ ] 示例已经测试可用
- [ ] 没有坏链接或失效引用

## 相关文档

- **主 CLAUDE.md：** `../CLAUDE.md`
- **Agent Development：** `../agents/CLAUDE.md`
- **Domain Skills：** 见主 `CLAUDE.md` 里的导航图

---

**Last Updated:** November 5, 2025  
**Standards Count:** 5 comprehensive standards  
**Enforcement:** Required for all skills and agents
