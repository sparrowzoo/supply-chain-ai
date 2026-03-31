# 项目说明
- 基于 XGBoost 的供应链销量预测系统

## 项目环境
- Python 环境: conda env `supply_chain_ai` (Python 3.12)
- 主要依赖: xgboost, pandas, numpy, scikit-learn, joblib
- 工具链: hatchling, ruff, pytest, loguru, typer, pydantic-settings

## Copilot 项目偏好
- 每次请求自动生成当前上下文快照，保存到 context 目录，文件名格式为 c-年月日时分秒.md
- 快照内容需与 Copilot 实际用到的全部上下文一致，包括知识文件、环境、目录、编辑器状态等
- 快照需包含最近10轮对话内容（用户与 Copilot 的问答）
- 目录结构不需要动态扫描
- 代码建议需符合团队规范，优先生成可维护、易协作的代码
- 测试建议需覆盖主流程和边界场景

## 项目结构
- `sales_forecast/` — 源码主包
  - `cli/` — CLI 命令 (typer)
  - `config/` — 配置管理 (pydantic)
  - `data/` — 数据加载与处理
  - `features/` — 特征工程
  - `models/` — 模型训练/预测/评估
  - `visualization/` — 可视化
  - `utils/` — 工具函数
- `config/` — YAML 配置文件
- `tests/` — 测试