import numpy as np

spindle_speeds = np.array([1200, 1500, 1800])
print(spindle_speeds.shape,
      spindle_speeds.ndim,
      spindle_speeds.size,
      spindle_speeds.dtype)

machine_data = np.array([
    [72, 1500, 8],
    [75, 1600, 9]
])
print(machine_data.shape,
      machine_data.ndim,
      machine_data.size,
      machine_data.dtype)
print(f'Обороты второй машины: {machine_data[1, 1]}')
print(f'Номер программы первой машины: {machine_data[0, 2]}')

increased_speeds = spindle_speeds + 100
print(f"Увеличенные обороты: {increased_speeds}")
print(f"Исходные обороты: {spindle_speeds}")

all_machine_speeds = machine_data[:, 1]
print(f'Обороты всех машин: {all_machine_speeds}')
print(f'Форма массива оборотов: {all_machine_speeds.shape}')

temperatures = machine_data[:, 0]
calibrated_temperatures = temperatures + 2
print(f"Исходная температура машин: {temperatures}")
print(f"Откалиброванная температура машин: {calibrated_temperatures}")
