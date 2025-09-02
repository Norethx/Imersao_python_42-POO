import pytest
from utils import format_cents

testdata = [
    (1000000000, '[+] R$ 10.000.000,00'),
    (-1000000000, '[-] R$ 10.000.000,00'),
    (29, '[+] R$ 0,29'),
    (1, '[+] R$ 0,01'),
    (-1, '[-] R$ 0,01'),
    (25, '[+] R$ 0,25'),
    (-25, '[-] R$ 0,25'),
    (420, '[+] R$ 4,20'),
    (-420, '[-] R$ 4,20'),
]

@pytest.mark.parametrize("number, expected", testdata)
def test_utils(number: int, expected: str) -> None:
    """test of string format"""
    result: str = format_cents(number)
    assert expected == result