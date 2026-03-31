# 自定义 Copilot/Agent Skill 说明及定义操作步骤详解

本指南适用于 VS Code Copilot/Agent 用户，手把手教你如何自定义一个全局 skill（以“记记字典”为例），实现本地知识记忆、查询等能力。适合零基础用户。

---

## 1. Skill 目录结构规范

全局 skill 建议统一放在：
```
~/.vscode/extensions/github.copilot-skill/agent-customization/你的-skill目录/
```
如本例：
```
~/.vscode/extensions/github.copilot-skill/agent-customization/python-assistant/
```

## 2. Skill 说明文档与实现代码

- 说明文档：SKILL.md（描述 skill 能力、用法、交互风格等）
- 实现代码：如 local_dict.py（具体功能实现）

二者需同目录归档。

## 3. Skill 说明文档（SKILL.md）模板

```yaml
---
description: |
  简要描述 skill 能力、适用场景。
  ...
skills:
  - name: 你的 skill 名称（建议自然语言，如“记记字典”）
    description: skill 详细说明。
    usage: |
      - 用自然语言举例说明如何触发。
      - 如需代码集成/命令行体验也可补充。
    entry: 入口脚本（如 local_dict.py）
    example: |
      # 自然语言对话
      ...
      # 代码调用
      ...
prompt: |
  详细说明 LLM/Agent 行为风格、边界、注意事项。
  ...
---
```

## 4. 实现代码（如 local_dict.py）

- 可用 Python 实现你的功能类/脚本。
- 支持命令行交互、类调用等。
- 示例见本项目 python-assistant/local_dict.py。

## 5. 操作步骤（以“记记字典”skill为例）

### 步骤一：创建 skill 目录
```bash
mkdir -p ~/.vscode/extensions/github.copilot-skill/agent-customization/python-assistant
```

### 步骤二：编写 SKILL.md
将上面模板内容结合你的需求填写，保存为：
```
~/.vscode/extensions/github.copilot-skill/agent-customization/python-assistant/SKILL.md
```

### 步骤三：实现功能代码
如 local_dict.py，放在同目录下。

### 步骤四：重启 VS Code（或 Copilot/Agent）
让新 skill 生效。

### 步骤五：体验 skill
直接用自然语言对话，如：
- 记住 foo=bar 到本地字典
- 查查 foo
- 删除 foo
- 列出所有知识点

Agent 会自动调用 skill，直接返回结果。

---

## 6. 常见问题与建议
- skill 名称建议用自然语言，便于记忆和触发。
- prompt 字段决定 Agent 行为风格，建议写明“只返回结果、不展示细节”等。
- 说明文档和代码必须同目录。
- 支持多 skill 并存，互不影响。
- 如需批量/特殊操作，Agent 会主动询问。

---

## 7. 参考示例
详见本项目 python-assistant 目录下 SKILL.md 和 local_dict.py。

如有疑问或需进阶用法，欢迎随时咨询！


