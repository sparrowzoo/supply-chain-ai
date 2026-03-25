"""可视化 — 数据探索与模型评估图表"""

from loguru import logger


def plot_feature_importance(model, feature_names: list[str]) -> None:
    """绘制特征重要性"""
    # TODO: 实现特征重要性图
    logger.info("特征重要性图")


def plot_prediction_vs_actual(y_true, y_pred) -> None:
    """绘制预测值 vs 实际值"""
    # TODO: 实现预测对比图
    logger.info("预测 vs 实际图")
