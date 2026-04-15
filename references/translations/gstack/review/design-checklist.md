# Design Review Checklist（Lite）

> **`DESIGN_METHODOLOGY` 的子集**。如果要在这里增删条目，也要同步更新 `scripts/gen-skill-docs.ts` 里的 `generateDesignMethodology()`，反之亦然。

## 使用说明

这个 checklist 只针对 **diff 中涉及的前端源码**，不是针对实际渲染结果。要把改动过的前端文件完整读一遍，而不是只看 diff hunk，然后再标记 anti-pattern。

**触发条件：** 只有 diff 碰到 frontend files 时才运行。用 `gstack-diff-scope` 检测：

```bash
source <(~/.claude/skills/gstack/bin/gstack-diff-scope <base> 2>/dev/null)
```

如果 `SCOPE_FRONTEND=false`，就静默跳过整段 design review。

**`DESIGN.md` 校准：** 如果 repo 根目录存在 `DESIGN.md` 或 `design-system.md`，先读它。所有 findings 都要以项目自己声明的 design system 为准。凡是被 `DESIGN.md` 明确认可的模式，都不要报。如果没有 `DESIGN.md`，再用通用设计原则。

---

## 置信度分层

每一项都会带一个检测置信度标签：

- **[HIGH]**：能通过 grep / pattern match 稳定识别，基本是确定性问题
- **[MEDIUM]**：依赖模式聚合或启发式，仍可作为 finding，但会有一些噪音
- **[LOW]**：需要理解视觉意图，应该表述成 “Possible issue — verify visually or run /design-review.”

---

## 分类

**AUTO-FIX**（仅限机械式 CSS 修复，且必须是 HIGH confidence、无需设计判断）：
- `outline: none` 但没有替代焦点样式，补 `outline: revert` 或 `&:focus-visible { outline: 2px solid currentColor; }`
- 新增 CSS 里出现 `!important`，删除它并修正 specificity
- 正文文字 `font-size < 16px`，提升到 16px

**ASK**（其余全部，都需要设计判断）：
- 所有 AI slop findings
- 字体结构问题
- 间距与布局选择
- 交互状态缺失
- 违反 `DESIGN.md` 的实现

**LOW confidence 项**：
- 用 “Possible: [description]. Verify visually or run /design-review.” 呈现
- 永远不要 AUTO-FIX

---

## 输出格式

```text
Design Review: N issues (X auto-fixable, Y need input, Z possible)

**AUTO-FIXED:**
- [file:line] 问题 -> 已应用修复

**NEEDS INPUT:**
- [file:line] 问题描述
  Recommended fix: 建议修复方案

**POSSIBLE (verify visually):**
- [file:line] 可能有问题，请用 /design-review 进一步验证
```

如果没发现问题：`Design Review: No issues found.`

如果没有改动 frontend files：静默跳过，不输出。

---

## 类别

### 1. AI Slop Detection（6 项，最高优先级）

这些是 AI 生成 UI 最典型的痕迹，任何像样工作室里的设计师都不会把这种东西直接发到线上。

- **[MEDIUM]** 紫 / 靛 / 蓝紫渐变背景。关注 `linear-gradient` 是否落在 `#6366f1`–`#8b5cf6` 一带，或 CSS custom properties 是否解析到这类紫色。
- **[LOW]** 三栏 feature grid：每列都是“彩色圆形图标 + 粗体标题 + 两行描述”，并且三列对称重复。可从 grid / flex 容器中寻找恰好 3 个孩子，每个都含圆形元素 + heading + paragraph。
- **[LOW]** 把图标塞进彩色圆圈当 section decoration。典型特征是 `border-radius: 50%` + 背景色，仅作为装饰容器。
- **[HIGH]** 什么都居中：所有 headings、descriptions、cards 都 `text-align: center`。可以按密度 grep，如果超过 60% 的 text container 都居中，就报。
- **[MEDIUM]** 全站统一使用大而圆的 border-radius：cards、buttons、inputs、containers 都用同一个 16px+ 半径。聚合 `border-radius` 值，如果超过 80% 都是同一个且值 >= 16px，就报。
- **[MEDIUM]** 通用 hero 文案：如 “Welcome to [X]”、“Unlock the power of...” 、“Your all-in-one solution for...” 、“Revolutionize your...” 、“Streamline your workflow”。可以对 HTML / JSX 文案做模式搜索。

### 2. Typography（4 项）

- **[HIGH]** 正文字号 `< 16px`。查 `body`、`p`、`.text` 或 base styles 上的 `font-size` 声明，凡是小于 16px（或在 16px base 下小于 `1rem`）都要报。
- **[HIGH]** diff 中引入了超过 3 种 font families。统计所有 `font-family` 声明，若改动文件里出现了超过 3 种唯一字体，就报。
- **[HIGH]** heading hierarchy 跳级：同一文件 / 组件里，`h1` 后直接接 `h3`，中间没有 `h2`
- **[HIGH]** 黑名单字体：Papyrus、Comic Sans、Lobster、Impact、Jokerman。对 `font-family` 做 grep。

### 3. Spacing & Layout（4 项）

- **[MEDIUM]** 存在不落在 4px / 8px scale 上的任意间距值，且 `DESIGN.md` 已明确规定 spacing scale。检查 `margin`、`padding`、`gap` 是否偏离该刻度。
- **[MEDIUM]** 固定宽度但没有响应式兜底：容器写了 `width: NNNpx`，却没有 `max-width` 或 `@media` breakpoints，手机上容易横向滚动。
- **[MEDIUM]** 文本容器缺少 `max-width`，导致段落一行超过 75 个字符。检查正文或 paragraph wrapper 是否设置了 `max-width`。
- **[HIGH]** 新增 CSS 里出现 `!important`。几乎总是 specificity 逃生口，应该用正确结构解决。

### 4. Interaction States（3 项）

- **[MEDIUM]** 新增的 buttons、links、inputs 没有 hover / focus states。查看对应样式是否定义了 `:hover` 与 `:focus` 或 `:focus-visible`
- **[HIGH]** 使用 `outline: none` 或 `outline: 0`，却没有替代的 focus indicator，会直接破坏键盘可访问性
- **[LOW]** 交互目标小于 44px。需要结合 `min-height` / `min-width` / `padding` 才能估算，有一定不确定性

### 5. `DESIGN.md` 违规项（3 项，条件启用）

仅当存在 `DESIGN.md` 或 `design-system.md` 时检查：

- **[MEDIUM]** 使用了不在 palette 中的颜色。把改动里的 CSS 颜色与 `DESIGN.md` 里定义的 palette 对照。
- **[MEDIUM]** 使用了不在 typography section 里的字体。把 `font-family` 与 `DESIGN.md` 字体列表对照。
- **[MEDIUM]** 使用了超出 spacing scale 的间距值。把 `margin` / `padding` / `gap` 与 `DESIGN.md` 标定的尺度对照。

---

## Suppressions

不要报：
- 在 `DESIGN.md` 中已经明确写成 intentional choice 的模式
- 第三方 / vendor CSS 文件（`node_modules`、vendor 目录）
- CSS reset 或 normalize stylesheet
- 测试 fixture 文件
- 生成产物 / 压缩后的 CSS
