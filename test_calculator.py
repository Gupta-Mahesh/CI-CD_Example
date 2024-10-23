import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    assert add(3, 5) == 8


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(4, 2) == 8


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)


