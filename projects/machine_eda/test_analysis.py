"""Tests for the machine EDA calculation functions."""
import pandas as pd
from analysis import calculate_failure_percent
from analysis import calculate_region_percent


sample = pd.DataFrame({
    "Machine failure": [0, 1, 0, 0]
})

def test_calculate_failure_percent():
    result = calculate_failure_percent(sample)
    assert result == 25.0


def test_failure_percent_without_failures():
    sample = pd.DataFrame({
    "Machine failure": [0, 0, 0]
    })
    result = calculate_failure_percent(sample)
    assert result == 0.0


def test_failure_percent_empty_data():
    sample = pd.DataFrame({
        "Machine failure": []
    })
    result = calculate_failure_percent(sample)
    assert result is None


def test_failure_percent_three_of_five():
    sample = pd.DataFrame({
    "Machine failure": [1, 0, 1, 1, 0]
    })
    result = calculate_failure_percent(sample)
    assert result == 60


def test_region_percent_strict_boundaries():
    sample = pd.DataFrame({
        "Rotational speed [rpm]": [1400, 1500, 1400, 1600],
        "Torque [Nm]": [60, 60, 50, 40]
    })
    result = calculate_region_percent(sample)
    assert result == 25


def test_region_percent_no_matches():
    sample = pd.DataFrame({
        "Rotational speed [rpm]": [1500, 1700],
        "Torque [Nm]": [50, 40]
    })
    result = calculate_region_percent(sample)
    assert result == 0.0


def test_region_percent_none():
    sample = pd.DataFrame({
        "Rotational speed [rpm]": [],
        "Torque [Nm]": []
    })
    result = calculate_region_percent(sample)
    assert result is None
