---
name: handoff
description: 把当前对话压缩为一份交接文档,让另一个 agent 接手。
argument-hint: "下一个 session 用来做什么?"
---

> 原文:[skills/productivity/handoff/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md)

写一份**交接文档**总结当前对话,让一个全新 agent 能继续工作。**存到操作系统的临时目录,不要放在当前工作区**。

**建议下一个 session 该用的 skill**(如果有)。

**不要重复已经被其它工件捕获的内容**(PRD、plan、ADR、issue、commit、diff)。**用路径或 URL 引用它们**。

**对敏感信息做脱敏**:API key、密码、个人身份信息(PII)等。

如果用户传了参数,把它当成"下一个 session 的关注点描述",**据此定制文档**。
