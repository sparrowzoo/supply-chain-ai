# ML 项目脚手架规范

> 基于 [nanobot](https://github.com/dnakov/nanobot) 实际源码和 ML 社区最佳实践，制定的现代化 Python ML 项目脚手架标准。
> 本文档为 supply-chain-forecast 项目的脚手架规范，与实际代码保持同步。
>
> - 参考版本: nanobot v0.1.4.post4 (hatchling + typer + pydantic + loguru)
> - 适用范围: Python >=3.12，2026 年主流实践
> - 设计原则: **与 nanobot 保持一致，仅在 ML 场景需要时才扩展**
> - 封版日期: 2026-03-25

---

## 一、目录结构

```
supply-chain-forecast/               # 项目根目录
├── .github/
│   └── copilot-instructions.md      # Copilot 项目指令
├── .vscode/
│   ├── launch.json                  # 调试配置
│   └── settings.json                # VS Code 工作区配置（ruff formatter）
├── .dockerignore
├── .env.example                     # 环境变量模板（不含敏感值）
├── .gitignore
├── Dockerfile
├── LICENSE                          # MIT
├── Makefile
├── README.md
├── pyproject.toml                   # ← 唯一构建/依赖配置入口（无 requirements.txt）
│
├── config/                          # 运行时配置文件（YAML）
│   ├── base.yaml                    # 基础配置
│   └── local.yaml                   # 本地覆盖（gitignore）
│
├── data/                            # 数据目录（不提交）
│   ├── raw/                         # 原始数据
│   │   └── .gitkeep
│   ├── processed/                   # 处理后数据
│   │   └── .gitkeep
│   └── external/                    # 外部数据源
│       └── .gitkeep
│
├── models/                          # 训练产物（不提交，仅 .gitkeep）
│   └── .gitkeep
│
├── notebooks/                       # Jupyter 实验笔记本（提交）
│
├── logs/                            # 运行日志（不提交）
│   └── .gitkeep
│
├── reports/                         # 实验报告
│   └── figures/
│       └── .gitkeep
│
├── sales_forecast/                  # 📦 源码主包（项目同名）
│   ├── __init__.py                  # __version__ 定义
│   ├── __main__.py                  # python -m sales_forecast 入口
│   │
│   ├── cli/                         # 命令行接口
│   │   ├── __init__.py
│   │   └── commands.py
│   │
│   ├── config/                      # 配置管理（代码级）
│   │   ├── __init__.py              # 导出 AppConfig, load_config
│   │   ├── schema.py                # pydantic 配置 Schema
│   │   ├── loader.py                # YAML → pydantic 加载
│   │   └── paths.py                 # 路径辅助（参考 nanobot）
│   │
│   ├── data/                        # 数据层
│   │   ├── __init__.py
│   │   └── make_dataset.py
│   │
│   ├── features/                    # 特征工程
│   │   ├── __init__.py
│   │   └── build_features.py
│   │
│   ├── models/                      # 模型层（职责分离）
│   │   ├── __init__.py              # 导出 Trainer, Predictor, evaluate_model
│   │   ├── train.py                 # 训练
│   │   ├── predict.py               # 推理
│   │   └── evaluate.py              # 评估
│   │
│   ├── visualization/               # 可视化
│   │   ├── __init__.py
│   │   └── plots.py
│   │
│   └── utils/                       # 工具函数
│       ├── __init__.py
│       └── helpers.py
│
├── tests/                           # 测试
│   ├── __init__.py
│   ├── conftest.py                  # pytest fixtures
│   ├── test_config.py
│   ├── test_data.py
│   ├── test_features.py
│   └── test_models.py
│
└── template/                        # 脚手架规范文档
```

### 1.1 与 nanobot 的对应关系

| 层级 | nanobot | supply-chain-forecast | 说明 |
|------|---------|----------------------|------|
| 源码包 | `nanobot/` | `sales_forecast/` | 项目同名包，`pip install` 后可 import |
| 入口 | `__main__.py` → `cli.commands:app` | 相同 | `python -m sales_forecast` |
| CLI | `nanobot/cli/commands.py` (typer) | `sales_forecast/cli/commands.py` | 相同 |
| 配置 | `nanobot/config/{schema,loader,paths}.py` | `sales_forecast/config/` | 相同结构 |
| 工具 | `nanobot/utils/helpers.py` | `sales_forecast/utils/helpers.py` | 相同 |
| 测试 | `tests/` 根目录 | 相同 | 相同 |
| **ML 扩展** | — | `data/`, `features/`, `models/`, `visualization/` | ML 专有 |
| **ML 资源** | — | `data/`, `models/`, `notebooks/`, `reports/` | ML 产物目录 |

### 1.2 为什么用项目同名包而非 `src/`

| 对比 | `src/` 模式 | 项目同名包（采用） |
|------|------------|-------------------|
| import | `from src.models import ...` | `from sales_forecast.models import ...` |
| 安装后 | 不自然 | 与 pip install 后的 import 一致 |
| 代表项目 | nanobot ❌, FastAPI ❌, Django ❌ | nanobot ✅, FastAPI ✅, Django ✅ |
| pyproject | 需要 `package_dir` 映射 | `packages = ["sales_forecast"]` |

### 1.3 config/ 双层结构说明

项目中有**两个 config 目录**，职责不同：

```
config/                     ← 运行时配置文件（YAML，可被用户/运维修改）
  base.yaml                   纯数据，不含代码逻辑
  local.yaml                  本地覆盖，不提交

sales_forecast/config/      ← 配置管理代码（Python）
  schema.py                   定义配置结构 + 类型校验（pydantic）
  loader.py                   加载 config/base.yaml → pydantic 对象
  paths.py                    路径常量/辅助函数
```

**加载流程**: `config/base.yaml` → `loader.py` 读取 → `schema.py` 校验 → 类型安全的配置对象

---

## 二、核心文件规范

### 2.1 `pyproject.toml` — 项目唯一配置入口

> 对标 nanobot 的 pyproject.toml，保持结构一致。

```toml
[project]
name = "supply-chain-forecast"
version = "0.1.0"
description = "基于 XGBoost 的供应链销量预测系统"
requires-python = ">=3.12"
license = {text = "MIT"}
authors = [{name = "zhanglizhi"}]
keywords = ["ml", "forecasting", "xgboost", "supply-chain"]

dependencies = [
    "xgboost>=3.2.0",
    "pandas>=3.0.1",
    "numpy>=2.4.3",
    "scikit-learn>=1.8.0",
    "joblib>=1.5.3",
    "pydantic>=2.12.0,<3.0.0",
    "pydantic-settings>=2.12.0,<3.0.0",
    "pyyaml>=6.0",
    "loguru>=0.7.3,<1.0.0",
    "typer>=0.20.0,<1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=9.0.0,<10.0.0",
    "pytest-cov>=6.0.0,<7.0.0",
    "ruff>=0.1.0",
]
notebook = [
    "jupyter>=1.0.0",
    "matplotlib>=3.7.0",
    "seaborn>=0.12.0",
]
tracking = [
    "mlflow>=2.5.0",
]

[project.scripts]
sales-forecast = "sales_forecast.cli.commands:app"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["sales_forecast"]

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP", "B"]
ignore = ["E501", "N803", "N806"]
# E/F/W: pycodestyle + pyflakes (基础)
# I: isort (import 排序)
# N: pep8-naming (命名规范)
# UP: pyupgrade (自动升级旧语法)
# B: bugbear (常见 bug 检测)
# E501: 忽略行长硬限制，由 ruff format 自动处理
# N803/N806: ML 惯例使用大写 X, X_train, X_test（与 scikit-learn 一致）

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short"
```

**与 nanobot 的差异说明：**

| 配置项 | nanobot | 本项目 | 原因 |
|--------|---------|--------|------|
| `target-version` | `py311` | `py312` | 按实际环境 |
| ruff `select` | `E,F,I,N,W` | + `UP,B` | ML 项目代码质量更重要 |
| ruff `ignore` | `E501` | + `N803,N806` | ML 惯例大写 X/X_train |
| `hatch.build include` | 包含 `.md/.sh` 资源 | 不需要 | 无内嵌模板 |
| `keywords` | `ai, agent, chatbot` | `ml, forecasting, ...` | 业务不同 |
| 其余结构 | — | 完全一致 | — |

### 2.2 `sales_forecast/__init__.py`

> 对标 nanobot: 定义 `__version__`。

```python
"""supply-chain-forecast — 基于 XGBoost 的供应链销量预测系统"""

__version__ = "0.1.0"
```

### 2.3 `sales_forecast/__main__.py`

> 对标 nanobot: 支持 `python -m sales_forecast`。

```python
"""Entry point for: python -m sales_forecast"""

from sales_forecast.cli.commands import app

if __name__ == "__main__":
    app()
```

### 2.4 `Makefile` — 常用命令

```makefile
.PHONY: help install train predict evaluate test lint format clean

help:  ## 显示帮助
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## 安装项目（开发模式）
	pip install -e ".[dev]"

train:  ## 训练模型
	python -m sales_forecast train

predict:  ## 运行预测
	python -m sales_forecast predict

evaluate:  ## 评估模型
	python -m sales_forecast evaluate

test:  ## 运行测试
	pytest tests/ -v --cov=sales_forecast --cov-report=term-missing

lint:  ## 代码检查
	ruff check sales_forecast/ tests/
	ruff format --check sales_forecast/ tests/

format:  ## 格式化代码
	ruff format sales_forecast/ tests/
	ruff check --fix sales_forecast/ tests/

clean:  ## 清理产物
	rm -rf dist/ build/ *.egg-info/ .pytest_cache/ .ruff_cache/ .coverage htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
```

### 2.5 关于 `requirements.txt`

**本项目不使用 `requirements.txt`**，`pyproject.toml` 是唯一的依赖声明来源。

- Dockerfile 使用 `uv pip install --system .` 直接读取 `pyproject.toml`
- 开发环境使用 `pip install -e ".[dev]"`
- 如有特殊部署场景需要，可通过 `pip-compile pyproject.toml -o requirements.txt` 临时生成

---

## 三、核心模块规范

### 3.1 配置管理 — `sales_forecast/config/`

> 对标 nanobot 的 `config/{schema,loader,paths}.py` 三文件结构。

**schema.py** — pydantic 配置定义（注意子配置用 `BaseModel`，仅顶层用 `BaseSettings`）：

```python
# sales_forecast/config/schema.py
"""配置 Schema — pydantic 类型校验"""

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DataConfig(BaseModel):
    raw_path: str = "data/raw"
    processed_path: str = "data/processed"
    test_size: float = 0.2
    random_state: int = 42


class ModelConfig(BaseModel):
    n_estimators: int = 100
    max_depth: int = 5
    learning_rate: float = 0.1
    subsample: float = 0.8
    colsample_bytree: float = 0.8
    early_stopping_rounds: int = 10


class TrainConfig(BaseModel):
    cross_val_folds: int = 5
    save_model: bool = True
    model_dir: str = "models"


class LoggingConfig(BaseModel):
    level: str = "INFO"
    file: str = "logs/training.log"


class AppConfig(BaseSettings):
    """顶层配置，支持环境变量覆盖"""

    data: DataConfig = DataConfig()
    model: ModelConfig = ModelConfig()
    train: TrainConfig = TrainConfig()
    logging: LoggingConfig = LoggingConfig()
```

> **为什么子配置用 `BaseModel` 而非 `BaseSettings`?**
> pydantic-settings 不支持嵌套 `BaseSettings`。子配置用 `BaseModel` 定义结构，
> 仅顶层 `AppConfig` 继承 `BaseSettings` 以获取环境变量覆盖能力。
> 这也是 nanobot 的 `config/schema.py` 中的实际做法。

**loader.py** — 加载 YAML 配置文件：

```python
# sales_forecast/config/loader.py
from pathlib import Path

import yaml

from sales_forecast.config.schema import AppConfig


def load_config(config_path: str = "config/base.yaml") -> AppConfig:
    """加载 YAML 配置并校验为 pydantic 对象"""
    path = Path(config_path)
    if path.exists():
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        return AppConfig.model_validate(data)
    return AppConfig()
```

**paths.py** — 路径辅助（对标 nanobot 的 `config/paths.py`）：

```python
# sales_forecast/config/paths.py
"""路径辅助函数"""

from pathlib import Path


def get_project_root() -> Path:
    """返回项目根目录"""
    return Path(__file__).resolve().parent.parent.parent


def get_model_dir() -> Path:
    return get_project_root() / "models"


def get_data_dir(stage: str = "raw") -> Path:
    return get_project_root() / "data" / stage


def get_logs_dir() -> Path:
    return get_project_root() / "logs"
```

### 3.2 CLI 入口 — `sales_forecast/cli/`

> 对标 nanobot 的 `cli/commands.py` — 使用 typer。

```python
# sales_forecast/cli/commands.py
"""CLI 命令定义 — 使用 typer 构建"""

from pathlib import Path

import typer
from loguru import logger

app = typer.Typer(help="供应链销量预测系统")


@app.command()
def train(config: str = "config/base.yaml"):
    """训练模型"""
    logger.info(f"加载配置: {config}")
    # TODO: from sales_forecast.models.train import run_training
    # run_training(config)


@app.command()
def predict(
    model_path: str = "models/model.joblib",
    input_file: Path | None = None,
):
    """使用模型预测"""
    logger.info(f"加载模型: {model_path}")
    # TODO: from sales_forecast.models.predict import run_prediction
    # run_prediction(model_path, input_file)


@app.command()
def evaluate(model_path: str = "models/model.joblib"):
    """评估模型性能"""
    logger.info("开始评估...")
    # TODO: from sales_forecast.models.evaluate import run_evaluation
    # run_evaluation(model_path)


if __name__ == "__main__":
    app()
```

安装后可直接调用：
```bash
sales-forecast train --config config/base.yaml
sales-forecast predict --model-path models/best.joblib
# 或
python -m sales_forecast train
```

### 3.3 日志 — loguru

> nanobot 全局使用 `from loguru import logger`，不用标准库 logging。

```python
from loguru import logger

logger.info("模型训练完成")
logger.info(f"RMSE: {rmse:.4f}")

# 输出到文件（自动轮转）
logger.add("logs/training.log", rotation="10 MB")
```

### 3.4 模型层 — 职责分离

| 文件 | 职责 | 对应 nanobot 设计原则 |
|------|------|---------------------|
| `train.py` | 模型创建、训练、保存 | 单一职责 |
| `predict.py` | 加载模型、推理 | 单一职责 |
| `evaluate.py` | 指标计算、报告生成 | 单一职责 |

不要把训练+预测+评估+保存全放在一个类里。参考 nanobot 的模块拆分:
每个文件一个核心职责，通过 `__init__.py` 导出公共 API。

### 3.5 `__init__.py` 导出规范

> nanobot 在每个子包的 `__init__.py` 中定义 `__all__`，导出公共 API。

```python
# sales_forecast/models/__init__.py
"""模型层"""

from sales_forecast.models.evaluate import evaluate_model
from sales_forecast.models.predict import Predictor
from sales_forecast.models.train import Trainer

__all__ = ["Trainer", "Predictor", "evaluate_model"]
```

```python
# sales_forecast/config/__init__.py
"""配置管理模块"""

from sales_forecast.config.loader import load_config
from sales_forecast.config.schema import AppConfig

__all__ = ["AppConfig", "load_config"]
```

### 3.6 `.env.example` — 环境变量模板

```bash
# .env.example — 复制为 .env 并填入实际值
# MLFLOW_TRACKING_URI=http://localhost:5000
# MLFLOW_EXPERIMENT_NAME=sales-forecast
```

### 3.7 `tests/conftest.py` — pytest fixtures

```python
# tests/conftest.py
"""pytest fixtures"""

import numpy as np
import pandas as pd
import pytest

from sales_forecast.config.schema import AppConfig


@pytest.fixture
def app_config():
    """测试用默认配置"""
    return AppConfig()


@pytest.fixture
def sample_dataframe():
    """测试用样本数据"""
    np.random.seed(42)
    return pd.DataFrame(
        {
            "feature_1": np.random.randn(100),
            "feature_2": np.random.randn(100),
            "target": np.random.randn(100),
        }
    )


@pytest.fixture
def tmp_model_dir(tmp_path):
    """临时模型目录"""
    model_dir = tmp_path / "models"
    model_dir.mkdir()
    return model_dir
```

---

## 四、工具链选型

| 类别 | 选型 | 替代方案 | 理由 |
|------|------|---------|------|
| 构建 | hatchling | setuptools | nanobot 同款，PEP 标准 |
| 包管理 | uv | pip | 10-100x 速度，nanobot Docker 采用 |
| 代码规范 | ruff | black+pylint+isort | nanobot 同款，全合一 |
| 类型检查 | pyright | mypy | 可选但推荐 |
| 测试 | pytest + pytest-cov | unittest | 社区标准 |
| 日志 | loguru | logging | nanobot 同款，API 更简洁 |
| 配置 | pydantic-settings | hydra/omegaconf | nanobot 同款，类型安全 |
| CLI | typer | argparse/click | nanobot 同款，自动生成帮助 |
| 实验追踪 | mlflow | wandb | 开源可自托管 |
| 容器化 | Docker + uv | conda-pack | nanobot 同款 |
| CI/CD | GitHub Actions | — | 社区标准 |

---

## 五、`.gitignore` 标准模板

```gitignore
# Python
__pycache__/
*.py[cod]
*.so
*.egg-info/
dist/
build/
.venv/
venv/

# 数据与模型产物（大文件不提交，但保留目录结构）
data/raw/
data/processed/
data/external/
/models/
!data/raw/.gitkeep
!data/processed/.gitkeep
!data/external/.gitkeep
!/models/.gitkeep

# 日志
logs/
!logs/.gitkeep

# 笔记本（提交 notebook 文件，仅忽略 checkpoint）
# .ipynb_checkpoints/ 已在下方 Jupyter 部分忽略

# 报告产物
reports/figures/
!reports/figures/.gitkeep

# 环境与密钥
.env
config/local.yaml

# IDE
.idea/

# Jupyter
.ipynb_checkpoints/

# 测试与覆盖率
.pytest_cache/
.coverage
htmlcov/

# ruff
.ruff_cache/

# 模型文件
*.pkl
*.joblib
*.h5
*.onnx
```

> **重要**: 根目录 `models/` 使用 `/models/`（前导斜杠）限定只匹配项目根目录，
> 避免误忽略 `sales_forecast/models/` 源码目录。同时通过扩展名规则
> (`*.joblib` `*.pkl` 等) 双重保障。

---

## 六、Dockerfile 参考

> 对标 nanobot Dockerfile: 使用 uv 基础镜像 + 分层缓存。

```dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# 先安装依赖（利用 Docker 层缓存）
COPY pyproject.toml README.md ./
RUN mkdir -p sales_forecast && touch sales_forecast/__init__.py && \
    uv pip install --system --no-cache . && \
    rm -rf sales_forecast

# 再复制源码
COPY sales_forecast/ sales_forecast/
RUN uv pip install --system --no-cache .

ENTRYPOINT ["sales-forecast"]
CMD ["train"]
```

> **说明**: Dockerfile 不 COPY `requirements.txt`，直接通过 `pyproject.toml` 安装依赖。
> `README.md` 必须 COPY 是因为 hatchling 构建时需要读取它。

---

## 七、配置文件实例

### 7.1 `config/base.yaml`

YAML 结构必须与 `schema.py` 的 pydantic 模型字段**扁平对应**，不要使用额外嵌套层级：

```yaml
# 基础配置
data:
  raw_path: data/raw
  processed_path: data/processed
  test_size: 0.2
  random_state: 42

model:
  n_estimators: 100
  max_depth: 5
  learning_rate: 0.1
  subsample: 0.8
  colsample_bytree: 0.8
  early_stopping_rounds: 10

train:
  cross_val_folds: 5
  save_model: true
  model_dir: models

logging:
  level: INFO
  file: logs/training.log
```

> **注意**: YAML key 必须与 pydantic Schema 字段名一一对应。
> 不要使用 `model.params.n_estimators` 这样的嵌套结构，
> 否则 pydantic 会静默忽略不匹配的字段，回退到默认值。

### 7.2 `.env.example`

```bash
# .env.example — 复制为 .env 并填入实际值
# MLFLOW_TRACKING_URI=http://localhost:5000
# MLFLOW_EXPERIMENT_NAME=sales-forecast
```

### 7.3 `.dockerignore`

```
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.venv/
venv/
.git/
.pytest_cache/
.ruff_cache/
.coverage
htmlcov/
data/
models/
logs/
notebooks/
*.pkl
*.joblib
*.h5
*.onnx
.env
```

---

## 八、工具链验证命令

以下命令可验证脚手架是否完整：

```bash
# 安装
pip install -e ".[dev]"

# CLI 验证
python -m sales_forecast --help
sales-forecast --help

# 导入验证
python -c "from sales_forecast.config import AppConfig, load_config; print(load_config().model_dump())"

# 代码规范
ruff check sales_forecast/ tests/
ruff format --check sales_forecast/ tests/

# 测试
pytest tests/ -v --cov=sales_forecast --cov-report=term-missing
```
