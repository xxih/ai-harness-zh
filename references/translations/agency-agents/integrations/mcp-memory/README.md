# MCP Memory 集成

> 通过 Model Context Protocol（MCP），让任意 agent 跨会话拥有持久记忆。

## 它解决什么问题

默认情况下，The Agency 里的 agents 每次会话都会从零开始。上下文需要靠人工在 agent 和会话之间复制粘贴。接入 MCP memory server 后，会发生这些变化：

- **跨会话记忆**：agent 可以记住之前会话中的决策、交付物和上下文
- **交接连续性**：当一个 agent handoff 给另一个 agent 时，接手方可以直接回忆已完成内容，不需要人工转述
- **失败回滚**：当 QA 检查失败，或者某个架构决策被证明错误时，可以回滚到已知良好状态，而不是从头来过

## 设置

你需要一个提供 memory tools 的 MCP server：`remember`、`recall`、`rollback` 和 `search`。把它加入你的 MCP client 配置（例如 Claude Code、Cursor 等）：

```json
{
  "mcpServers": {
    "memory": {
      "command": "your-mcp-memory-server",
      "args": []
    }
  }
}
```

只要 MCP server 暴露了 `remember`、`recall`、`rollback` 和 `search` 这些 tools，就可以配合这套模式使用。具体实现可以参考 [MCP ecosystem](https://modelcontextprotocol.io)。

## 如何给任意 Agent 加上 Memory

要让现有 agent 具备持久记忆能力，可以在该 agent prompt 中增加一个 **Memory Integration** 小节，指导 agent 在关键节点使用 MCP memory tools。

### 模式

```markdown
## Memory Integration

When you start a session:
- Recall relevant context from previous sessions using your role and the current project as search terms
- Review any memories tagged with your agent name to pick up where you left off

When you make key decisions or complete deliverables:
- Remember the decision or deliverable with descriptive tags (your agent name, the project, the topic)
- Include enough context that a future session — or a different agent — can understand what was done and why

When handing off to another agent:
- Remember your deliverables tagged for the receiving agent
- Include the handoff metadata: what you completed, what's pending, and what the next agent needs to know

When something fails and you need to recover:
- Search for the last known-good state
- Use rollback to restore to that point rather than rebuilding from scratch
```

### Agent 实际会如何使用

当 prompt 中包含上述说明时，LLM 会自动在合适时机调用 MCP memory tools：

- `remember`：存储某个决策、交付物或上下文快照，并带上 tags
- `recall`：按关键词、tag 或语义相似度查找相关记忆
- `rollback`：出问题时回退到之前状态
- `search`：跨会话、跨 agents 查找特定记忆

这不需要改 agent 代码，也不需要你手写 API 调用，MCP tools 会处理这些动作。

## 示例：增强 Backend Architect

完整示例见 [backend-architect-with-memory.md](backend-architect-with-memory.md)，它展示了如何给标准 Backend Architect agent 增加一个 Memory Integration 小节。

## 示例：带记忆的工作流

完整工作流示例见 [../../examples/workflow-with-memory.md](../../examples/workflow-with-memory.md)，演示 Startup MVP 流程如何通过 memory 在 agents 之间传递上下文，而不是依赖复制粘贴。

## 建议

- **统一 tags**：每条 memory 都带上 agent 名称和 project 名称，`recall` 才稳定
- **让 LLM 判断重要性**：这些 memory 指令是指导，不是死规则。LLM 会自行判断什么时候记、记什么
- **`rollback` 是关键能力**：当 Reality Checker 判失败时，原 agent 可以直接回滚到最近检查点，而不是手工撤销
