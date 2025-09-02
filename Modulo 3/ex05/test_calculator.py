import calculator
import pytest


def test_add() -> None:
    """testing add function"""
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0


def test_subtract() -> None:
    """testing subtract function"""
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(10, 15) == -5


def test_multiply() -> None:
    """testing multiply function"""
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10


def test_divide() -> None:
    """testing divide function"""
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(9, 4) == 2.25


def test_divide_by_zero() -> None:
    """testing divide_by_zero function"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)


def test_power() -> None:
    """testing power function"""
    assert calculator.power(10, -2) == 0.01
    assert calculator.power(2, 2) == 4
    assert calculator.power(2, -2) == 0.25
    assert calculator.power(2, 10) == 1024


def test_mixed() -> None:
    """testing mixed function"""
    assert calculator.add(42, 1) == 43
    assert calculator.subtract(1000, 1000) == 0
    assert calculator.multiply(6, 100) == 600
    assert calculator.divide(120, 20) == 6.0
    assert calculator.power(2, 3) == 8
