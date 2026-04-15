# Design System — gstack

## 产品语境
- **这是什么：** gstack 的社区网站，一个把 Claude Code 变成“虚拟工程团队”的 CLI 工具对应的官网与社区面板
- **面向谁：** 正在了解 gstack 的开发者，以及现有社区成员
- **所属空间 / 行业：** Developer tools（同类参考：Linear、Raycast、Warp、Zed）
- **项目类型：** 社区 dashboard + 营销站点

## 审美方向
- **方向：** Industrial / Utilitarian，功能优先、信息密度高、以 monospace 作为性格字体
- **装饰程度：** 有意识地克制，在表面上加入细微 noise / grain 纹理来增加材质感
- **氛围：** 一个认真做工的人打造的严肃工具，带一点温度，不要冰冷。CLI 出身本身就是品牌。
- **参考站点：** `formulae.brew.sh`（竞品，但我们的站点是 live 且可交互的）、Linear（dark + restrained）、Warp（warm accents）

## Typography
- **Display / Hero：** Satoshi（Black 900 / Bold 700），几何感强但带温度，字形有辨识度（尤其小写 `a` 和 `g`）。不要 Inter，也不要 Geist。通过 Fontshare CDN 加载。
- **Body：** DM Sans（Regular 400 / Medium 500 / Semibold 600），干净、易读，比纯几何 display 字体更友好。通过 Google Fonts 加载。
- **UI / Labels：** DM Sans（与正文一致）
- **Data / Tables：** JetBrains Mono（Regular 400 / Medium 500），这是性格字体。支持 `tabular-nums`。Monospace 应该明显可见，不要只藏在代码块里。通过 Google Fonts 加载。
- **Code：** JetBrains Mono
- **加载方式：** DM Sans + JetBrains Mono 走 Google Fonts，Satoshi 走 Fontshare，统一使用 `display=swap`
- **字号体系：**
  - Hero：72px / `clamp(40px, 6vw, 72px)`
  - H1：48px
  - H2：32px
  - H3：24px
  - H4：18px
  - Body：16px
  - Small：14px
  - Caption：13px
  - Micro：12px
  - Nano：11px（JetBrains Mono labels）

## Color
- **策略：** 克制。amber accent 要少而准。把颜色给 dashboard 数据，chrome 本身保持中性。
- **Primary（dark mode）：** amber-500 `#F59E0B`，有温度、有活力，读起来像“terminal cursor”
- **Primary（light mode）：** amber-600 `#D97706`，在白底上对比更稳
- **Primary text accent（dark mode）：** amber-400 `#FBBF24`
- **Primary text accent（light mode）：** amber-700 `#B45309`
- **Neutrals：** 偏冷的 zinc 灰
  - zinc-50：`#FAFAFA`（最浅）
  - zinc-400：`#A1A1AA`
  - zinc-600：`#52525B`
  - zinc-800：`#27272A`
  - Surface（dark）：`#141414`
  - Base（dark）：`#0C0C0C`
  - Surface（light）：`#FFFFFF`
  - Base（light）：`#FAFAF9`
- **Semantic：** success `#22C55E`，warning `#F59E0B`，error `#EF4444`，info `#3B82F6`
- **Dark mode：** 默认模式。近黑 base（`#0C0C0C`），surface cards 用 `#141414`，边框 `#262626`
- **Light mode：** 温暖 stone base（`#FAFAF9`），白色 surface cards，stone 边框（`#E7E5E4`）。amber accent 切到 amber-600 以保证对比度。

## Spacing
- **基础单位：** 4px
- **密度：** 舒适，不要挤成 Bloomberg Terminal，也不要松到像纯营销站
- **刻度：** `2xs(2px) xs(4px) sm(8px) md(16px) lg(24px) xl(32px) 2xl(48px) 3xl(64px)`

## Layout
- **方法：** dashboard 走 grid discipline，landing page 走 editorial hero
- **Grid：** `lg+` 使用 12 列，mobile 使用 1 列
- **最大内容宽度：** 1200px（6xl）
- **Border radius：** `sm:4px`、`md:8px`、`lg:12px`、`full:9999px`
  - Cards / panels：`lg (12px)`
  - Buttons / inputs：`md (8px)`
  - Badges / pills：`full (9999px)`
  - Skill bars：`sm (4px)`

## Motion
- **策略：** 极简且服务理解。只有能帮助理解的过渡才值得存在。dashboard 的 live feed 本身就是 motion。
- **缓动：** enter（`ease-out / cubic-bezier(0.16,1,0.3,1)`）、exit（`ease-in`）、move（`ease-in-out`）
- **时长：** micro（50-100ms）、short（150ms）、medium（250ms）、long（400ms）
- **可动画元素：** live feed dot pulse（2s infinite）、skill bar fill（600ms ease-out）、hover states（150ms）

## Grain Texture
给整页加一层很轻的 noise overlay，增强材质感：
- Dark mode：opacity `0.03`
- Light mode：opacity `0.02`
- 用 SVG `feTurbulence` filter 作为 `body::after` 的 CSS background-image
- `pointer-events: none`、`position: fixed`、`z-index: 9999`

## 决策日志
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-21 | 初版 design system | 由 `/design-consultation` 产出。工业风审美、温暖 amber accent、Satoshi + DM Sans + JetBrains Mono。 |
| 2026-03-21 | Light mode 使用 amber-600 | amber-500 在白底上太亮、太发灰；amber-700 又太偏棕。amber-600 刚好。 |
| 2026-03-21 | 引入 grain texture | 给偏平的暗色表面增加材质感，避免落进“通用 SaaS 模板”的同质化。 |
