---
name: video-processor
description: 从 YouTube 和其他平台下载并处理视频。支持视频下载、音频提取、格式转换（mp4、webm）以及 Whisper 转录。当用户提到 YouTube 下载、视频转换、音频提取、转录、mp4、webm、ffmpeg、yt-dlp 或 whisper transcription 时使用。
metadata:
  author: iamzhihuix
  version: "1.0.0"
---

# Video Processor

## Instructions

这个 skill 提供完整的视频处理能力，包括 YouTube 视频下载、音频提取、格式转换，以及基于 yt-dlp、FFmpeg 和 OpenAI Whisper 模型的音频转录。

### Prerequisites

**必需工具**（必须安装在当前环境中）：

- **yt-dlp**：支持 YouTube 和上千个站点的视频下载器
  ```bash
  # 通过 pip 安装
  pip install -U yt-dlp

  # 验证安装
  yt-dlp --version
  ```

- **FFmpeg**：用于视频 / 音频处理的多媒体框架
  ```bash
  # macOS
  brew install ffmpeg

  # Ubuntu/Debian
  apt-get install ffmpeg

  # 验证安装
  ffmpeg -version
  ```

- **OpenAI Whisper**：语音转文字模型
  ```bash
  # 通过 pip 安装
  pip install -U openai-whisper

  # 验证安装
  whisper --help
  ```

**Python 包**（已通过 PEP 723 内嵌在脚本中）：

- `click`（CLI 框架）
- `ffmpeg-python`（FFmpeg 的 Python 封装）
- `yt-dlp`（视频下载器）

### Workflow

所有视频处理任务都使用 `scripts/video_processor.py`。该脚本提供以下命令：

#### 0. **从 YouTube 或其他平台下载视频**（NEW!）

从 YouTube 及其他成千上万个受支持的网站下载视频：

```bash
# 下载视频
uv run .claude/skills/video-processor/scripts/video_processor.py download "https://youtube.com/watch?v=..." output.mp4

# 仅下载音频（输出为 MP3）
uv run .claude/skills/video-processor/scripts/video_processor.py download "https://youtube.com/watch?v=..." --audio-only

# 只查看视频信息，不下载
uv run .claude/skills/video-processor/scripts/video_processor.py download "https://youtube.com/watch?v=..." --info

# 下载并嵌入字幕
uv run .claude/skills/video-processor/scripts/video_processor.py download "https://youtube.com/watch?v=..." output.mp4 --subtitle
```

可选项：

- `--audio-only`：仅下载音频（提取为 MP3）
- `--subtitle`：下载并嵌入字幕（支持 `en`、`zh-Hans`、`zh-Hant`）
- `--info`：仅显示视频信息，不下载
- `--format`：指定视频格式偏好（默认最佳画质）

#### 1. **从视频中提取音频**

从视频文件中提取音轨：

```bash
uv run .claude/skills/video-processor/scripts/video_processor.py extract-audio input.mp4 output.wav
```

可选项：

- `--format`：输出音频格式（默认 `wav`），支持 `wav`、`mp3`、`aac`、`flac`
- 输出结果可直接用于转录，也可单独作为音频文件使用

#### 2. **将视频转换为 MP4**

把任意视频文件转换为 MP4：

```bash
uv run .claude/skills/video-processor/scripts/video_processor.py to-mp4 input.avi output.mp4
```

可选项：

- `--codec`：视频编码器（默认 `libx264`），常见选项有 `libx264`、`libx265`、`h264`
- `--preset`：编码速度 / 质量预设（默认 `medium`），可选 `ultrafast`、`fast`、`medium`、`slow`、`veryslow`

#### 3. **将视频转换为 WebM**

把任意视频文件转换为适合网页播放的 WebM：

```bash
uv run .claude/skills/video-processor/scripts/video_processor.py to-webm input.mp4 output.webm
```

可选项：

- `--codec`：视频编码器（默认 `libvpx-vp9`），可选 `libvpx`、`libvpx-vp9`
- WebM 更适合网页播放与流式传输

#### 4. **使用 Whisper 转录音频**

使用 OpenAI Whisper 把音频或视频文件转成文本：

```bash
# 转录视频文件（会自动提取音频）
uv run .claude/skills/video-processor/scripts/video_processor.py transcribe input.mp4 transcript.txt

# 直接转录音频文件
uv run .claude/skills/video-processor/scripts/video_processor.py transcribe audio.wav transcript.txt
```

可选项：

