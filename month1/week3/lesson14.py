from pathlib import Path

script_path = Path(__file__)
script_dir = script_path.parent
project_root = script_dir.parent.parent
root_log_path = project_root / "machine_log.txt"
print(f"Путь к логу: {root_log_path}")
print(f"Файл существует: {root_log_path.exists()}")
try:
    with open(root_log_path, encoding="utf-8") as log_file:
        line_count = 0
        for log_line in log_file:
            line_count = line_count + 1
        print(f"Всего строк: {line_count}")
except FileNotFoundError:
    print("Файл не найден")
