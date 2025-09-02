from enum import Enum

def format_cents(valor: int) -> str:
    return f"[{('+' if valor > 0 else '-')}] R$ {int(abs(valor)/100):_},{(abs(valor)%100):02}".replace('_','.')


class InsufficientBalance(Exception):
    pass

class OperationType(Enum):
    credit = 1
    debit = 2