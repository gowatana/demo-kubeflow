import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def save_model(volume_path, model_name):
    # モデルとトークナイザーのロード
    # model_name = "cyberagent/open-calm-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # モデルとトークナイザーの保存
    # volume_path = "/mnt/saved_model"
    model_save_path = f"{volume_path}"
    tokenizer.save_pretrained(model_save_path)
    model.save_pretrained(model_save_path)

if __name__ == '__main__':
    volume_path = sys.argv[1]  # ボリュームのパスをコマンドライン引数から取得
    model_name = sys.argv[2]  # モデル名をコマンドライン引数から取得
    save_model(volume_path, model_name)

