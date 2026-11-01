"""Exploratory analysis of the UCI AI4I 2020 dataset."""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def load_readings(csv_path):
    return pd.read_csv(csv_path)


def calculate_failure_percent(readings):
    machine_failure = readings.groupby("Machine failure").size()
    if machine_failure.sum() == 0:
        return None
    else:
        failure_procent = (machine_failure.get(1, 0)) / (machine_failure.sum()) * 100
        return failure_procent


def calculate_region_percent(group):
    if group.shape[0] == 0:
        return None
    else:
        failures_in_region = group.loc[
            (group["Rotational speed [rpm]"] < 1500) & (group["Torque [Nm]"] > 50)
        ]
        failure_region_percent = ((failures_in_region.shape[0]) / (group.shape[0])) * 100
        return failure_region_percent


def build_group_summary(readings):
    summary_report = readings.groupby("Machine failure", as_index=False).agg(
        record_count=("UDI", "size"),
        mean_wear=("Tool wear [min]", "mean"),
        median_wear=("Tool wear [min]", "median"),
        mean_torque =("Torque [Nm]", "mean"),
        median_torque =("Torque [Nm]", "median"),
        mean_rotational_speed =("Rotational speed [rpm]", "mean"),
        median_rotational_speed =("Rotational speed [rpm]", "median")
    )
    return summary_report


def plot_wear_distribution(wear_without_failure, wear_with_failure, image_path):
    if wear_without_failure.size == 0 and wear_with_failure.size == 0:
        print("Нет данных для графика")
        return

    plt.figure()
    if wear_without_failure.size == 0:
        print("Пустая группа")
    else:
        weights_without_failure = [100 / wear_without_failure.size ] * wear_without_failure.size
        plt.hist(
            wear_without_failure,
            bins=[0, 50, 100, 150, 200, 250, 300],
            weights=weights_without_failure,
            alpha=0.5,
            histtype="step",
            label="Группа без отказов"
        )
    if wear_with_failure.size == 0:
        print("Пустая группа")
    else:
        weights_with_failure = [100 / wear_with_failure.size ] * wear_with_failure.size
        plt.hist(
            wear_with_failure,
            bins=[0, 50, 100, 150, 200, 250, 300],
            weights=weights_with_failure,
            alpha=0.5,
            label="Группа отказов"
        )
    plt.xlabel("Износ инструмента, мин")
    plt.ylabel("Доля записей внутри группы, %")
    plt.title("Распределение износа инструмента по признаку отказа")
    plt.legend()
    plt.savefig(image_path, dpi=150, bbox_inches="tight")
    plt.show()


def plot_speed_torque(without_failure, with_failure, image_path):
    plt.figure()
    plt.scatter(
        without_failure["Rotational speed [rpm]"],
        without_failure["Torque [Nm]"],
        color="blue",
        alpha=0.3,
        s=5,
        label="Группа без отказа"
    )
    plt.scatter(
        with_failure["Rotational speed [rpm]"],
        with_failure["Torque [Nm]"],
        color="orange",
        alpha=0.3,
        s=5,
        label="Группа c отказом"
    )
    plt.xlabel("Обороты, об/мин")
    plt.ylabel("Крутящий момент, Н·м")
    plt.title("Обороты и крутящий момент")
    plt.legend()
    plt.savefig(image_path, dpi=150, bbox_inches="tight")
    plt.show()


def main():

    lesson_directory = Path(__file__).resolve().parent
    database_path = lesson_directory / "data/raw/ai4i2020.csv"

    readings = load_readings(database_path)

    failure_procent = calculate_failure_percent(readings)

    tool_wear_range_max = readings.groupby("Machine failure")["Tool wear [min]"].max()
    tool_wear_range_min = readings.groupby("Machine failure")["Tool wear [min]"].min()
    tool_wear_range = (tool_wear_range_max) - (tool_wear_range_min)
    wear_without_failure = readings.loc[
        readings["Machine failure"] == 0,
        "Tool wear [min]"
    ]
    wear_with_failure =readings.loc[
        readings["Machine failure"] == 1,
        "Tool wear [min]"
    ]
    first_image_path = lesson_directory / "wear_distribution.png"

    plot_wear_distribution(
        wear_without_failure,
        wear_with_failure,
        first_image_path
    )

    print(f'Процент отказа: {failure_procent}')
    print(readings.shape)
    print(readings.columns)
    print(type(readings))
    print(readings.head(5))
    print(readings.dtypes)
    print(f'Количество пропусков по столбцам: {readings.isna().sum()}')
    print(f'Количество полностью повторяющихся строк: {readings.duplicated().sum()}')
    print(f'Количество повторов UDI: {readings["UDI"].duplicated().sum()}')
    print(f'Минимальная температура воздуха [K]: {readings["Air temperature [K]"].min()}')
    print(f'Максимальная температура воздуха [K]: {readings["Air temperature [K]"].max()}')
    print(f'Минимальные обороты [об/мин]: {readings["Rotational speed [rpm]"].min()}')
    print(f'Максимальные обороты [об/мин]: {readings["Rotational speed [rpm]"].max()}')
    print(f'Минимальный износ инструмента [мин]: {readings["Tool wear [min]"].min()}')
    print(f'Максимальный износ инструмента [мин]: {readings["Tool wear [min]"].max()}')
    print(f'Размах износа, мин: {tool_wear_range}')
    print(f'Количество записей без отказа: {wear_without_failure.size}')
    print(f'Количество записей с отказом: {wear_with_failure.size}')

    without_failure = readings.loc[
        readings["Machine failure"] == 0,
    ]
    with_failure =readings.loc[
        readings["Machine failure"] == 1,
    ]

    with_failure_percent = calculate_region_percent(with_failure)

    without_failure_percent = calculate_region_percent(without_failure)

    scatter_image_path = lesson_directory / "speed_torque_scatter.png"

    plot_speed_torque(without_failure, with_failure, scatter_image_path)

    print(f'Доля записей без отказа в области обороты < 1500 об/мин '
          f'и момент > 50 Н·м: {without_failure_percent}%')
    print(f'Доля записей с отказом в области обороты < 1500 об/мин '
          f'и момент > 50 Н·м: {with_failure_percent}%')

    summary_report = build_group_summary(readings)

    print(summary_report)

    output_path = lesson_directory / "group_summary.csv"
    summary_report.to_csv(output_path, index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    main()
