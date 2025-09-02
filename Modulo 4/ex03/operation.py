from utils import format_cents

class Operation:
    
    def __init__(self, cents: int, description: str):
        if cents == 0:
            raise ValueError("Valor da transicao zerado")
        self.cents: int = cents
        self.operation_type:str = ('credit' if self.cents > 0 else 'debit')
        self.description:str = description
    
    def __str__(self) -> str:
        return f"{format_cents(self.cents)} ({self.description})"
    
    def __repr__(self) -> str:
        return f"Operation(cents={self.cents}, operation_type='{self.operation_type}', description='{self.description}')"