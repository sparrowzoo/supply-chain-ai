基于 XGBoost 的销量预测系统。

## 项目环境
- Python 环境: conda env `supply_chain_ai` (Python 3.12)
- 核心依赖: xgboost>=2.0.0, pandas, numpy, scikit-learn, joblib

## 项目结构
- `sales_forecast/src/data/` — 数据加载与处理
- `sales_forecast/src/features/` — 特征工程
- `sales_forecast/src/models/` — 模型训练与预测
- `sales_forecast/src/visualization/` — 可视化
- `sales_forecast/config/` — 配置文件
- `sales_forecast/tests/` — 测试
