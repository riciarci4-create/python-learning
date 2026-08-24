"""Урок 27: выбор строк и столбцов через loc и iloc."""

from pathlib import Path

import pandas as pd


# Практика урока
# 1. Загрузка журнала станков из CSV.
# 2. Выбор столбцов по именам.
# 3. Выбор строк и ячеек через loc.
# 4. Выбор строк и ячеек через iloc.
# 5. Инженерное извлечение нужного фрагмента таблицы.

lesson_dir = Path(__file__).resolve().parent
csv_path = lesson_dir / "machine_readings.csv"
readings = pd.read_csv(csv_path)
print(readings)
print(readings.columns)
print(readings.index)

only_temperature = readings["temperature"]
machine_id_and_rpm = readings[["machine_id", "rpm"]]
print(type(only_temperature))
print(only_temperature.shape)
print(type(machine_id_and_rpm))
print(machine_id_and_rpm.shape)
print(only_temperature)
print(machine_id_and_rpm)

cnc_03_temperature = readings.loc[2, "temperature"]
selected_machine_temperatures = readings.loc[1:3, ["machine_id", "temperature"]]
print(cnc_03_temperature)
print(selected_machine_temperatures)

selected_machine_rpm = readings.iloc[1:3, [0, 2]]
print(selected_machine_rpm)

readings_by_machine = readings.set_index("machine_id")
cnc_03_by_machine = readings_by_machine.loc[
    "CNC-03",
    ["temperature", "rpm", "is_running"]
]
print(readings_by_machine)
print(readings_by_machine.index)
print(cnc_03_by_machine)
print(cnc_03_by_machine.ndim)
print(type(cnc_03_by_machine))
print(cnc_03_by_machine.shape)
