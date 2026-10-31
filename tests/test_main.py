
import pytest
from datetime import datetime
from src.main import calculate_waiting_time


def test_normal_waiting_time():
    arrival = datetime(2026, 10, 20, 8, 5)
    assessment = datetime(2026, 10, 20, 8, 20)

    assert calculate_waiting_time(arrival, assessment) == 15


def test_assessment_before_arrival():
    arrival = datetime(2026, 10, 20, 8, 20)
    assessment = datetime(2026, 10, 20, 8, 5)

    with pytest.raises(ValueError):
        calculate_waiting_time(arrival, assessment)


def test_zero_waiting_time():
    arrival = datetime(2026, 10, 20, 8, 5)
    assessment = datetime(2026, 10, 20, 8, 5)

    assert calculate_waiting_time(arrival, assessment) == 0

