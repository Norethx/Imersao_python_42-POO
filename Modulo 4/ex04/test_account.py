import pytest
from utils import format_cents
from account import Account


testdata = [
    (1, '000.000.000-01',"Account(1, '000.000.000-01')"    ),
    (2, '000.000.000-02',"Account(2, '000.000.000-02')"    ),
    (3, '000.000.000-03',"Account(3, '000.000.000-03')"    ),
    (4, '000.000.000-04',"Account(4, '000.000.000-04')"    ),
    (5, '000.000.000-05',"Account(5, '000.000.000-05')"    ),
    (6, '000.000.000-06',"Account(6, '000.000.000-06')"    ),
    (7, '000.000.000-07',"Account(7, '000.000.000-07')"    ),
    (8, '000.000.000-08',"Account(8, '000.000.000-08')"    ),
    (9, '000.000.000-09',"Account(9, '000.000.000-09')"    )
]

testdat2 = [
    (1, '000.000.000-01',"Account: 1\nBalance: [-] R$ 0,00"    ),
    (2, '000.000.000-02',"Account: 2\nBalance: [-] R$ 0,00"    ),
    (3, '000.000.000-03',"Account: 3\nBalance: [-] R$ 0,00"    ),
    (4, '000.000.000-04',"Account: 4\nBalance: [-] R$ 0,00"    ),
    (5, '000.000.000-05',"Account: 5\nBalance: [-] R$ 0,00"    ),
    (6, '000.000.000-06',"Account: 6\nBalance: [-] R$ 0,00"    ),
    (7, '000.000.000-07',"Account: 7\nBalance: [-] R$ 0,00"    ),
    (8, '000.000.000-08',"Account: 8\nBalance: [-] R$ 0,00"    ),
    (9, '000.000.000-09',"Account: 9\nBalance: [-] R$ 0,00"    )
]

# testdat3 = [
#     (1, '000.000.000-01',    ),
#     (2, '000.000.000-02',    ),
#     (3, '000.000.000-03',    ),
#     (4, '000.000.000-04',    ),
#     (5, '000.000.000-05',    ),
#     (6, '000.000.000-06',    ),
#     (7, '000.000.000-07',    ),
#     (8, '000.000.000-08',    ),
#     (9, '000.000.000-09',    )
# ]

# testdat4 = [
#     (1, '000.000.000-01',    ),
#     (2, '000.000.000-02',    ),
#     (3, '000.000.000-03',    ),
#     (4, '000.000.000-04',    ),
#     (5, '000.000.000-05',    ),
#     (6, '000.000.000-06',    ),
#     (7, '000.000.000-07',    ),
#     (8, '000.000.000-08',    ),
#     (9, '000.000.000-09',    )
# ]

# testdat5 = [
#     (0, "Debito Urubu do Pix"),
#     (0, "Credito Urubu do Pix"),
# ]



@pytest.mark.parametrize("id, cpf, expected", testdata)
def test_account_repr(id: int, cpf: str, expected: str) -> None:
    """test __repr__"""
    p = Account(id, cpf)
    assert expected == p.__repr__()
    
@pytest.mark.parametrize("id, cpf, expected", testdat2)
def test_account_print(id: int, cpf: str, expected: str) -> None:
    """test __str__"""
    p = Account(id, cpf)
    result:str = str(p)
    assert expected == result
    
# @pytest.mark.parametrize("id, cpf , expected", testdat2)
# def test_account_withdraw(id: int, cpf: str, expected: str) -> None:
#     """test __str__"""
#     p = Account(id, cpf)
#     result:str = str(p)
#     assert expected == result

# @pytest.mark.parametrize("id, cpf , expected", testdat2)
# def test_account_deposit(id: int, cpf: str, expected: str) -> None:
#     """test __str__"""
#     p = Account(id, cpf)
#     result:str = str(p)
#     assert expected == result

# @pytest.mark.parametrize("num, desc", testdat3)
# def test_cents_zero(num: int, desc: str) -> None:
#     """testing cents with zero function"""
#     with pytest.raises(ValueError, match="Valor da transicao zerado"):
#         p = Operation(num, desc)