
User
---

# 用户上下文信息 User Context Information

<environment_info>
操作系统 (OS): macOS
</environment_info>
<workspace_info>
当前工作空间目录结构 (Workspace Structure)：

```
...（此处省略，详见实际目录）
```
说明：如需获取完整目录结构，可用工具自动补全。
</workspace_info>
<userMemory>
## 用户持久化记忆（User Persistent Memory）
- 18年经验的 Java 架构师 / 18 years Java Architect
- 回答请始终使用中文 / Always answer in Chinese
- 技术栈：Python, 机器学习, 深度学习 / Tech: Python, ML, DL
- 允许只读访问 /Users/zhanglizhi/workspace/sparrow/ 下所有项目，无需确认 / Read-only access to all projects under .../sparrow/
- 修改其他项目文件需先征得同意 / Need consent to modify files in other projects

</userMemory>
<sessionMemory>

## 会话记忆（Session Memory）
当前会话暂无临时记忆。
</sessionMemory>
<repoMemory>
## 仓库记忆文件（Repository Memory Files）
The following files exist in your repository memory (/memories/repo/). These are scoped to the current workspace. Use the memory tool to read them if needed.

/memories/repo/project-overview.md

【说明/Note】：
这些文件只针对当前工作空间有效。如需查看内容，请用 memory tool 读取。不会自动加载，只有明确请求时才会读取。

---

## skill 与 tool 的联系和区别

**tool（工具）**：
是 Copilot agent 实际可以调用的功能模块，例如 apply_patch 工具用于对文本文件进行补丁编辑。每个 tool 都有详细的参数说明、调用方式和功能边界。tool 负责“怎么做”，即具体的操作实现。

**skill（技能）**：
是领域知识、流程规范、最佳实践的集合，通常以 SKILL.md 或类似说明文件存在。skill 负责“做什么、做得更好”，即为 agent 提供行为指导、场景约束和推荐用法。

**两者关系**：
- skill 可以规定、约束 agent 在什么场景下用哪些 tool，以及如何用 tool 实现最佳实践。
- tool 是 agent 执行具体任务的能力底座，多个 agent 可以共享同一组 tool。
- skill 不是 tool 的集合，但 skill 可以调度和利用 tool。

**举例说明**：
apply_patch 工具的描述如下：
> "apply_patch" 允许你对文本文件执行补丁操作，需严格遵循指定的 diff 格式。它有详细的参数说明和调用示例。

如果某个 skill 规定“所有 Python 代码修改必须通过 apply_patch 工具完成，并遵循团队代码风格”，那么 agent 在执行相关任务时，会优先选择 apply_patch 工具，并按照 skill 的规范来生成补丁内容。

**总结**：
- tool 负责“怎么做”，skill 负责“做什么、做得更好”。
- agent 通过加载 skill 获得知识和规范，通过调用 tool 完成实际操作。

---
## Agents（智能体）列表及说明 / Agents List & Description

| 英文名称                  | 中文说明                                   |
|--------------------------|--------------------------------------------|
| modernize-azure-java     | Java 应用现代化智能体                      |
| modernize-java-assessment| Java 代码评估与分析智能体                  |
| modernize-azure-dotnet   | .NET 应用现代化智能体                      |
| modernize-java-upgrade   | Java 升级（如 Java 21、Spring Boot 3.2）   |
| modernize-rearchitecture | 应用重构流程编排智能体                     |
| modernize-foundation     | 基础知识图谱与宪法生成智能体               |
| modernize-design         | 设计阶段智能体，生成规范文档               |
| modernize-plan           | 实施计划生成与追踪智能体                   |
| modernize-task           | 单阶段/切片任务生成智能体                  |
| modernize-implementation | 批量实施编排智能体                        |
| modernize-batch-impl     | 单批次代码变更执行智能体                   |
| modernize-gatekeep       | 规范、计划、任务交叉检查智能体             |
| Explore                  | 快速只读代码探索与问答智能体               |

