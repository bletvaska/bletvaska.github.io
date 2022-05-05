from dataclasses import dataclass


@dataclass
class BankAccount:
    ballance: int = 0

    def deposit(self, amount: int):
        if type(amount) != int:
            raise TypeError('The amount should be integer')

        if amount < 0:
            raise ValueError('The amount should be positive.')

        self.ballance += amount


