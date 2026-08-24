import numpy as np


temperatures = np.array([70, 72, 74, 73, 71, 98], dtype=float)
mean_temperature = temperatures.mean()
print(f"Среднее значение температуры: {mean_temperature}")

median_temperature = np.median(temperatures)
print(f"Медианное значение температуры: {median_temperature}")

temperature_range = temperatures.max() - temperatures.min()
print(f"Диапазон температур: {temperature_range}")

standard_deviation = np.std(temperatures)
print(f"Стандартное отклонение температуры: {standard_deviation}")

candidate_temperature = 98
z_score = (candidate_temperature - mean_temperature) / standard_deviation
print(f"z-score показатель по всем данным: {z_score}")

baseline_temperatures = temperatures[:-1]
print(f"Базовый массив: {baseline_temperatures}")

baseline_mean = baseline_temperatures.mean()
baseline_std = np.std(baseline_temperatures)
print(f"Средняя базовая величина: {baseline_mean}")
print(f"Стандартное отклонение базовой линии: {baseline_std}")

if baseline_std != 0:
    clean_z_score = (candidate_temperature - baseline_mean) / baseline_std
    print(f"z-score показатель по чистой базовой линии: {clean_z_score}")
else:
    print("z-score невозможно вычислить так как отклонение равно 0")


def calculate_z_score(baseline_values, candidate_value):
    if baseline_values.size == 0:
        return None
    mean_value = baseline_values.mean()
    std_value = baseline_values.std()
    if std_value == 0:
        return None
    return (candidate_value - mean_value) / std_value


empty_baseline = np.array([], dtype=float)
constant_baseline = np.array([72, 72, 72], dtype=float)
analysis_z_score = calculate_z_score(baseline_temperatures, candidate_temperature)
empty_analysis_z_score = calculate_z_score(empty_baseline, 80)
constant_analysis_z_score = calculate_z_score(constant_baseline, 80)
print(f"Значение при нормальной базе: {analysis_z_score}")
print(f"Значение при постоянной базе: {constant_analysis_z_score}")
print(f"Значение при пустой базе: {empty_analysis_z_score}")
