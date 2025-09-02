from operation import Operation
from utils import format_cents

class Account:
    def __init__(self, account_id: int, cpf: str):
        self.account_id = account_id
        self.cpf = cpf
        self.__balance = 0
        self.__operations = []
    
    def deposit(self, amount: int, description: str) -> None:
        if amount == 0:
            raise ValueError("valor deve ser > 0")
        self.__balance += amount
        self.__operations.append(Operation(amount, description))
        
    def withdraw(self, amount: int, description: str) -> None:
        if amount > self.__balance:
            raise ValueError("Valor de transação maior que balanço")
        if amount == 0:
            raise ValueError("valor deve ser > 0")
        self.__balance -= amount
        self.__operations.append(Operation((amount * -1), description))            
            
    def statement(self) -> None:
        for x in self.__operations:
            print(x)
        print("Balance: ",format_cents(self.__balance))
    
    def __str__(self)-> str:
        return (f"Account: {self.account_id}\nBalance: {format_cents(self.__balance)}")
    
    def __repr__(self)-> str:
        return (f"Account({self.account_id}, '{self.cpf}')")