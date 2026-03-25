"""数据加载与预处理"""

from pathlib import Path

import pandas as pd
from loguru import logger


def load_raw_data(path: str = "data/raw") -> pd.DataFrame:
    """加载原始数据"""
    # TODO: 实现数据加载逻辑
    logger.info(f"加载数据: {path}")
    raise NotImplementedError


def save_processed_data(df: pd.DataFrame, path: str = "data/processed") -> None:
    """保存处理后的数据"""
    output = Path(path)
    output.mkdir(parents=True, exist_ok=True)
    # TODO: 实现保存逻辑
    logger.info(f"数据已保存: {output}")