- `--model`：Whisper 模型大小（默认 `base`），可选：
  - `tiny`：最快，准确率最低（约 1GB RAM）
  - `base`：速度快，准确率不错（约 1GB RAM）**[默认]**
  - `small`：速度与准确率平衡（约 2GB RAM）
  - `medium`：较高准确率（约 5GB RAM）
  - `large`：准确率最高，速度最慢（约 10GB RAM）
- `--language`：语言代码（默认自动检测），例如 `en`、`es`、`fr`、`de`、`zh`
- `--format`：输出格式（默认 `txt`），可选 `txt`、`srt`、`vtt`、`json`

**转录流程：**

1. 如果输入是视频，FFmpeg 会先把音频提取到临时 WAV 文件
2. Whisper 处理该音频文件
3. 按请求的格式保存转录结果
4. 自动清理临时文件

#### 5. **组合工作流示例**

对一个视频做端到端处理：

```bash
# 1. 提取音频用于分析
uv run .claude/skills/video-processor/scripts/video_processor.py extract-audio lecture.mp4 lecture.wav

# 2. 转录成 SRT 字幕
uv run .claude/skills/video-processor/scripts/video_processor.py transcribe lecture.mp4 lecture.srt --format srt --model small

# 3. 转成适合网页播放的格式
uv run .claude/skills/video-processor/scripts/video_processor.py to-webm lecture.mp4 lecture.webm
```

### Key Technical Details

**FFmpeg 与 Whisper 的集成方式：**

- FFmpeg 本身不负责语音转录，它负责为外部转录工具准备音频
- 典型流程是：提取音频（FFmpeg）→ 转录（Whisper）→ 视情况重新与视频整合
- 高级场景下，FFmpeg 也可以把音频直接 pipe 给 Whisper 做实时处理

**适合转录的音频格式：**

- Whisper 对 WAV 和 MP3 的处理效果最好
- 最佳采样率为 16kHz（脚本会自动完成转换）
- 脚本会按适合 Whisper 的参数提取音频

**输出格式：**

- **txt**：纯文本转录
- **srt**：SubRip 字幕格式（含时间戳）
- **vtt**：WebVTT 字幕格式（网页标准）
- **json**：带词级时间戳的详细 JSON

### Error Handling

脚本包含较完整的错误处理：

- 校验输入文件是否存在
- 检查 FFmpeg 和 Whisper 是否已安装
- 对缺失依赖给出清晰错误信息
- 出错时也会处理临时文件清理

### Performance Tips

- 快速草稿优先使用 `tiny` 或 `base`
- 正式转录优先使用 `small` 或 `medium`
- 只有在确实需要最高准确率时才使用 `large`
- 长视频建议先提取音频，再分段转录
- 使用 VP9 转为 WebM 会更慢，但产出的文件更小

## Examples

### Example 1: 快速把视频转成 MP4

用户请求：

```
I have an AVI file from my old camera. Can you convert it to MP4?
```

你应该：

1. 使用默认参数执行 `to-mp4`：
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py to-mp4 old_video.avi output.mp4
   ```
2. 确认转换成功完成
3. 告知用户输出文件位置

### Example 2: 提取音频并转录

用户请求：

```
I recorded a lecture video and need a transcript. Can you extract the audio and transcribe it?
```

你应该：

1. 先提取音频：
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py extract-audio lecture.mp4 lecture.wav
   ```
2. 再用 `base` 模型转录（速度与准确率平衡较好）：
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py transcribe lecture.mp4 transcript.txt --model base
   ```
3. 将 `transcript.txt` 提供给用户

### Example 3: 生成适合网页的视频和字幕

用户请求：

```
I need to put this video on my website with subtitles. Can you help?
```

你应该：

1. 转为更适合网页的 WebM：
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py to-webm presentation.mp4 presentation.webm
   ```
2. 生成 SRT 字幕文件：
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py transcribe presentation.mp4 subtitles.srt --format srt --model small
   ```
3. 告诉用户现在已经有：
   - `presentation.webm`（适合网页播放的视频）
   - `subtitles.srt`（可嵌入网页的视频字幕）

### Example 4: 指定语言并提高转录质量

用户请求：

```
I have a Spanish interview video that needs an accurate transcript for publication.
```

你应该：

1. 指定语言并使用更大的模型，以获得更高准确率：
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py transcribe interview.mp4 transcript.txt --model medium --language es
   ```
2. 如果需要审校，也可以同时生成 SRT：
   ```bash
   uv run .claude/skills/video-processor/scripts/video_processor.py transcribe interview.mp4 transcript.srt --format srt --model medium --language es
   ```
