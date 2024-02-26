FROM python:3.8-slim

RUN pip install --no-cache-dir torch transformers
RUN pip install --no-cache-dir boto3
RUN pip install --no-cache-dir flask

# スクリプトを追加
WORKDIR /app
COPY serve_model.py /app/serve_model.py
