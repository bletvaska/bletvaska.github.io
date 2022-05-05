from dataclasses import dataclass


@dataclass
class BankAccount:
    owner: str
    balance: int = 0

    def withdraw(self, amount: int):
        if type(amount) != int:
            raise TypeError(f'Amount "{amount}" is not integer.')

        if amount < 0:
            raise ValueError('Amount should be positive.')

        self.balance -= amount

        # return self.balance


    def deposit(self, amount: int):
        if type(amount) != int:
            raise TypeError(f'Amount "{amount}" is not integer.')

        if amount < 0:
            raise ValueError('Amount should be positive.')

        if self.balance - amount < 0:
            raise ValueError('Insufficient funds.')

        self.balance += amount

        # return self.balance


    def transfer(self, account, amount: int):
        pass

