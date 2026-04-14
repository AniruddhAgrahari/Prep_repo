#Account class that holds balance and performs deposit/withdraw operations.
from datetime import datetime

class MinimumFundsError(Exception):
    pass
class InsufficientFundsError(Exception):
     pass

class Account:

    def __init__(self, owner, account_id, balance = 0):

        self.history = []

        if balance < 0:
             raise ValueError
        self.owner = owner
        self.__balance = balance
        self.account_id = account_id



    @property
    def balance(self):
        return self.__balance
    
    def get_history(self):
         return self.history
    
    def deposit(self, amount):
            self.__balance += amount
            
            transaction_history = {
                 "type":"deposit",
                 "amount":amount,
                 "time_stamp":datetime.now(),
                 "balance_after":self.balance
            }

            self.history.append(transaction_history)

    def withdraw(self, amount):
         if amount > self.__balance:
              raise MinimumFundsError
         else:
              self.__balance -= amount
              transaction_history = {
                   "type":"withdraw",
                   "amount":amount,
                   "time_stamp":datetime.now(),
                   "balance_after":self.balance
              }
              self.history.append(transaction_history)

    def __str__(self):
         return (f"Owner:{self.owner}, Account:{self.account_id}, Balance:{self.balance}")

class SavingsAccount(Account):
     def __init__(self, min_bal, owner, account_id, balance=0):
          super().__init__(owner, account_id, balance)
          self.min_bal = min_bal
     def withdraw(self, amount):
          usable_amount = self.balance - self.min_bal
          if amount > usable_amount:
               raise MinimumFundsError
          super().withdraw(amount)\
        
class CurrentAccount(Account):
     def __init__(self, owner, account_id, overdraft, balance = 0):
          super().__init__(owner, account_id, balance)
          self.overdraft = overdraft

     def withdraw(self, amount):
          total = self.balance + self.overdraft
          if amount > total:
               raise InsufficientFundsError
          elif amount > self.balance and amount <= total:
               self._Account__balance -= amount
               self._Account__balance -= 50  # fee
          else:
               super().withdraw(amount)
               
               
               
          
acc = Account("Aniruddh", "A001", 5000)
acc.deposit(1000)
acc.withdraw(500)
print(acc)
print(acc.get_history())

# SavingsAccount test
sav = SavingsAccount(1000, "Aniruddh", "S001", 5000)
sav.withdraw(3500)  # should work, balance stays above 1000
sav.withdraw(500)   # should raise MinimumFundsError

# CurrentAccount test
cur = CurrentAccount("Aniruddh", "C001", 500, 1000)
cur.withdraw(800)   # normal withdraw
cur.withdraw(400)   # overdraft, should charge ₹50 fee
cur.withdraw(1000)  # should raise error