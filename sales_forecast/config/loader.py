"""配置加载器 — 从 YAML 文件加载并校验为 pydantic 对象"""

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
