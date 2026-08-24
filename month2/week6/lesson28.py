"""Урок 28: условная фильтрация и булевы маски в pandas."""

from pathlib import Path

import pandas as pd


lesson_dir = Path(__file__).resolve().parent
csv_path = lesson_dir / "machine_readings.csv"
readings = pd.read_csv(csv_path)

print(readings)

high_temperature_mask = readings["temperature"] >= 85
print(high_temperature_mask)

high_temperature_machines = readings[high_temperature_mask]
print(high_temperature_machines)
print(high_temperature_machines.shape)

high_temperature_report = readings.loc[
    high_temperature_mask,
    ["machine_id", "temperature"]
]
print(high_temperature_report)
print(high_temperature_report.shape)

warm_running_mask = (readings["temperature"] >= 75) & (readings["is_running"])
print(warm_running_mask)

warm_running_report = readings.loc[
    warm_running_mask,
    ["machine_id", "temperature", "is_running"]
]
print(warm_running_report)
print(warm_running_report.shape)

attention_mask = (readings["temperature"] < 70) | (~readings["is_running"])
attention_report = readings.loc[
    attention_mask,
    ["machine_id", "temperature", "is_running"]
]
print(attention_mask)
print(attention_report)
print(attention_report.shape)

no_match_mask = readings["temperature"] > 100
no_match_report = readings.loc[
    no_match_mask,
    ["machine_id", "temperature"]
]
print(no_match_mask)
print(no_match_report)
print(no_match_report.shape)
print(no_match_report.empty)

requires_attention_mask = (
    (readings["temperature"] >= 85)
    | (readings["is_running"] & (readings["rpm"] < 1300))
)
requires_attention_report = readings.loc[
    requires_attention_mask,
    ["machine_id", "temperature", "rpm", "is_running"]
]
print(requires_attention_mask)
print(requires_attention_report)
print(requires_attention_report.shape)
