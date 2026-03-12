from bank_account import BankAccount, InsufficientFundsError


class CurrentAccount(BankAccount):
    
    def __init__(self, owner, balance, overdraft):
        super().__init__(owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        total_limit = self.balance + self.overdraft
        if amount > (total_limit):
            raise InsufficientFundsError
        super().withdraw(amount)

    def calculate_interest(self, time):
        return 0
    

acc1 = CurrentAccount("Aniruddh", 1000, 500)
acc1.withdraw(1200)
assert acc1.balance == -200

acc2 = CurrentAccount("Rajiv", 6969, 69)
try:
    acc2.withdraw(7500)
    assert False
except InsufficientFundsError:
    pass

acc3 = CurrentAccount("Harshal", 5500, 500)
acc3.calculate_interest(1)