import string
from typing import Callable


def min_and_max_lenght(s_str: str) -> bool:
    """Verify lenght of string"""
    return len(s_str) >= 8 and len(s_str) <= 16


def has_uppercase(s_str: str) -> bool:
    """Verify if exist uppercase"""
    return any(c in string.ascii_uppercase for c in s_str)


def has_lowercase(s_str: str) -> bool:
    """Verify if exist lowercase"""
    return any(c in string.ascii_lowercase for c in s_str)


def has_digit(s_str: str) -> bool:
    """Verify if exist digit"""
    return any(c in string.digits for c in s_str)


def has_special_char(s_str: str) -> bool:
    """Verify if exist special char"""
    return any(c in string.punctuation for c in s_str)


def is_hasnt_space(s_str: str) -> bool:
    """Verify if haven't exist special char"""
    return not any(c.isspace() for c in s_str)


def is_valid_password(s_str: str) -> bool:
    """handle verifify password"""
    l_func: list[Callable[[str], bool]] = [
        min_and_max_lenght,
        has_uppercase,
        has_lowercase,
        has_digit,
        has_special_char,
        is_hasnt_space,
    ]
    for func in l_func:
        if not bool(func(s_str)):
            return False
    return True
