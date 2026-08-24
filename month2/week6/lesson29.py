"""Урок 29: группировка и агрегирование данных в pandas."""

from pathlib import Path

import pandas as pd


lesson_dir = Path(__file__).resolve().parent
csv_path = lesson_dir / "machine_readings.csv"
readings = pd.read_csv(csv_path)

print(readings)

mean_temperature_by_status = readings.groupby("is_running")["temperature"].mean()
print(mean_temperature_by_status)
print(type(mean_temperature_by_status))
print(mean_temperature_by_status.shape)
print(mean_temperature_by_status.index)

mean_temperature_table_by_status = (
    readings.groupby("is_running", as_index=False)
    ["temperature"].mean()
)
print(mean_temperature_table_by_status)
print(type(mean_temperature_table_by_status))
print(mean_temperature_table_by_status.shape)
print(mean_temperature_table_by_status.columns)
print(mean_temperature_table_by_status.index)

machine_count_by_status = readings.groupby("is_running").size()
print(machine_count_by_status)
print(type(machine_count_by_status))
print(machine_count_by_status.shape)

max_rpm_by_status = readings.groupby("is_running")["rpm"].max()
print(max_rpm_by_status)

status_summary = readings.groupby("is_running", as_index=False).agg(
    machine_count=("machine_id", "size"),
    mean_temperature=("temperature", "mean"),
    max_rpm=("rpm", "max"),
)
print(status_summary)
print(type(status_summary))
print(status_summary.shape)
print(status_summary.columns)

readings_with_missing = readings.copy()
print(readings_with_missing)
print(readings)

readings_with_missing.loc[1, "temperature"] = pd.NA
print(readings_with_missing)
print(readings)

row_count_with_missing = readings_with_missing.groupby("is_running").size()
temperature_count_with_missing = (
    readings_with_missing.groupby("is_running")
    ["temperature"].count()
)
print(row_count_with_missing)
print(temperature_count_with_missing)

quality_summary = readings_with_missing.groupby("is_running", as_index=False).agg(
    machine_count=("machine_id", "size"),
    temperature_count=("temperature", "count"),
    mean_temperature=("temperature", "mean"),
)
quality_summary["missing_temperature_count"] = (
    quality_summary["machine_count"]
    - quality_summary["temperature_count"]
)
print(quality_summary)
print(quality_summary.to_string(index=False))
