"""模型预测 — 加载已训练模型并推理"""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from loguru import logger


class Predictor:
    """加载模型并执行预测"""

    def __init__(self, model_path: str = "models/model.joblib"):
        self.model_path = Path(model_path)
        self.model = None

    def load(self):
        """加载模型"""
        if not self.model_path.exists():
            raise FileNotFoundError(f"模型文件不存在: {self.model_path}")
        self.model = joblib.load(self.model_path)
        logger.info(f"模型已加载: {self.model_path}")

    def predict(self, X: pd.DataFrame | np.ndarray) -> np.ndarray:
        """执行预测"""
        if self.model is None:
            self.load()
        return self.model.predict(X)
