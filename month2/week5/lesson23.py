import numpy as np

measurements = np.array([
    [70, 72, 74],
    [80, 82, 84]
])
print(measurements)
print(measurements.shape)

mean_by_machine = measurements.mean(axis=1)
print(f'Среднее значение по строкам: {mean_by_machine}')

mean_by_measurements = measurements.mean(axis=0)
print(f"Среднее значение по столбцам: {mean_by_measurements}")

max_by_machine = measurements.max(axis=1)
print(f"Пиковая температура каждого станка: {max_by_machine}")

machine_metrics = np.array([
    [72, 1500, 2.1],
    [80, 1700, 3.5],
    [76, 1600, 2.8]
])
mean_metrics = machine_metrics.mean(axis=0)
print(f"Среднее значение данных по столбцам: {mean_metrics}")

metric_ranges = machine_metrics.max(axis=0) - machine_metrics.min(axis=0)
print(f'Размах показателей: {metric_ranges}')
