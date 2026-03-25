.PHONY: help install train predict evaluate test lint format clean

help:  ## 显示帮助
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## 安装项目（开发模式）
	pip install -e ".[dev]"

train:  ## 训练模型
	python -m sales_forecast train

predict:  ## 运行预测
	python -m sales_forecast predict

evaluate:  ## 评估模型
	python -m sales_forecast evaluate

test:  ## 运行测试
	pytest tests/ -v --cov=sales_forecast --cov-report=term-missing

lint:  ## 代码检查
	ruff check sales_forecast/ tests/
	ruff format --check sales_forecast/ tests/

format:  ## 格式化代码
	ruff format sales_forecast/ tests/
	ruff check --fix sales_forecast/ tests/

clean:  ## 清理产物
	rm -rf dist/ build/ *.egg-info/ .pytest_cache/ .ruff_cache/ .coverage htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
