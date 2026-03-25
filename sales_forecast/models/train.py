"""模型训练 — 创建、训练、保存模型"""

from pathlib import Path

import joblib
import xgboost as xgb
from loguru import logger
from sklearn.model_selection import train_test_split

from sales_forecast.config.schema import AppConfig
from sales_forecast.models.evaluate import evaluate_model


class Trainer:
    """XGBoost 模型训练器"""

    def __init__(self, config: AppConfig | None = None):
        self.config = config or AppConfig()
        self.model = None

    def train(self, X, y):
        """训练 XGBoost 模型"""
        mc = self.config.model
        dc = self.config.data

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=dc.test_size, random_state=dc.random_state
        )

        self.model = xgb.XGBRegressor(
            n_estimators=mc.n_estimators,
            max_depth=mc.max_depth,
            learning_rate=mc.learning_rate,
            subsample=mc.subsample,
            colsample_bytree=mc.colsample_bytree,
            random_state=dc.random_state,
            objective="reg:squarederror",
            early_stopping_rounds=mc.early_stopping_rounds,
        )

        self.model.fit(
            X_train,
            y_train,
            eval_set=[(X_test, y_test)],
            verbose=False,
        )

        y_pred = self.model.predict(X_test)
        metrics = evaluate_model(y_test, y_pred)
        return metrics

    def save(self, path: str | None = None):
        """保存模型"""
        save_path = Path(path or self.config.train.model_dir) / "model.joblib"
        save_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.model, save_path)
        logger.info(f"模型已保存: {save_path}")
