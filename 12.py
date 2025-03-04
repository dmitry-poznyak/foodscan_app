import tensorflow_datasets as tfds

dataset, info = tfds.load("food101", split="train", with_info=True, as_supervised=True)

# Выводим список классов (названий блюд)
print(info.features["label"].names)
