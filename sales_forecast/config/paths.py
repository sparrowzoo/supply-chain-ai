"""路径辅助函数"""

from pathlib import Path


def get_project_root() -> Path:
    """返回项目根目录"""
    return Path(__file__).resolve().parent.parent.parent


def get_model_dir() -> Path:
    return get_project_root() / "models"


def get_data_dir(stage: str = "raw") -> Path:
    return get_project_root() / "data" / stage


def get_logs_dir() -> Path:
    return get_project_root() / "logs"
