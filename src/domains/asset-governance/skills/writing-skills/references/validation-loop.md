# Writing Skills Validation Loop

## 1. RED：先写 baseline

先定义一个 pressure scenario，目标是逼出“没有这个 skill 时最容易犯的错”。

模板：

```text
场景：
- 当前要创建 / 重写的 skill 是什么
- 没有 skill 时，agent 最可能漏什么、误判什么、偷什么懒
- 本轮只观察，不提前给答案

预期失败：
- description 偷跑 workflow
- 把项目私规错写成通用 skill
- 不做 references 拆分，正文越写越长
- 没有 baseline 就直接宣布 skill ready
```

记录要求：

- 写下 agent 实际失败点
- 写下它的合理化措辞，而不只是结论
- 失败点越具体，后续 skill 越容易写得最小

## 2. GREEN：只写修正 baseline 的最小 skill

- 不要试图一次写出“终极版”
- 只补那些已经在 baseline 里真实出现的失败
- 如果某个规则可以放进 `references/`，就不要把主文档写成百科全书

## 3. REFACTOR：补漏洞，不补虚荣细节

用近邻场景继续试探：

- 只改了 skill 名称，但边界没变
- 同一问题换一种说法
- 混入平台特定诉求，观察 skill 是否越界
- 用户只要求“顺手整理一下”，观察 agent 是否错误升级为正式 skill

发现新漏洞时：

1. 判断是正文该补，还是该下沉到 `references/`
2. 回写 skill
3. 用原 baseline + 新场景一起复验

## 4. 无独立 agent 时的降级做法

如果当前环境没有独立 agent / subagent：

1. 仍然要先写 baseline 场景
2. 显式列出“没有 skill 时最可能的错误”
3. 写完 skill 后，按同一场景逐条自查
4. 把未验证项标成风险，不要伪装成已经验证通过

## 5. ready 判断

只有同时满足以下条件，才算 ready：

- baseline 已经被显式定义
- skill 已覆盖 baseline 暴露的主要失败
- 至少完成一轮复验
- 若仓库维护 target 快照，source 与 target 已同步
- 没有悬空的关键待确认项