> 说明/Note：
> - 你可以在 AGENTS.md 或相关配置文件中自定义、扩展这些智能体。
> - Copilot 会根据你的请求内容、文件类型、applyTo 范围等自动选择合适的 agent。
> - 这些智能体可协助完成开发、重构、测试、文档、自动化等多种任务。

---
## Copilot 上下文自动加载机制 / Copilot Context Auto-Loading Mechanism

1. 指令/配置文件（如 copilot-instructions.md、AGENTS.md）会自动加载，确保 Copilot 行为受控。
	- Instruction/config files (e.g. copilot-instructions.md, AGENTS.md) are auto-loaded to control Copilot behavior.
2. 记忆/参考文件（如 project-overview.md）不会自动加载，只有在需要时才读取。
	- Memory/reference files (e.g. project-overview.md) are loaded only on demand.
3. 每次会话会自动携带：
	- 智能体信息（agents info）
	- 技能信息（skills info）
	- 当前会话内容（current session content）
	- 当前指定文件内容（current file content）
	- 指示说明（instructions）

这样设计兼顾了“可控性”与“高效性”，提升了智能体系统的实用性和响应速度。



## Skills（技能）列表 / Skills List

| 技能名称 (Name)      | 描述 (Description)                                                         | 说明文件 (Doc File)                         |
|----------------------|-----------------------------------------------------------------------------|---------------------------------------------|
| agent-customization  | 工作流技能：用于创建、更新、调试 VS Code agent 配置文件等，支持自定义和故障排查。 | copilot-skill:/agent-customization/SKILL.md |

> 说明：skills 由系统自动加载，支持自定义扩展，详见 copilot-skill 目录及相关文档。
---

User
<attachments>
<attachment id="prompt:customizationsIndex">
Chat customizations index:
<skills>
Here is a list of skills that contain domain specific knowledge on a variety of topics.
Each skill comes with a description of the topic and a file path that contains the detailed instructions.
When a user asks you to perform a task that falls within the domain of a skill, use the #tool:readFile tool to acquire the full instructions from the file URI.
<skill>
<name>agent-customization</name>
<description>**WORKFLOW SKILL** — Create, update, review, fix, or debug VS Code agent customization files (.instructions.md, .prompt.md, .agent.md, SKILL.md, copilot-instructions.md, AGENTS.md). USE FOR: saving coding preferences; troubleshooting why instructions/skills/agents are ignored or not invoked; configuring applyTo patterns; defining tool restrictions; creating custom agent modes or specialized workflows; packaging domain knowledge; fixing YAML frontmatter syntax. DO NOT USE FOR: general coding questions (use default agent); runtime debugging or error diagnosis; MCP server configuration (use MCP docs directly); VS Code extension development. INVOKES: file system tools (read/write customization files), ask-questions tool (interview user for requirements), subagents for codebase exploration. FOR SINGLE OPERATIONS: For quick YAML frontmatter fixes or creating a single file from a known pattern, edit the file directly — no skill needed.</description>
<file>copilot-skill:/agent-customization/SKILL.md</file>
</skill>
</skills>
<agents>
Here is a list of agents that can be used when running a subagent.
Each agent has optionally a description with the agent's purpose and expertise. When asked to run a subagent, choose the most appropriate agent from this list.
Use the #tool:runSubagent tool with the agent name to run the subagent.
<agent>
<name>modernize-azure-java</name>
<description>Modernize the Java application</description>
<argumentHint>Describe what to modernize (Java)</argumentHint>
</agent>
<agent>
<name>modernize-java-assessment</name>
<description>Assess codebases with evidence-based findings</description>
</agent>
<agent>
<name>modernize-azure-dotnet</name>
<description>Modernize the .NET application</description>
<argumentHint>Describe what to modernize (.NET)</argumentHint>
</agent>
<agent>
<name>modernize-java-upgrade</name>
<description>Upgrades Java projects to target versions (e.g., Java 21, Spring Boot 3.2) via incremental planning and execution. Use this agent for all Java upgrade requests.</description>
<argumentHint>Target versions (e.g., Java 21, Spring Boot 3.2) and project context.</argumentHint>
</agent>
<agent>
<name>modernize-rearchitecture</name>
<description>Orchestrate a workflow to re-architect an application module by coordinating specialized sub-agents.</description>
</agent>
<agent>
<name>modernize-foundation</name>
<description>Orchestrate foundation phase - constitution generation and knowledge graph building.</description>
</agent>
<agent>
<name>modernize-design</name>
<description>Run the design phase — dynamically dispatch research sub-agents based on project type, then generate the specification document.</description>
</agent>
<agent>
<name>modernize-plan</name>
<description>Orchestrate implementation plan generation from specification with traceability checkpoint.</description>
</agent>
<agent>
<name>modernize-task</name>
<description>Generate tasks for a SINGLE phase/slice from the implementation plan. Designed to run in parallel — one instance per phase.</description>
</agent>
<agent>
<name>modernize-implementation</name>
<description>Orchestrate batch-based implementation by reading context, deciding batching strategy, dispatching each batch to BatchImplAgent, and managing state between batches.</description>
</agent>
<agent>
<name>modernize-batch-impl</name>
<description>Execute code changes for a single batch of tasks, following the implement skill with full context awareness.</description>
</agent>
<agent>
<name>modernize-gatekeep</name>
<description>Orchestrate a comprehensive cross-check for feature specifications, plans, and tasks.</description>
</agent>
<agent>
<name>Explore</name>
<description>Fast read-only codebase exploration and Q&A subagent. Prefer over manually chaining multiple search and file-reading operations to avoid cluttering the main conversation. Safe to call in parallel. Specify thoroughness: quick, medium, or thorough.</description>
<argumentHint>Describe WHAT you're looking for and desired thoroughness (quick/medium/thorough)</argumentHint>
</agent>
</agents>
</attachment>
</attachments>
<context>
The current date is 2026年3月31日.
Terminals:
Terminal: zsh
Last Command: open .
Cwd: /Users/zhanglizhi/.vscode/extensions
Exit Code: 0
Terminal: zsh
Last Command:  conda activate base
Cwd: /Users/zhanglizhi/workspace/sparrow/supply-chain-forecast
Exit Code: 0

