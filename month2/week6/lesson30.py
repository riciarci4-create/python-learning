"""Урок 30: объединение таблиц через merge в pandas."""

from pathlib import Path

import pandas as pd


lesson_dir = Path(__file__).resolve().parent
readings_path = lesson_dir / "machine_readings.csv"
catalog_path = lesson_dir / "machine_catalog.csv"

readings = pd.read_csv(readings_path)
machine_catalog = pd.read_csv(catalog_path)

print(readings)
print(machine_catalog)

inner_result = readings.merge(
    machine_catalog,
    on="machine_id",
    how="inner",
)
print(inner_result)
print(inner_result.shape)

left_result = readings.merge(
    machine_catalog,
    on="machine_id",
    how="left",
    indicator=True,
    validate="many_to_one",
)
print(left_result)
print(left_result.shape)

missing_catalog_report = left_result.loc[
    left_result["_merge"] == "left_only",
    ["machine_id", "temperature", "_merge"],
]
print(missing_catalog_report)
print(missing_catalog_report.shape)
