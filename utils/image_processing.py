from PIL import Image as PILImage
import numpy as np

def preprocess_image(image_path):
    img = PILImage.open(image_path)
    img = img.resize((224, 224))  # Изменяем размер изображения под модель
    img = np.array(img) / 255.0  # Нормализуем пиксели
    img = np.expand_dims(img, axis=0).astype(np.float32)  # Приводим к float32
    return img
