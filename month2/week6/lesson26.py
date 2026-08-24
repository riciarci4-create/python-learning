"""Урок 26: введение в pandas и табличные данные."""

import pandas as pd
from pathlib import Path


# Практика урока
# 1. Создание DataFrame из производственных данных.
# 2. Исследование shape, columns, index и dtypes.
# 3. Выбор одного столбца как Series.
# 4. Чтение данных из CSV.
# 5. Инженерная проверка структуры загруженной таблицы.

machine_data = {
    "machine_id": [1, 2, 3],
    "temperature": [70, 71, 72],
    "rpm": [1000, 1100, 1200],
    "is_running": [True, False, True]
}
table = pd.DataFrame(machine_data)
print(table)
print(table.shape)
print(table.dtypes)

temperatures = table["temperature"]
print(type(temperatures))
print(temperatures.shape)
print(temperatures)

project_lesson = Path(__file__).resolve().parent
csv_path = project_lesson / "machine_readings.csv"
readings = pd.read_csv(csv_path)
print(readings)
print(readings.shape)
print(readings.dtypes)

expected_columns = ["machine_id", "temperature", "rpm", "is_running"]
actual_columns = readings.columns.tolist()
columns_are_valid = actual_columns == expected_columns
not_readings_empty = not readings.empty
print(columns_are_valid)
print(not_readings_empty)
