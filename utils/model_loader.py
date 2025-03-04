import tensorflow as tf
import numpy as np
import os

MODEL_PATH = 'model/food_recognition.tflite'

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Ошибка: Файл модели {MODEL_PATH} не найден!")

    interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
    interpreter.allocate_tensors()
    return interpreter

def predict_dish(processed_img):
    interpreter = load_model()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], processed_img)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_class = np.argmax(output_data)

    return predicted_class
