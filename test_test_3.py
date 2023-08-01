from test_3 import sum_current_time, check_valid_input
import pytest


def test_valid_time_sum():
    valid_time = '04:06:28'
    assert sum_current_time(valid_time) == 38


def test_valid_time_returns_int():
    valid_time = '04:06:28'
    assert isinstance(sum_current_time(valid_time), int)


def test_valid_input_returns_true_for_valid_input():
    valid_time = '04:06:28'
    assert check_valid_input(valid_time) == True


def test_invalid_input_not_string_raises_type_error():
    invalid_time = 134534
    with pytest.raises(TypeError):
        check_valid_input(invalid_time)


def test_invalid_time_format_colons():
    invalid_time = '05:43'
    with pytest.raises(ValueError):
        check_valid_input(invalid_time)


def test_wrong_string_size_raises_value_error():
    invalid_time = "20:30:10.00"
    with pytest.raises(ValueError):
        check_valid_input(invalid_time)


def test_too_big_an_input_raises_value_error():
    invalid_time = "99:99:99"
    with pytest.raises(ValueError):
        check_valid_input(invalid_time)


def test_not_integers_inputed_raises_value_error():
    invalid_time = "HA:ha:HA"
    with pytest.raises(ValueError):
        check_valid_input(invalid_time)
