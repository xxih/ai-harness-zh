[English](README.md) | [中文](README.zh-CN.md)

# Happy Claude Skills

一组为 AI 编程助手设计的实用技能插件。

支持 **Claude Code**、**Codex**、**Factory Droid**、**OpenClaw**、**Cursor** 及 [40+ 编程助手](https://github.com/vercel-labs/skills#available-agents)。

## 包含的 Skills

### docx-format-replicator
从现有 Word 文档提取格式，并用相同格式生成新文档。

**适用场景：**
- 企业文档模板复制
- 批量生成格式一致的文档
- 技术规范文档系列
- 研制任务书等标准化文档

### video-processor
从 YouTube 等平台下载和处理视频。支持视频下载、音频提取、格式转换和 Whisper 语音转文字。

**适用场景：**
- 从 YouTube 等平台下载视频
- 从视频文件中提取音频
- 将视频转换为 MP4/WebM 格式
- 使用 Whisper 将音频/视频转录为文字

### wechat-article-writer
公众号文章自动化写作流程，4 步完成高质量文章：搜索资料、撰写文章、生成标题、排版优化。

**适用场景：**
- 撰写微信公众号文章
- 生成爆款标题
- 自媒体内容创作
- 文章排版优化

### trends-bulletin
多平台热词速报，采集 HuggingFace、GitHub、Hacker News、Product Hunt、Reddit、YouTube 6 个平台的热门趋势，并推送到 Telegram。

**适用场景：**
- 每日多平台趋势监控
- AI/科技热点发现
- 内容创作选题参考
- Telegram 自动化趋势推送

### browser
基于 Chrome DevTools Protocol 的浏览器自动化工具。启动 Chrome、导航页面、执行 JavaScript、截图、可视化选择 DOM 元素。

**适用场景：**
- 带登录状态的网页爬虫
- 视觉回归测试
- DOM 检查和数据提取
- 截图用于文档

## 安装方法

### 通用安装（推荐）

适用于 Claude Code、Codex、Droid、OpenClaw、Cursor 等 40+ 编程助手：

```bash
# 安装所有 skills（交互式选择 agent 和 skill）
npx skills add iamzhihuix/happy-claude-skills

# 安装指定 skills
npx skills add iamzhihuix/happy-claude-skills --skill browser --skill 1password

# 安装到指定 agent
npx skills add iamzhihuix/happy-claude-skills --agent codex
npx skills add iamzhihuix/happy-claude-skills --agent droid
npx skills add iamzhihuix/happy-claude-skills --agent openclaw

# 全部安装，跳过交互
npx skills add iamzhihuix/happy-claude-skills --all
```

### Claude Code 插件市场

```
/plugin marketplace add iamzhihuix/happy-claude-skills
/plugin install browser@happy-claude-skills
```

### 本地开发

```bash
git clone https://github.com/iamzhihuix/happy-claude-skills.git

# Claude Code
claude --plugin-dir /path/to/happy-claude-skills

# 任意 agent
npx skills add ./happy-claude-skills --all
```

## 使用方法

安装后，直接描述需求即可 — 你的 agent 会自动识别并调用相应的 skill：

> "我有一个研制任务书模板，需要用相同格式生成5份新文档"

> "下载这个 YouTube 视频并转录成文字"

> "帮我写一篇关于 AI 编程技巧的公众号文章"

> "抓取这个网页的产品信息"

> "帮我发一下热词速报"

> "把这个 API key 存到 1Password"

## 依赖

### docx-format-replicator
- Python 3.7+
- python-docx

```bash
pip install python-docx
```

### video-processor
- Python 3.7+
- yt-dlp
- FFmpeg
- openai-whisper

```bash
pip install yt-dlp openai-whisper
brew install ffmpeg  # macOS
```

### trends-bulletin
- Bun（无外部依赖，使用内置 fetch）

```bash
# 安装 Bun（如未安装）
curl -fsSL https://bun.sh/install | bash
```

### browser
- Node.js 18+
- puppeteer-core
- Google Chrome

```bash
npm install --prefix skills/browser
```

## 项目结构

```
happy-claude-skills/
├── AGENTS.md                    # Agent 通用说明（Codex 等）
├── .claude-plugin/
│   └── marketplace.json         # Claude Code 市场配置
├── skills/
│   ├── docx-format-replicator/
│   │   ├── SKILL.md             # Skill 定义
│   │   ├── scripts/             # Python 脚本
│   │   ├── assets/              # 示例文件
│   │   └── references/          # 参考文档
│   ├── video-processor/
│   │   ├── SKILL.md             # Skill 定义
│   │   └── scripts/             # Python 脚本
│   ├── wechat-article-writer/
│   │   └── SKILL.md             # Skill 定义
│   ├── trends-bulletin/
│   │   ├── SKILL.md             # Skill 定义
│   │   └── scripts/             # TypeScript 脚本
│   └── browser/
│       ├── SKILL.md             # Skill 定义
│       ├── package.json         # Node.js 依赖
│       └── scripts/             # Node.js 脚本
├── README.md
└── LICENSE
```

## 鸣谢

- **video-processor** skill 改编自 [@disler](https://github.com/disler) 的 [claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) 项目
- **browser** skill 基于 [Mario Zechner](https://mariozechner.at) 的文章 [What if you don't need MCP?](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/) ([GitHub](https://github.com/badlogic/browser-tools))，整理自 [Factory.ai](https://docs.factory.ai/guides/skills/browser)

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
