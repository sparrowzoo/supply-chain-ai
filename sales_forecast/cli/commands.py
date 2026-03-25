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
