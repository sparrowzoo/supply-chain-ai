"""通用辅助函数"""

from pathlib import Path


def ensure_dir(path: Path) -> Path:
    """确保目录存在，不存在则创建"""
    path.mkdir(parents=True, exist_ok=True)
    return path
