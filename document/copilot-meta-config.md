## copilot-skill: 路径与 VS Code 扩展目录说明

以 copilot-skill: 开头的路径，实际对应本地 VS Code 扩展插件的安装目录。例如：

	copilot-skill:/agent-customization/SKILL.md

对应本地绝对路径：

	~/.vscode/extensions/github.copilot-skill/agent-customization/SKILL.md

其中：
- ~/.vscode/extensions/ 是 VS Code 扩展的本地存放目录（不同操作系统可能略有差异）
- github.copilot-skill/ 是 Copilot Skill 扩展的文件夹
- agent-customization/SKILL.md 是具体的技能说明配置文件

你可以在本地 VS Code 扩展目录下找到这些文件并进行维护。
# Copilot Agent 元配置与技能说明

本项目采用 VS Code Copilot Agents 智能协作体系，以下为与 Copilot 相关的元配置及技能说明，便于团队理解和扩展。

| 配置项         | 配置文件位置                                   | 备注说明                         | 作用及说明                                                                 |
|----------------|----------------------------------------------|----------------------------------|----------------------------------------------------------------------------|
| 用户信息       | memories/user-profile.md                      | 只读权限、技术栈、语言偏好       | Copilot 回答风格、权限判断、定制化体验。Copilot 本身会维护一个全局用户信息配置，项目中的配置（如 memories/user-profile.md）会覆盖全局配置；如项目未配置，则自动回退使用全局配置。 |
| Copilot 指令   | .github/copilot-instructions.md               | 项目环境、依赖、结构、工具链     | 约束 Copilot 行为，统一项目工程化规范与自动化建议。仅用于 Copilot 与用户的交互，不会参与 LLM 的上下文构建，与 user profile 不同。 |
| Agents 配置    | AGENTS.md                                     | dev-engineer-agent/qa-tester-agent | 定义 Copilot 智能 agent 的职责、适用范围、技能、限制，自动分派开发/测试任务 |
| Agent skills   | AGENTS.md 的 skills 字段                      | 结构化声明 agent 能力            | 列举 agent 可自动完成的任务类型（如 code-generation、pytest-case-generation）|
| 技能说明文档   | copilot-skill:/agent-customization/SKILL.md   | agent-customization skill         | 详细解释 agent 技能体系、适用场景、调用方式、约束、扩展方式等。该文件为实际的技能说明配置文件，供团队查阅和扩展。 |
| 说明文档       | README.md                                     | Copilot 相关说明（如有）         | 项目快速入门、Copilot 使用说明、团队协作规范                                |

## 说明
- skills 字段是 agent 的“功能点清单”，直接影响 agent 能做什么。
- 技能说明文档是“元信息/帮助文档”，用于解释、指导和规范 agent 的使用和扩展。
- 两者互补，共同构成 agent 的完整能力体系和使用说明。

如需扩展 agent 能力或自定义团队协作规范，请参考上述配置文件并结合实际需求进行调整。