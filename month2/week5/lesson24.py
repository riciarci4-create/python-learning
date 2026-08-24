from pathlib import Path

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

project_root = Path(__file__).resolve().parent.parent.parent
print(project_root)

image_path = project_root / "assets" / "test_image.png"
print(image_path)
print(image_path.exists())

with Image.open(image_path) as image:
    image_array = np.array(image)
    grayscale_array = np.array(image.convert("L"))
    print(image.format)
    print(image.size)
    print(image.mode)

print(image_array.shape)
print(image_array.ndim)
print(image_array.dtype)
print(image_array[0, 0])
print(image_array[50, 100])
print(grayscale_array.shape)
print(grayscale_array.ndim)
print(grayscale_array[0, 0])

plt.imshow(image_array)
plt.title("Тестовое изображение")
plt.axis("off")
plt.show()

column_brightness = grayscale_array.mean(axis=0)
print(column_brightness.shape)
print(column_brightness.min())
print(column_brightness.max())

plt.plot(column_brightness)
plt.title("Средняя яркость по столбцам")
plt.xlabel("Номер столбца")
plt.ylabel("Яркость")
plt.show()

defect_image = grayscale_array.copy()
defect_image[:, 90:110] = 0
print(grayscale_array[50, 100])
print(defect_image[50, 100])

defect_profile = defect_image.mean(axis=0)
plt.plot(defect_profile)
plt.title("Профиль яркости с дефектом")
plt.xlabel("Номер столбца")
plt.ylabel("Яркость")
plt.show()
