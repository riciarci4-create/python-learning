from PIL import Image

image = Image.new("RGB", (200, 100), (255, 0, 0))
image.save("assets/test_image.png")
opened_image = Image.open("assets/test_image.png")
width, height = opened_image.size
pixel = opened_image.getpixel((0, 0))
center_x = width // 2
center_y = height // 2
center_pixel = opened_image.getpixel((center_x, center_y))
print(f"Формат: {opened_image.format}\nРазмер: {opened_image.size}\nРежим цвета: {opened_image.mode}")
print(f"Ширина: {width}")
print(f"Высота: {height}")
print(f"Пиксель (0, 0): {pixel}")
print(f"Пиксель в центре ({center_x}, {center_y}): {center_pixel}")