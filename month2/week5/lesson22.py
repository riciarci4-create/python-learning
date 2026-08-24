import numpy as np

temperatures = np.array([68, 92, 85, 97, 74])
print(temperatures)

overheat_mask = temperatures > 85
# Ожидаю: [False, True, False, True, False]
print(overheat_mask)

overheat_temperatures = temperatures[overheat_mask]
# ожидаю: [92, 97]
print(overheat_temperatures)

min_temperature = temperatures.min()
max_temperature = temperatures.max()
mean_temperature = temperatures.mean()
print(f"Минимальная температура: {min_temperature}")
print(f"Максимальная температура: {max_temperature}")
print(f"Средняя температура: {mean_temperature}")

mean_overheat_temperature = overheat_temperatures.mean()
print(f"Среднее значение высоких температур: {mean_overheat_temperature}")

machine_data = np.array([
    [1, 68, 1200],
    [2, 92, 1500],
    [3, 85, 1400],
    [4, 97, 1700],
    [5, 74, 1300],
])
print(machine_data)

machine_temperatures = machine_data[:, 1]
print(machine_temperatures)

critical_mask = machine_temperatures > 85
print(critical_mask)

critical_machines = machine_data[critical_mask]
print(critical_machines)

critical_count = critical_mask.sum()
print(f"Количество станков с критической температурой: {critical_count}")
print(critical_machines.shape)

if critical_count > 0:
    mean_critical_temperature = critical_machines[:, 1].mean()
    print(f'Среднее значение критической температуры: {mean_critical_temperature}')
else:
    print("Критические станки не обнаружены")
