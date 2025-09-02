from account import Account
from utils import SameAccountError, AccountNotRegisterError, InsufficientBalance, AccountAlredyExists

class Bank:
    def __init__(self)->None:
        """Construtor da classe Bank"""
        self.__accounts: list[Account] = []
        
    def __contains__(self, account_id: int) -> bool:
        """Função utilizada quando in é invocado"""
        return any(account for account in self.__accounts if account_id == account.account_id)
    
    def __len__(self) -> int:
        """Função utilizada quando  len é invocado"""
        return len(self.__accounts)
    
    def __getitem__(self, account_id: int) -> Account:
        """Função utilizada quando passado junto a classe '[]'"""
        return [x for x in self.__accounts if x.account_id == account_id][0]
        
    def add_account(self, account: Account)-> None:
        """adiciona uma nova conta ao banco"""
        if any(account1 for account1 in self.__accounts if account1.account_id == account.account_id):
            raise AccountAlredyExists("Conta já existe")
        self.__accounts.append(account)
        
    def get_account_by_cpf(self, cpf: str)-> Account:
        """Se existir uma conta no cpf cadastrado no banco retorna o primeiro"""
        return [x for x in self.__accounts if x.cpf == cpf][0]
        
    def get_account_by_id(self, account_id: int)-> Account:
        """Se existir uma conta com o id retorna o primeiro"""
        return [x for x in self.__accounts if x.account_id == account_id][0]
    
    def transfer(self, source_account: int, destination_account:int, value: int, description: str) -> None:
        """Realiza a transferencia monetaria de de uma conta para outra"""
        source = self.get_account_by_id(source_account)
        dest = self.get_account_by_id(destination_account)
        if source == dest:
            raise SameAccountError("Traferencia para a mesma conta") 
        if source is None or dest is None:
            raise AccountNotRegisterError("Conta nao cadastrada")
        try:
            source.withdraw(value, description)
            dest.deposit(value, description)
        except ValueError:
            raise ValueError("valor deve ser > 0")
        except InsufficientBalance:
            raise InsufficientBalance("Valor de transação > que saldo")
    