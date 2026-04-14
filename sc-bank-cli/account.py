#Account class that holds balance and performs deposit/withdraw operations.
from datetime import datetime

class MinimumFundsError(Exception):
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



acc = Account("Aniruddh", "A001", 5000)
acc.deposit(1000)
acc.withdraw(500)
print(acc)
print(acc.get_history())