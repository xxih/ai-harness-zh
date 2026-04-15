# Maintainability Specialist Review Checklist

适用范围：始终启用（每次 review 都跑）
输出格式：每行一个 JSON finding。Schema：
`{"severity":"INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"maintainability","summary":"...","fix":"...","fingerprint":"path:line:maintainability","specialist":"maintainability"}`

如果没有发现：只输出 `NO FINDINGS`，不要输出别的内容。

---

## 审查类别

### Dead Code 与未使用导入
- 改动文件里变量被赋值但从未读取
- 新定义的函数 / 方法从未被调用，要用 `Grep` 跨仓检查
- 变更后 imports / requires 已不再使用
- 注释掉的代码块仍留在文件里

### Magic Numbers 与字符串耦合
- 在业务逻辑里直接写裸数字（阈值、limit、重试次数），应提成命名常量
- 错误消息字符串被其他地方拿去当过滤条件或条件判断
- URL、端口、hostname 被硬编码，本应进配置
- 多文件重复出现同样的 literal 值

### 过期注释与 Docstrings
- 注释仍描述旧行为，但代码已在本次 diff 中变化
- `TODO` / `FIXME` 注释指向的工作其实已完成
- Docstring 参数列表与当前函数签名不一致
- 注释里的 ASCII 图与真实代码流不再相符

### DRY 违规
- diff 内部出现多段高度相似的 3 行以上代码
- 明显 copy-paste，本应提共享 helper
- 测试文件里配置或 setup 逻辑重复
- 重复条件链更适合收成 lookup table 或 map

### 条件分支副作用不对称
- 代码根据条件分支，但某一支漏掉了应有副作用
- 日志声称动作已执行，但真实动作被条件跳过
- 状态流转里一条分支更新了相关记录，另一条没更新
- 事件只在 happy path 发出，错误或边界路径没有对应发射

### 模块边界违规
- 直接探测别的模块内部实现，访问约定上的 private 方法
- controller / view 里直接打数据库，不走 service / model
- 组件间高度耦合，本应通过接口交互
