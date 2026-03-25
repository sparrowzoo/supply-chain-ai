# Supply Chain Forecast

基于 XGBoost 的供应链销量预测系统。

## 快速开始

```bash
# 安装（开发模式）
pip install -e ".[dev]"

# 训练
sales-forecast train

# 预测
sales-forecast predict

# 评估
sales-forecast evaluate

# 测试
make test

# 代码检查
make lint
```

## 项目结构

```
supply-chain-forecast/
├── config/              # 运行时配置 (YAML)
├── data/                # 数据目录
├── models/              # 训练产物
├── sales_forecast/      # 源码主包
│   ├── cli/             # CLI 命令
│   ├── config/          # 配置管理代码
│   ├── data/            # 数据加载
│   ├── features/        # 特征工程
│   ├── models/          # 模型 (train/predict/evaluate)
│   ├── visualization/   # 可视化
│   └── utils/           # 工具函数
├── tests/               # 测试
└── template/            # 脚手架参考文档
```

## 技术栈

| 类别 | 工具 |
|------|------|
| ML 框架 | XGBoost |
| 数据处理 | pandas, numpy, scikit-learn |
| 构建 | hatchling |
| CLI | typer |
| 配置 | pydantic-settings + YAML |
| 日志 | loguru |
| 代码规范 | ruff |
| 测试 | pytest |
