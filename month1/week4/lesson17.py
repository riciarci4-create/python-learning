from pathlib import Path
from PIL import Image


class ImageLoader:
    def __init__(self, image_path):
        self.image_path = Path(image_path)
        self.image = None

    def show_path(self):
        print(self.image_path)

    def exists(self):
        return self.image_path.exists()

    def load(self):
        if not self.exists():
            return False
        self.image = Image.open(self.image_path)
        return True

    def get_info(self):
        if self.image is None:
            return None
        return self.image.format, self.image.size, self.image.mode

    def is_loaded(self):
        if self.image is None:
            return False
        else:
            return True

    def get_size(self):
        if self.image is None:
            return None
        else:
            return self.image.size

    def get_area(self):
        if self.image is None:
            return None
        width, height = self.image.size
        return width * height

    def is_large(self):
        if self.image is None:
            return False
        if self.get_area() > 10000:
            return True
        else:
            return False

    def get_summary(self):
        if self.image is None:
            return "Image is not loaded"
        return (f"Format: {self.image.format}, "
                f"size: {self.get_size()}, "
                f"area: {self.get_area()}, "
                f"large: {self.is_large()}")


loader = ImageLoader("assets/test_image.png")
loader2 = ImageLoader("assets/other.png")
if loader.exists():
    print("Файл найден")
else:
    print("Файл не найден")
loader.show_path()
loader2.show_path()
print(loader.is_loaded())
print(loader.load())
info = loader.get_info()
if info is None:
    print("Изображение не загружено")
else:
    image_format, image_size, image_mode = info
    print(f"Формат: {image_format}")
    print(f"Размер: {image_size}")
    print(f"Режим: {image_mode}")
print(loader.is_loaded())
print(loader.get_size())
print(loader.get_area())
print(loader.is_large())
print(loader.get_summary())