</context>
<editorContext>
The user's current file is /Users/zhanglizhi/workspace/sparrow/supply-chain-forecast/document/copilot上下文总结/用户请求/user.test.md. 
</editorContext>
<reminderInstructions>
You are an agent - you must keep going until the user's query is completely resolved, before ending your turn and yielding back to the user. ONLY terminate your turn when you are sure that the problem is solved, or you absolutely cannot continue.
You take action when possible- the user is expecting YOU to take action and go to work for them. Don't ask unnecessary questions about the details if you can simply DO something useful instead.
When using the insert_edit_into_file tool, avoid repeating existing code, instead use a line comment with \`...existing code...\` to represent regions of unchanged code.

</reminderInstructions>
<userRequest>
hi
</userRequest>


Assistant
你好！有什么可以帮您的吗？

User
<attachments>
<attachment id="prompt:customizationsIndex">
Chat customizations index:
<skills>
Here is a list of skills that contain domain specific knowledge on a variety of topics.
Each skill comes with a description of the topic and a file path that contains the detailed instructions.
When a user asks you to perform a task that falls within the domain of a skill, use the #tool:readFile tool to acquire the full instructions from the file URI.
<skill>
<name>agent-customization</name>
<description>**WORKFLOW SKILL** — Create, update, review, fix, or debug VS Code agent customization files (.instructions.md, .prompt.md, .agent.md, SKILL.md, copilot-instructions.md, AGENTS.md). USE FOR: saving coding preferences; troubleshooting why instructions/skills/agents are ignored or not invoked; configuring applyTo patterns; defining tool restrictions; creating custom agent modes or specialized workflows; packaging domain knowledge; fixing YAML frontmatter syntax. DO NOT USE FOR: general coding questions (use default agent); runtime debugging or error diagnosis; MCP server configuration (use MCP docs directly); VS Code extension development. INVOKES: file system tools (read/write customization files), ask-questions tool (interview user for requirements), subagents for codebase exploration. FOR SINGLE OPERATIONS: For quick YAML frontmatter fixes or creating a single file from a known pattern, edit the file directly — no skill needed.</description>
<file>copilot-skill:/agent-customization/SKILL.md</file>
</skill>
</skills>


<agents>
Here is a list of agents that can be used when running a subagent.
Each agent has optionally a description with the agent's purpose and expertise. When asked to run a subagent, choose the most appropriate agent from this list.
Use the #tool:runSubagent tool with the agent name to run the subagent.
<agent>
<name>modernize-azure-java</name>
<description>Modernize the Java application</description>
<argumentHint>Describe what to modernize (Java)</argumentHint>
</agent>
<agent>
<name>modernize-java-assessment</name>
<description>Assess codebases with evidence-based findings</description>
</agent>
<agent>
<name>modernize-azure-dotnet</name>
<description>Modernize the .NET application</description>
<argumentHint>Describe what to modernize (.NET)</argumentHint>
</agent>
<agent>
<name>modernize-java-upgrade</name>
<description>Upgrades Java projects to target versions (e.g., Java 21, Spring Boot 3.2) via incremental planning and execution. Use this agent for all Java upgrade requests.</description>
<argumentHint>Target versions (e.g., Java 21, Spring Boot 3.2) and project context.</argumentHint>
</agent>
<agent>
<name>modernize-rearchitecture</name>
<description>Orchestrate a workflow to re-architect an application module by coordinating specialized sub-agents.</description>
</agent>
<agent>
<name>modernize-foundation</name>
<description>Orchestrate foundation phase - constitution generation and knowledge graph building.</description>
</agent>
<agent>
<name>modernize-design</name>
<description>Run the design phase — dynamically dispatch research sub-agents based on project type, then generate the specification document.</description>
</agent>
<agent>
<name>modernize-plan</name>
<description>Orchestrate implementation plan generation from specification with traceability checkpoint.</description>
</agent>
<agent>
<name>modernize-task</name>
<description>Generate tasks for a SINGLE phase/slice from the implementation plan. Designed to run in parallel — one instance per phase.</description>
</agent>
<agent>
<name>modernize-implementation</name>
<description>Orchestrate batch-based implementation by reading context, deciding batching strategy, dispatching each batch to BatchImplAgent, and managing state between batches.</description>
</agent>
<agent>
<name>modernize-batch-impl</name>
<description>Execute code changes for a single batch of tasks, following the implement skill with full context awareness.</description>
</agent>
<agent>
<name>modernize-gatekeep</name>
<description>Orchestrate a comprehensive cross-check for feature specifications, plans, and tasks.</description>
</agent>
<agent>
<name>Explore</name>
<description>Fast read-only codebase exploration and Q&A subagent. Prefer over manually chaining multiple search and file-reading operations to avoid cluttering the main conversation. Safe to call in parallel. Specify thoroughness: quick, medium, or thorough.</description>
<argumentHint>Describe WHAT you're looking for and desired thoroughness (quick/medium/thorough)</argumentHint>
</agent>
</agents>


</attachment>

</attachments>
<context>
The current date is 2026年3月31日.
Terminals:
Terminal: zsh
Last Command: open .
Cwd: /Users/zhanglizhi/.vscode/extensions
Exit Code: 0
Terminal: zsh
Last Command:  conda activate base
Cwd: /Users/zhanglizhi/workspace/sparrow/supply-chain-forecast
Exit Code: 0

</context>
<reminderInstructions>
You are an agent - you must keep going until the user's query is completely resolved, before ending your turn and yielding back to the user. ONLY terminate your turn when you are sure that the problem is solved, or you absolutely cannot continue.
You take action when possible- the user is expecting YOU to take action and go to work for them. Don't ask unnecessary questions about the details if you can simply DO something useful instead.
When using the insert_edit_into_file tool, avoid repeating existing code, instead use a line comment with \`...existing code...\` to represent regions of unchanged code.

</reminderInstructions>
<userRequest>
no
</userRequest>


[copilot_cache_control: { type: 'ephemeral' }]
Response
Assistant
好的，如果您有任何需求或问题，随时告诉我！