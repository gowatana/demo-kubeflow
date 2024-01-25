import sys
import tensorflow as tf
import numpy as np

def predict_model(volume_path):
    model = tf.keras.models.load_model(f'{volume_path}/mnist_saved_model')
    new_data = np.random.rand(28, 28).reshape(1, 28, 28) / 255.0
    predictions = model.predict(new_data)
    predicted_class = np.argmax(predictions, axis=1)
    print("Predicted class:", predicted_class)
    with open(f'{volume_path}/predictions.txt', 'w') as f:
        f.write("Predicted class: " + str(predicted_class[0]) + "\n")

if __name__ == '__main__':
    volume_path = sys.argv[1]  # ボリュームのパスをコマンドライン引数から取得
    predict_model(volume_path)

