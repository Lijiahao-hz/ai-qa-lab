import pytest

from calc import add, subtract, divide, is_valid_password


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_number():
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6


def test_divide_normal():
    assert divide(9, 3) == 3
    
def test_divide_negative():
   assert divide(-6, 3) == -2


def test_divide_by_zero_should_raise():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_password_too_short():
    assert is_valid_password("abc123") is False


def test_password_all_digits():
    assert is_valid_password("12345678") is False


def test_password_valid():
    assert is_valid_password("abc12345") is True

def test_password_boundary():
    assert is_valid_password("abc1234") is False


