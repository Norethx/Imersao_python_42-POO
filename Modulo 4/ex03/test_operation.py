import pytest
from utils import format_cents
from operation import Operation

testdata = [
    (1000000000, 'Credito Urubu do Pix',"Operation(cents=1000000000, operation_type='credit', description='Credito Urubu do Pix')"),
    (-1000000000, 'Debito Tigrin',"Operation(cents=-1000000000, operation_type='debit', description='Debito Tigrin')"),
    (29, 'Credito Urubu do Pix',"Operation(cents=29, operation_type='credit', description='Credito Urubu do Pix')"),
    (1, 'Credito Urubu do Pix',"Operation(cents=1, operation_type='credit', description='Credito Urubu do Pix')"),
    (-1, 'Debito Tigrin',"Operation(cents=-1, operation_type='debit', description='Debito Tigrin')"),
    (25, 'Credito Urubu do Pix',"Operation(cents=25, operation_type='credit', description='Credito Urubu do Pix')"),
    (-25, 'Debito Tigrin',"Operation(cents=-25, operation_type='debit', description='Debito Tigrin')"),
    (420, 'Credito Urubu do Pix',"Operation(cents=420, operation_type='credit', description='Credito Urubu do Pix')"),
    (-420, 'Debito Tigrin',"Operation(cents=-420, operation_type='debit', description='Debito Tigrin')")
]

testdat2 = [
    (1000000000, "Credito Urubu do Pix","[+] R$ 10.000.000,00 (Credito Urubu do Pix)"),
    (-1000000000, 'Debito Tigrin','[-] R$ 10.000.000,00 (Debito Tigrin)'),
    (29, 'Credito Urubu do Pix','[+] R$ 0,29 (Credito Urubu do Pix)'),
    (1, 'Credito Urubu do Pix','[+] R$ 0,01 (Credito Urubu do Pix)'),
    (-1, 'Debito Tigrin','[-] R$ 0,01 (Debito Tigrin)'),
    (25, 'Credito Urubu do Pix','[+] R$ 0,25 (Credito Urubu do Pix)'),
    (-25, 'Debito Tigrin','[-] R$ 0,25 (Debito Tigrin)'),
    (420, 'Credito Urubu do Pix','[+] R$ 4,20 (Credito Urubu do Pix)'),
    (-420, 'Debito Tigrin','[-] R$ 4,20 (Debito Tigrin)')
]

testdat3 = [
    (0, "Debito Urubu do Pix"),
    (0, "Credito Urubu do Pix"),
]



@pytest.mark.parametrize("value, description, expected", testdata)
def test_operation_repr(value: int, description: str, expected: str) -> None:
    """test __repr__"""
    p = Operation(value, description)
    assert expected == p.__repr__()
    
@pytest.mark.parametrize("num, desc , expected", testdat2)
def test_operation_print(num: int, desc: str, expected: str) -> None:
    """test __str__"""
    p = Operation(num, desc)
    result:str = str(p)
    assert expected == result

@pytest.mark.parametrize("num, desc", testdat3)
def test_cents_zero(num: int, desc: str) -> None:
    """testing cents with zero function"""
    with pytest.raises(ValueError, match="Valor da transicao zerado"):
        p = Operation(num, desc)