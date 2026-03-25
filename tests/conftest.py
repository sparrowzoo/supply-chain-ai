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
