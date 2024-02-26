import os
import argparse
from transformers import pipeline
from flask import Flask, request, jsonify
import tempfile
import boto3
import botocore

def download_model_from_minio(bucket_url, model_dir):
    # S3互換のMinioクライアントを作成
    s3_client = boto3.client(
        "s3",
        endpoint_url=bucket_url,
        config=boto3.session.Config(signature_version=botocore.UNSIGNED)
    )

    # 一時ディレクトリを作成
    temp_dir = tempfile.mkdtemp()

    # バケット内のファイルを一時ディレクトリにダウンロード
    bucket_name = model_dir.split("/", 1)[0]
    model_path = model_dir.split("/", 1)[1]
    for obj in s3_client.list_objects(Bucket=bucket_name, Prefix=model_path)["Contents"]:
        dest_path = os.path.join(temp_dir, os.path.relpath(obj["Key"], model_path))
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        s3_client.download_file(bucket_name, obj["Key"], dest_path)

    return temp_dir

def load_model(model_name, model_dir, bucket_url):
    # Minioバケットからモデルをダウンロード
    downloaded_model_dir = download_model_from_minio(bucket_url, model_dir)
    # ダウンロードしたディレクトリからモデルをロード
    return pipeline("text-generation", model=downloaded_model_dir, tokenizer=model_name)

def serve_model(model):
    app = Flask(__name__)

    @app.route("/generate", methods=["POST"])
    def generate():
        input_data = request.json.get("input_text")
        output = model(input_data)
        return jsonify({"output_text": output})

    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, required=True)
    parser.add_argument("--model_dir", type=str, required=True)
    parser.add_argument("--bucket_url", type=str, required=True)
    args = parser.parse_args()

    model = load_model(args.model_name, args.model_dir, args.bucket_url)
    serve_model(model)

