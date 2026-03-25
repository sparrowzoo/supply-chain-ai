"""模型评估 — 指标计算与报告生成"""

import numpy as np
from loguru import logger
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_model(y_true, y_pred) -> dict:
    """计算回归评估指标"""
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    metrics = {"rmse": rmse, "mae": mae, "r2": r2}
    logger.info(f"RMSE: {rmse:.4f} | MAE: {mae:.4f} | R²: {r2:.4f}")
    return metrics
