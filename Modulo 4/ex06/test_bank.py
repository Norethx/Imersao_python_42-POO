import pytest
from bank import Bank
from account import Account
from utils import InsufficientBalance, AccountNotRegisterError

def test_value_greater_cash() -> None:
    """testing withdraw with value greater of the account"""
    bank = Bank()
    p1 = Account(22, "000.000.000-01")
    p2 = Account(23, "000.000.000-02")
    bank.add_account(p1)
    bank.add_account(p2)
    with pytest.raises(InsufficientBalance, match="Valor de transação > que saldo"):
        bank.transfer(22, 23, 1000, "test")

def test_not_exists_account() -> None:
    """testing withdraw with account not exists"""
    bank = Bank()
    p1 = Account(22, "000.000.000-01")
    bank.add_account(p1)
    with pytest.raises(AccountNotRegisterError, match="Conta nao cadastrada"):
        bank.transfer(3, 22, 1000, "test")
    
        
def test_transfer() -> None:
    """testing transfer"""
    bank = Bank()
    p1 = Account(22, "000.000.000-01")
    p2 = Account(23, "000.000.000-02")
    bank.add_account(p1)
    bank.add_account(p2)
    bank[22].deposit(1000000, "teste1")
    bank.transfer(22, 23, 1000, "test2")
    assert bank[23]._Account__balance == 1000