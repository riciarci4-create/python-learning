import pandas as pd
TEMPERATURE_THRESHOLD = 120

machine_data = {
    "machine_id":["CNC-01", "CNC-02", "CNC-03", "CNC-04", "CNC-05"],
    "temperature":[72.0, None, 91.5, 350.0, 74.0],
    "rpm":[1200, 1450, None, 1700, 1300],
    "is_running":[True, True, False, True, None],
}
machine_readings = pd.DataFrame(machine_data)
print(machine_readings)

missing_by_column = machine_readings.isna().sum()
print(missing_by_column)

missing_mask = machine_readings.isna().any(axis=1)
rows_with_missing = machine_readings.loc[missing_mask]
print(rows_with_missing)
print(missing_mask)

temperature_available = machine_readings.dropna(subset=["temperature"])
print(temperature_available)

temperature_mean = machine_readings["temperature"].mean()
temperature_median = machine_readings["temperature"].median()
print(temperature_mean)
print(temperature_median)

cleaned_data = machine_readings.copy()
cleaned_data["temperature_was_missing"] = machine_readings["temperature"].isna()
print(cleaned_data)

cleaned_data["temperature"] = cleaned_data["temperature"].fillna(temperature_median)
print(cleaned_data)
print(cleaned_data.isna().sum())

cleaned_data["temperature_outlier"] = cleaned_data["temperature"] > TEMPERATURE_THRESHOLD
outlier_report = cleaned_data.loc[
    cleaned_data["temperature_outlier"]
]
print(outlier_report)

quality_report = {}
quality_report["total_rows"] = cleaned_data.shape[0]
quality_report["rows_with_missing"] = rows_with_missing.shape[0]
quality_report["temperature_filled"] = cleaned_data["temperature_was_missing"].sum()
quality_report["temperature_outliers"] = cleaned_data["temperature_outlier"].sum()
quality_report["unresolved_missing_cells"] = cleaned_data.isna().sum().sum()
print(quality_report)

quality_report_frame = pd.DataFrame([quality_report])
print(quality_report_frame)
