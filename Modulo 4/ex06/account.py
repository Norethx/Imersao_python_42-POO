from operation import Operation
from utils import format_cents, InsufficientBalance

class Account:
    def __init__(self, account_id: int, cpf: str):
        """Builder of class account"""
        self.account_id = account_id
        self.cpf = cpf
        self.__balance:int = 0
        self.__operations: list[Operation] = []
    
    def deposit(self, amount: int, description: str) -> None:
        """add balance of the account"""
        if amount == 0:
            raise ValueError("valor deve ser > 0")
        self.__balance += amount
        self.__operations.append(Operation(amount, description))
        
    def withdraw(self, amount: int, description: str) -> None:
        """remove balance of the account"""
        if amount > self.__balance:
            raise InsufficientBalance("Valor de transação > que saldo")
        if amount == 0:
            raise ValueError("valor deve ser > 0")
        self.__balance -= amount
        self.__operations.append(Operation((amount * -1), description))            
            
    def statement(self) -> None:
        """history and balance of account"""
        for x in self.__operations:
            print(x)
        print(f"Balance: {format_cents(self.__balance)}")
    
    def __str__(self)-> str:
        """String formart of class"""
        return (f"Account: {self.account_id}\nBalance: {format_cents(self.__balance)}")
    
    def __repr__(self)-> str:
        """representation of class"""
        return (f"Account({self.account_id}, '{self.cpf}')")