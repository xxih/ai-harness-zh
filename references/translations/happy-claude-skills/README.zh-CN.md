[翻译说明](README.md)

# Happy Claude Skills

一组为 Claude Code 设计的实用 skill 插件。

## 包含的 Skills

### docx-format-replicator
从现有 Word 文档中提取格式，并用相同格式生成内容不同的新文档。

**适用场景：**
- 企业文档模板复刻
- 批量生成格式一致的文档
- 技术规范文档系列化生成
- 研制任务书等标准化文档

### video-processor
从 YouTube 等平台下载并处理视频。支持视频下载、音频提取、格式转换，以及使用 Whisper 进行语音转文字。

**适用场景：**
- 从 YouTube 等平台下载视频
- 从视频文件中提取音频
- 将视频转换为 MP4/WebM 格式
- 使用 Whisper 将音频或视频转录为文本

### wechat-article-writer
公众号文章自动化写作流程，用 4 个步骤完成高质量文章：检索资料、撰写正文、生成标题、优化排版。

**适用场景：**
- 撰写微信公众号文章
- 生成爆款标题
- 自媒体内容创作
- 文章排版与优化

### trends-bulletin
多平台热词速报。抓取 HuggingFace、GitHub、Hacker News、Product Hunt、Reddit 和 YouTube 的热门内容，并将格式化报告发送到 Telegram。

**适用场景：**
- 日常多平台热点监控
- AI / 科技热门话题发现
- 内容创作者选题调研
- Telegram 自动推送热点简报

### browser
基于 Chrome DevTools Protocol 的浏览器自动化工具。可启动 Chrome、导航页面、执行 JavaScript、截图，并交互式选择 DOM 元素。

**适用场景：**
- 带登录态的网页抓取
- 视觉回归测试
- DOM 检查与数据提取
- 为文档留存截图

## 安装方法

### 从 GitHub 安装

首先，在 Claude Code 中将此仓库添加为插件市场：

```
/plugin marketplace add iamzhihuix/happy-claude-skills
```

然后安装所需的 skills：

```
/plugin install docx-format-replicator@happy-claude-skills
/plugin install video-processor@happy-claude-skills
/plugin install wechat-article-writer@happy-claude-skills
/plugin install browser@happy-claude-skills
/plugin install trends-bulletin@happy-claude-skills
```

### 本地开发安装

克隆仓库后，使用 `--plugin-dir` 参数：

```bash
git clone https://github.com/iamzhihuix/happy-claude-skills.git
claude --plugin-dir /path/to/happy-claude-skills
```

## 使用方法

安装后，只需在 Claude Code 里直接描述你的需求：

> "我有一个文档模板，需要生成 5 份格式完全相同的新文档"

> "下载这个 YouTube 视频并转录成文字"

> "帮我写一篇关于 AI 编程技巧的公众号文章"

> "抓取这个网页上的产品信息"

> "帮我发一下热词速报" / "Send me a trends bulletin"

Claude 会自动识别并调用相应的 skill。

## 依赖

### docx-format-replicator
- Python 3.7+
- `python-docx`

```bash
pip install python-docx
```

### video-processor
- Python 3.7+
- `yt-dlp`
- FFmpeg
- `openai-whisper`

```bash
pip install yt-dlp openai-whisper
brew install ffmpeg  # macOS
```

### trends-bulletin
- Bun（无外部依赖，使用内置 `fetch`）

```bash
# 安装 Bun（如未安装）
curl -fsSL https://bun.sh/install | bash
```

### browser
- Node.js 18+
- `puppeteer-core`
- Google Chrome

```bash
npm install --prefix skills/browser
```

## 项目结构

```
happy-claude-skills/
├── .claude-plugin/
│   └── marketplace.json         # 市场配置
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
│   │   └── scripts/             # Python 脚本
│   └── browser/
│       ├── SKILL.md             # Skill 定义
│       ├── package.json         # Node.js 依赖
│       └── scripts/             # Node.js 脚本
├── README.md
└── LICENSE
```

## 鸣谢

- **video-processor** skill 改编自 [@disler](https://github.com/disler) 的 [claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability)
- **browser** skill 基于 [Mario Zechner](https://mariozechner.at) 的文章 [What if you don't need MCP?](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/)（[GitHub](https://github.com/badlogic/browser-tools)），并基于 [Factory.ai](https://docs.factory.ai/guides/skills/browser) 的实现整理而成

## 贡献

欢迎提交 Issue 和 Pull Request。

## 许可证

MIT License
