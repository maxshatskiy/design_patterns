"""from Aaron Maxwell. a simple class with several constructors. alternate constructor."""
import re
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    @classmethod
    def from_pennies(cls, total_cents):
        dollar = total_cents //100
        cents = total_cents % 100
        return cls(dollar, cents)

class TipMoney(Money):
    pass



if __name__=="__main__":
    tip = TipMoney.from_pennies(475)
