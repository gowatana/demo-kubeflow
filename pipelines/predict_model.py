import tensorflow as tf
import numpy as np

def predict_model():
    model = tf.keras.models.load_model('/mnt/demo-vol-01/mnist_saved_model')
    new_data = np.random.rand(28, 28)
    new_data = new_data.reshape(1, 28, 28) / 255.0
    predictions = model.predict(new_data)
    predicted_class = np.argmax(predictions, axis=1)
    print("Predicted class:", predicted_class)
    with open('/mnt/demo-vol-01/predictions.txt', 'w') as f:
        f.write("Predicted class: " + str(predicted_class[0]) + "\n")

