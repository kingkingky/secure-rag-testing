import pytest

from security_analyzer import (
    calculate_asr,
    compare_security
)


def test_calculate_asr():

    data = {
        "total_tests": 200,
        "failed_defense": 20
    }

    assert calculate_asr(data) == 10.0


def test_detect_regression():

    baseline = {
        "Prompt Injection": {
            "total_tests": 100,
            "failed_defense": 2
        }
    }

    current = {
        "Prompt Injection": {
            "total_tests": 100,
            "failed_defense": 8
        }
    }

    result = compare_security(baseline, current)

    assert result["Prompt Injection"]["regression"] is True


def test_no_regression():

    baseline = {
        "Access Control": {
            "total_tests": 100,
            "failed_defense": 5
        }
    }

    current = {
        "Access Control": {
            "total_tests": 100,
            "failed_defense": 5
        }
    }

    result = compare_security(baseline, current)

    assert result["Access Control"]["regression"] is False


def test_invalid_data():

    data = {
        "total_tests": 100,
        "failed_defense": 120
    }

    with pytest.raises(ValueError):
        calculate_asr(data)