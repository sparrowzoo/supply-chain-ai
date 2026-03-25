from setuptools import setup, find_packages

setup(
    name="supply-chain-forecast",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "xgboost>=3.2.0",
        "pandas>=3.0.1",
        "numpy>=2.4.3",
        "scikit-learn>=1.8.0",
        "joblib>=1.5.3",
    ],
    author="zhanglizhi",
    description="基于 XGBoost 的销量预测系统",
)
