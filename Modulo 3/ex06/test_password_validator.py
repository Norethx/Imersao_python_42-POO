from password_validator import is_valid_password
import pytest

testdata = [
    (("B@rrig@V4zi4"), True),  # senha correta
    (("teste"), False),  # senha correta
    (("teste11111"), False),  # senha teste apenas lower e digit
    (("teste@@@@@"), False),  # senha teste apenas lower e special
    (("Testeeeeee"), False),  # senha teste apenas lower e Upper
    (("Born2beR@@t"), True),  # senha correta
    (("Welcome to the family"), False),  #
    (("Born2beR@@t "), False),  # senha com espaco
    (("A@1asbflkworkfil"), True),  # senha com 16
    (("A@1asbflkworkfioooo"), False),  # senha maior que 16
]


@pytest.mark.parametrize("given, expected", testdata)
def test_password_invalid(given: str, expected: bool) -> None:
    """make a test of valid_password"""
    result = is_valid_password(given)
    assert expected == result
