import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

import tensorflow as tf
import numpy as np
from PIL import Image as PILImage

from utils.image_processing import preprocess_image
from utils.model_loader import predict_dish
from utils.recipes import get_recipe

MODEL_PATH = "model/food_recognition.tflite"

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Загрузите фото блюда", size_hint=(1, 0.1))
        layout.add_widget(self.label)

        self.img = Image(size_hint=(1, 0.5))
        layout.add_widget(self.img)

        self.result_label = Label(text="Результат: ", size_hint=(1, 0.2))
        layout.add_widget(self.result_label)

        self.choose_file_btn = Button(text="Выбрать изображение", size_hint=(1, 0.1))
        self.choose_file_btn.bind(on_press=self.choose_file)
        layout.add_widget(self.choose_file_btn)

        return layout

    def choose_file(self, instance):
        chooser = FileChooserIconView(filters=['*.png', '*.jpg', '*.jpeg'], multiselect=False)
        self.popup = Popup(title="Выберите изображение", size_hint=(0.9, 0.9))

        btn_select = Button(text="Открыть", size_hint_y=None, height=50)
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(chooser)
        layout.add_widget(btn_select)

        self.popup.content = layout
        btn_select.bind(on_press=lambda x: self.on_file_select(chooser.selection))

        self.popup.open()

    def on_file_select(self, selection):
        if selection:
            file_path = selection[0]
            self.img.source = file_path
            self.img.reload()

            self.popup.dismiss()
            self.result_label.text = "Обрабатываем изображение..."

            if not os.path.exists(MODEL_PATH):
                self.result_label.text = "Ошибка: Файл модели не найден!"
                return

            processed_img = preprocess_image(file_path)
            prediction = predict_dish(processed_img)

            # Отладочный вывод предсказанного класса
            print(f"Предсказанный класс: {prediction}")

            dish_name, recipe = get_recipe(prediction)
            self.result_label.text = f"Распознанное блюдо: {dish_name}\nРецепт: {recipe}"


if __name__ == '__main__':
    MainApp().run()
