# 常用命令
.PHONY: train test clean

train:
	python src/models/train_model.py

test:
	pytest tests/

clean:
	rm -rf data/processed/*
	rm -rf models/*
	rm -rf logs/*
