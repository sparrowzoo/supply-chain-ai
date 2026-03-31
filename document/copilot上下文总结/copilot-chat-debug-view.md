# VS Code Copilot Chat Debug View 权威说明

## 1. 入口与用途
- 通过 VS Code 命令面板（Ctrl+Shift+P 或 Cmd+Shift+P），输入并运行 `Developer: Show Chat Debug View`。
- 该视图用于开发者和高级用户“白盒化”分析 Copilot Chat 与 LLM（大模型）之间的真实交互过程。

## 2. 能看到的内容
- 实际发送给 LLM 的 prompt（包括系统提示、用户输入、历史对话、代码片段等）。
- Copilot 插件如何拼接和组织上下文（如哪些文件、哪些对话、哪些配置被纳入 prompt）。
- LLM 返回的原始响应内容。
- Copilot 插件与 LLM 之间的底层通信细节（如请求体、响应体、token 统计等）。

## 3. 价值与应用场景
- 你可以看到 Copilot/LLM 实际“吃进去”的全部上下文，而不是仅仅看到你写的配置或你输入的对话。
- 便于分析为什么 LLM 有时答非所问、遗漏上下文、或 prompt 被截断。
- 适合调试 prompt 设计、上下文拼接、插件行为等高级场景。
- 方便团队做 prompt 优化、上下文裁剪、知识注入等工程实践。

## 4. 局限性
- 只能看到 Copilot 插件层面“最终发送给 LLM 的内容”，无法看到 LLM 内部的推理细节。
- 某些敏感信息可能被插件自动裁剪或脱敏。
- 需要一定英文基础和 prompt 工程经验，才能充分理解和利用这些底层信息。


## 5. 官方参考链接
- [Copilot Chat 官方文档（入口页）](https://docs.github.com/en/copilot/github-copilot-chat)
- [VS Code 命令面板/开发者工具](https://code.visualstudio.com/docs/getstarted/keybindings#_command-palette)
- [VS Code 调试与开发者工具](https://code.visualstudio.com/docs/editor/debugging)
- [Copilot Chat 插件源码（含 FAQ）](https://github.com/github/copilot.vscode)

## 6. 实践建议
- 多用该调试视图结合自己的配置和实际 prompt 进行比对。
- 如需更彻底的“白盒化”，可考虑用 OpenAI API、LangChain 等开源框架，自己拼接和记录 prompt。

---
如需进一步分析 prompt 结构或有其他 VS Code/Copilot 深度定制需求，可结合本说明和官方文档操作。