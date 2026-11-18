from enum import Enum


class EvenOrOdd(Enum):
    EVEN = "even"
    ODD = "odd"

def even_or_odd(number: int) -> EvenOrOdd:
    if number % 2 != 0:
        return EvenOrOdd.ODD

    return EvenOrOdd.EVEN
    
