import os

cwd = os.getcwd()
items = os.listdir(cwd)
dir_count = 0
file_count = 0
for item in items:
    item_path = os.path.join(cwd, item)
    if os.path.isdir(item_path):
        dir_count = dir_count + 1
        print(f"[DIR] {item_path}")
    else:
        file_count = file_count + 1
        print(f"[FILE] {item_path}")
print(f"Папок: {dir_count}")
print(f"Файлов: {file_count}")
print(f"Всего элементов: {len(items)}")
