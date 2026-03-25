```
ml_project/
├── .env.example                # 环境变量示例
├── .gitignore                  # Git 忽略文件
├── Makefile                    # 常用命令（如 make train）
├── README.md                   # 项目说明
├── requirements.txt            # Python 依赖
├── setup.py                    # 安装脚本
├── config/
│   ├── base.yaml               # 基础配置
│   └── local.yaml              # 本地配置（覆盖基础配置）
├── data/
│   ├── external/               # 外部数据
│   ├── processed/              # 处理后数据
│   └── raw/                    # 原始数据
├── logs/                       # 日志文件
├── models/                     # 保存训练好的模型
├── notebooks/                  # Jupyter 实验笔记本
├── reports/                    # 生成的可视化报告
│   └── figures/
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── make_dataset.py     # 数据下载/加载/拆分
│   ├── features/
│   │   ├── __init__.py
│   │   └── build_features.py   # 特征工程
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train_model.py      # 训练脚本
│   │   └── predict_model.py    # 预测脚本
│   └── visualization/
│       ├── __init__.py
│       └── visualize.py        # 可视化函数
└── tests/
    ├── __init__.py
    ├── test_data.py
    ├── test_features.py
    └── test_models.py
```