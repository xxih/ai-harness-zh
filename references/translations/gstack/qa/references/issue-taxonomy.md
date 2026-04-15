# QA 问题分类法

## 严重级别

| Severity | 定义 | 例子 |
|----------|------|------|
| **critical** | 阻断核心工作流、造成数据丢失，或直接让应用崩溃 | 提交表单后跳错误页、结账流断掉、数据在无确认下被删除 |
| **high** | 主要功能损坏或不可用，且没有可行绕路 | 搜索结果错误、文件上传静默失败、认证跳转死循环 |
| **medium** | 功能能用，但问题明显，且存在 workaround | 页面加载过慢（>5s）、表单缺校验但还能提交、仅移动端布局损坏 |
| **low** | 轻微外观或打磨问题 | 页脚 typo、1px 对齐偏差、hover state 不一致 |

## 分类

### 1. Visual / UI
- 布局损坏（元素重叠、文字裁切、横向滚动条）
- 图片损坏或缺失
- `z-index` 错误（元素被盖在后面）
- 字体 / 配色不一致
- 动画异常（卡顿、过渡没跑完）
- 对齐问题（不在网格上、间距不均）
- 深色模式 / theme 问题

### 2. Functional
- 链接失效（404、跳错目标）
- 死按钮（点击无反应）
- 表单校验有缺失、错误或可绕过
- 重定向错误
- 状态不持久（刷新或后退后数据丢失）
- Race condition（双提交、读到 stale data）
- 搜索返回错误结果或没有结果

### 3. UX
- 导航令人困惑（没有 breadcrumbs、走进死路）
- 缺 loading indicator，用户不知道系统是否在工作
- 交互缓慢（>500ms）但没有反馈
- 错误信息含糊，例如只有 “Something went wrong”
- 破坏性动作前缺确认
- 不同页面的交互模式不一致
- 死胡同场景（没有返回路径，也没有下一步）

### 4. Content
- 拼写或语法错误
- 文案过时或错误
- 残留 placeholder / lorem ipsum
- 文本被截断，却没有省略或 “more”
- 按钮或表单字段标签错误
- 空状态缺失或没有信息量

### 5. Performance
- 页面加载慢（>3 秒）
- 滚动卡顿（掉帧）
- 布局抖动（加载后内容跳动）
- 网络请求过多（单页 >50 个）
- 图片过大且未优化
- 阻塞性 JavaScript 让页面加载期无响应

### 6. Console / Errors
- JavaScript exception（未捕获错误）
- 网络请求失败（4xx、5xx）
- 弃用警告（预示后续 breakage）
- CORS 错误
- Mixed content 警告（HTTPS 页面里加载 HTTP 资源）
- CSP 违规

### 7. Accessibility
- 图片缺 alt text
- 表单输入缺 label
- 键盘导航损坏（tab 不到目标元素）
- Focus trap（modal / dropdown 里出不来）
- ARIA attributes 缺失或错误
- 颜色对比度不足
- 屏幕阅读器不可达

## 单页探索检查表

在一次 QA session 中，对每个访问过的页面都做下面检查：

1. **视觉扫一遍**：用 annotated screenshot（`snapshot -i -a -o`）检查布局、坏图、对齐。
2. **交互元素**：把每个按钮、链接和控件都点一遍，它是否真的做了它声称会做的事？
3. **表单**：填写并提交。测试空提交、非法输入和边界情况（长文本、特殊字符）。
4. **导航**：检查所有进出路径。包括 breadcrumbs、返回按钮、deep links、移动端菜单。
5. **状态**：检查空状态、加载状态、错误状态，以及 full / overflow 状态。
6. **Console**：交互后运行 `console --errors`，看是否新出现 JS errors 或 failed requests。
7. **响应式**：需要时检查 mobile 和 tablet 视口。
8. **认证边界**：登出时会发生什么？不同角色用户看到的行为是否一致？
