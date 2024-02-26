import os
import argparse
from transformers import pipeline
from flask import Flask, request, jsonify

def load_model(model_name, model_dir):
    return pipeline("text-generation", model=model_name, tokenizer=model_name)

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
    args = parser.parse_args()

    model = load_model(args.model_name, args.model_dir)
    serve_model(model)

