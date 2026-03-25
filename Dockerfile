FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# 先安装依赖（利用 Docker 层缓存）
COPY pyproject.toml README.md ./
RUN mkdir -p sales_forecast && touch sales_forecast/__init__.py && \
    uv pip install --system --no-cache . && \
    rm -rf sales_forecast

# 再复制源码
COPY sales_forecast/ sales_forecast/
RUN uv pip install --system --no-cache .

ENTRYPOINT ["sales-forecast"]
CMD ["train"]
