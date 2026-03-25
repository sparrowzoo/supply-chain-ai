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
