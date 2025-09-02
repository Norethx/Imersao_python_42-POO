from typing import Any


def add(num1: int, num2: int) -> int:
    """sum value 1 with value 2"""
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    """subtract value 1 with value 2"""
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    """multiply value 1 with value 2"""
    return num1 * num2


def divide(num1: int, num2: int) -> float:
    """divide value 1 with value 2"""
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2


def power(base: int, expoent: int) -> Any:
    """divide value 1 with value 2"""
    return base**expoent
