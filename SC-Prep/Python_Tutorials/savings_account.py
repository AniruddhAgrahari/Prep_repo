from bank_account import BankAccount, InsufficientFundsError


class MinimumBalanceError(Exception):
      pass
    
class SavingsAccount(BankAccount):
        
        def __init__(self, owner, balance, min_bal):
            super().__init__(owner, balance)
            self.min_bal = min_bal

        def withdraw(self, amount):
              if amount > self.balance:
                    raise InsufficientFundsError
              if self.balance - amount < self.min_bal:
                    raise MinimumBalanceError
              super().withdraw(amount)


acc1 = SavingsAccount("Aniruddh", 1000, 500)
acc1.withdraw(200)
assert acc1.balance == 800

acc2 = SavingsAccount("Aniruddh", 1000, 500)
try:
      acc2.withdraw(1500)
      assert False
except InsufficientFundsError:
     pass

acc3 = SavingsAccount("Aniruddh", 1000, 500)
try:
      acc3.withdraw(600)
      assert False
except MinimumBalanceError:
      pass