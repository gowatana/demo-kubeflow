import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def gen_text(model_save_path, output_file_path, input_text):
    # GPUがある場合は利用
    device = 0 if torch.cuda.is_available() else -1

    # モデルとトークナイザーのロード
    tokenizer = AutoTokenizer.from_pretrained(model_save_path, token=False, truncation=True)
    model = AutoModelForCausalLM.from_pretrained(model_save_path, token=False)

    # 生成用のパイプラインをセットアップ
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer, device=device)

    # テキスト生成
    generated_texts = generator(
        input_text,
        max_length=30,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7,
        repetition_penalty=1.2,
        top_k=50,
        pad_token_id=0
    )

    generated_text = generated_texts[0]['generated_text']  # 最初の生成テキストを取得
    print(f"Generated text: {generated_text}")  # 生成テキストを表示

    # ファイルに保存
    with open(output_file_path, 'w') as f:
        f.write(generated_text)

    # ファイル内容を表示
    with open(output_file_path, 'r') as f:
        print("Saved text content:")
        print(f.read())

if __name__ == '__main__':
    model_save_path = sys.argv[1]  # モデルの保存パスをコマンドライン引数から取得
    output_file_path = sys.argv[2]
    input_text = sys.argv[3]  # 入力テキストをコマンドライン引数から取得
    gen_text(model_save_path, output_file_path, input_text)

