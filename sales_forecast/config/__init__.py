"""配置管理模块"""

from sales_forecast.config.loader import load_config
from sales_forecast.config.schema import AppConfig

__all__ = ["AppConfig", "load_config"]
