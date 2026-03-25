import os
import sys

# 从命令行参数获取项目名称，默认为 sales_forecast
if len(sys.argv) > 1:
    PROJECT_NAME = sys.argv[1]
else:
    PROJECT_NAME = "default_project"

# 目录结构
DIRS = [
    f"{PROJECT_NAME}/config",
    f"{PROJECT_NAME}/data/external",
    f"{PROJECT_NAME}/data/processed",
    f"{PROJECT_NAME}/data/raw",
    f"{PROJECT_NAME}/logs",
    f"{PROJECT_NAME}/models",
    f"{PROJECT_NAME}/notebooks",
    f"{PROJECT_NAME}/reports/figures",
    f"{PROJECT_NAME}/src/data",
    f"{PROJECT_NAME}/src/features",
    f"{PROJECT_NAME}/src/models",
    f"{PROJECT_NAME}/src/visualization",
    f"{PROJECT_NAME}/tests",
]

# 文件内容（描述性文件完整，代码文件仅含注释）
FILES = {
    f"{PROJECT_NAME}/.env.example": """# 环境变量示例
DATABASE_URL=postgresql://user:pass@localhost/dbname
MLFLOW_TRACKING_URI=http://localhost:5000
""",
    f"{PROJECT_NAME}/.gitignore": """# Python
__pycache__/
*.py[cod]
*.so
.Python
env/
venv/
*.egg-info/
dist/
build/

# Data
data/raw/
data/processed/
models/
logs/

# IDE
.vscode/
.idea/

# Jupyter
.ipynb_checkpoints/
*.ipynb
""",
    f"{PROJECT_NAME}/Makefile": """# 常用命令
.PHONY: train test clean

train:
	python src/models/train_model.py

test:
	pytest tests/

clean:
	rm -rf data/processed/*
	rm -rf models/*
	rm -rf logs/*
""",
    f"{PROJECT_NAME}/README.md": """# 机器学习项目模板


## 项目结构
参见目录说明。

## 快速开始
""",
    f"{PROJECT_NAME}/requirements.txt": """# 核心库
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
matplotlib==3.7.2
seaborn==0.12.2

# 可选
jupyter==1.0.0
mlflow==2.5.0
pyyaml==6.0
pytest==7.4.0
python-dotenv==1.0.0
""",
    f"{PROJECT_NAME}/setup.py": """from setuptools import setup, find_packages

setup(
    name="ml_project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
    ],
    author="Your Name",
    description="A machine learning project template",
)
""",
    f"{PROJECT_NAME}/config/base.yaml": """# 基础配置
data:
  raw_path: data/raw
  processed_path: data/processed
  test_size: 0.2
  random_state: 42

model:
  name: logistic_regression
  params:
    C: 1.0
    max_iter: 1000

train:
  cross_val_folds: 5
  save_model: true
  model_dir: models

logging:
  level: INFO
  file: logs/training.log
""",
    f"{PROJECT_NAME}/config/local.yaml": """# 本地覆盖配置（不提交到版本控制）
data:
  raw_path: /custom/path/to/raw_data
""",
    f"{PROJECT_NAME}/src/__init__.py": "",
    f"{PROJECT_NAME}/src/data/__init__.py": "",
    f"{PROJECT_NAME}/src/data/make_dataset.py": """# 数据加载/拆分脚本（请在此实现具体逻辑）
\"\"\"
此模块负责加载原始数据、进行训练/测试集划分，并保存处理后的数据。
\"\"\"
""",
    f"{PROJECT_NAME}/src/features/__init__.py": "",
    f"{PROJECT_NAME}/src/features/build_features.py": """# 特征工程脚本（请在此实现特征构建、标准化等）
\"\"\"
此模块负责特征预处理、特征选择、特征变换等。
\"\"\"
""",
    f"{PROJECT_NAME}/src/models/__init__.py": "",
    f"{PROJECT_NAME}/src/models/train_model.py": """# 模型训练脚本（请在此实现训练逻辑）
\"\"\"
此模块负责模型训练、超参数调优、模型保存等。
\"\"\"
""",
    f"{PROJECT_NAME}/src/models/predict_model.py": """# 模型预测脚本（请在此实现预测逻辑）
\"\"\"
此模块负责加载已训练模型并对新数据进行预测。
\"\"\"
""",
    f"{PROJECT_NAME}/src/visualization/__init__.py": "",
    f"{PROJECT_NAME}/src/visualization/visualize.py": """# 可视化脚本（请在此实现绘图函数）
\"\"\"
此模块提供数据探索、模型评估结果的可视化函数。
\"\"\"
""",
    f"{PROJECT_NAME}/tests/__init__.py": "",
    f"{PROJECT_NAME}/tests/test_data.py": """# 数据模块的单元测试
\"\"\"
测试数据加载和预处理函数。
\"\"\"
""",
    f"{PROJECT_NAME}/tests/test_features.py": """# 特征模块的单元测试
\"\"\"
测试特征工程函数。
\"\"\"
""",
    f"{PROJECT_NAME}/tests/test_models.py": """# 模型模块的单元测试
\"\"\"
测试模型训练和预测函数。
\"\"\"
""",
}

def create_project():
    """创建项目目录和文件（代码文件仅含注释）"""
    for dir_path in DIRS:
        os.makedirs(dir_path, exist_ok=True)
        print(f"创建目录: {dir_path}")

    for file_path, content in FILES.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"创建文件: {file_path}")

    print(f"\n项目脚手架已创建在 '{PROJECT_NAME}' 目录下。")
    print("下一步：")
    print(f"  cd {PROJECT_NAME}")
    print("  python -m venv venv")
    print(f"  pip install -e ./{PROJECT_NAME}")

if __name__ == "__main__":
    create_project()