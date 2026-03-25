基于 XGBoost 的供应链销量预测系统。

## 项目环境
- Python 环境: conda env `supply_chain_ai` (Python 3.12)
- 核心依赖: xgboost, pandas, numpy, scikit-learn, joblib
- 工具链: hatchling + ruff + pytest + loguru + typer + pydantic-settings

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
