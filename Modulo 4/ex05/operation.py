from utils import format_cents,OperationType

class Operation:
    def __init__(self, cents: int, description: str):
        """Builder of class Operation"""
        if cents == 0:
            raise ValueError("Valor da transicao zerado")
        self.cents: int = cents
        self.operation_type:OperationType = (OperationType.credit if self.cents > 0 else OperationType.debit)
        self.description:str = description
    
    def __str__(self) -> str:
        """string formart of class"""
        return f"{format_cents(self.cents)} ({self.description})"
    
    def __repr__(self) -> str:
        """represation of class"""
        return f"Operation(cents={self.cents}, operation_type='{self.operation_type.name}', description='{self.description}')"