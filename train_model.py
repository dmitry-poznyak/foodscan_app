import tensorflow as tf
import tensorflow_datasets as tfds
import os

# Загружаем датасет Food-101
dataset, info = tfds.load("food101", split="train", with_info=True, as_supervised=True)

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# Функция для предобработки изображений
def preprocess(image, label):
    image = tf.cast(image, tf.float32) / 255.0  # Приводим к float32 и масштабируем
    image = tf.image.resize(image, IMG_SIZE)
    return image, label

# Преобразуем датасет
dataset = dataset.map(lambda img, lbl: preprocess(img, lbl)).batch(BATCH_SIZE).shuffle(1000)

# Загружаем MobileNetV2 без верхнего слоя
base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights="imagenet")
base_model.trainable = False  # Замораживаем веса

# Добавляем классификационный слой
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(101, activation="softmax")  # 101 класс блюд
])

# Компилируем модель
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Обучаем модель (ограничим число эпох для скорости)
EPOCHS = 5
model.fit(dataset, epochs=EPOCHS)

# Конвертируем в формат TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Создаём папку для модели (если её нет)
os.makedirs("model", exist_ok=True)

# Сохраняем модель
with open("model/food_recognition.tflite", "wb") as f:
    f.write(tflite_model)

print("Модель обучена и сохранена в формате .tflite")
