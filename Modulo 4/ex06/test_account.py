import pytest
from _pytest.capture import CaptureFixture
from account import Account
from utils import InsufficientBalance



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

testdat3 = [
    (1, '000.000.000-01', 1000, "[+] R$ 10,00 (deposit test)\nBalance: [+] R$ 10,00\n"   ),
    (2, '000.000.000-02', 1000, "[+] R$ 10,00 (deposit test)\nBalance: [+] R$ 10,00\n"   ),
    (3, '000.000.000-03', 1000, "[+] R$ 10,00 (deposit test)\nBalance: [+] R$ 10,00\n"   ),
    (4, '000.000.000-04', 1000, "[+] R$ 10,00 (deposit test)\nBalance: [+] R$ 10,00\n"   ),
    (5, '000.000.000-05', 1000, "[+] R$ 10,00 (deposit test)\nBalance: [+] R$ 10,00\n"   ),
    (6, '000.000.000-06', 1000, "[+] R$ 10,00 (deposit test)\nBalance: [+] R$ 10,00\n"   ),
    (7, '000.000.000-07', 1000, "[+] R$ 10,00 (deposit test)\nBalance: [+] R$ 10,00\n"   ),
    (8, '000.000.000-08', 1000, "[+] R$ 10,00 (deposit test)\nBalance: [+] R$ 10,00\n"   ),
    (9, '000.000.000-09', 1000, "[+] R$ 10,00 (deposit test)\nBalance: [+] R$ 10,00\n"   )
]



testdat4 = [
    (1, '000.000.000-01', 1000, "[+] R$ 10,00 (deposit test)\n[-] R$ 10,00 (cash test)\nBalance: [-] R$ 0,00\n"   ),
    (2, '000.000.000-02', 1000, "[+] R$ 10,00 (deposit test)\n[-] R$ 10,00 (cash test)\nBalance: [-] R$ 0,00\n"   ),
    (3, '000.000.000-03', 1000, "[+] R$ 10,00 (deposit test)\n[-] R$ 10,00 (cash test)\nBalance: [-] R$ 0,00\n"   ),
    (4, '000.000.000-04', 1000, "[+] R$ 10,00 (deposit test)\n[-] R$ 10,00 (cash test)\nBalance: [-] R$ 0,00\n"   ),
    (5, '000.000.000-05', 1000, "[+] R$ 10,00 (deposit test)\n[-] R$ 10,00 (cash test)\nBalance: [-] R$ 0,00\n"   ),
    (6, '000.000.000-06', 1000, "[+] R$ 10,00 (deposit test)\n[-] R$ 10,00 (cash test)\nBalance: [-] R$ 0,00\n"   ),
    (7, '000.000.000-07', 1000, "[+] R$ 10,00 (deposit test)\n[-] R$ 10,00 (cash test)\nBalance: [-] R$ 0,00\n"   ),
    (8, '000.000.000-08', 1000, "[+] R$ 10,00 (deposit test)\n[-] R$ 10,00 (cash test)\nBalance: [-] R$ 0,00\n"   ),
    (9, '000.000.000-09', 1000, "[+] R$ 10,00 (deposit test)\n[-] R$ 10,00 (cash test)\nBalance: [-] R$ 0,00\n"   )
]

testdat5 = [
    (9, '000.000.000-09', 0)
]

testdat6 = [
    (9, '000.000.000-09', 0)
]

testdat7 = [
    (9, '000.000.000-09', 10)
]

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
    
@pytest.mark.parametrize("id, cpf, value, expected", testdat3)
def test_deposit_print(id: int, cpf: str, value:int, expected: str, capsys: CaptureFixture[str]) -> None:
    """test __deposit__"""
    p = Account(id, cpf)
    p.deposit(value,"deposit test")
    p.statement()
    result = capsys.readouterr()
    assert expected == result.out

@pytest.mark.parametrize("id, cpf, value, expected", testdat4)
def test_withdraw_print(id: int, cpf: str, value:int, expected: str, capsys: CaptureFixture[str]) -> None:
    """test __deposit__"""
    p = Account(id, cpf)
    p.deposit(value,"deposit test")
    p.withdraw(value,"cash test")
    p.statement()
    result = capsys.readouterr()
    assert expected == result.out

@pytest.mark.parametrize("id, cpf, value", testdat5)
def test_value_zero_dp(id: int, cpf: str, value:int) -> None:
    """testing deposit function with zero values"""
    with pytest.raises(ValueError, match="valor deve ser > 0"):
        p = Account(id, cpf)
        p.deposit(value,"deposit test")

@pytest.mark.parametrize("id, cpf, value", testdat6)
def test_value_zero_cash(id: int, cpf: str, value:int) -> None:
    """testing withdraw function with zero values"""
    p = Account(id, cpf)
    with pytest.raises(ValueError, match="valor deve ser > 0"):
        p.deposit(value,"deposit test")

@pytest.mark.parametrize("id, cpf, value", testdat7)
def test_value_greater_cash(id: int, cpf: str, value:int) -> None:
    """testing withdraw with value greater of the account"""
    p = Account(id, cpf)
    with pytest.raises(InsufficientBalance, match="Valor de transação > que saldo"):
        p.withdraw(value,"deposit test")
    
