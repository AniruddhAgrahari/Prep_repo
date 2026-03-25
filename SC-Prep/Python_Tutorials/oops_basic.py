class InsufficientFundsError(Exception):
    pass

class MinimumFundsError(Exception):
    pass

class BankAccount:
    bank_name = "Standard Chartered"
    min_bal = 10000

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}'s new balance: {self.balance}")

    def withdraw(self, amount):
        usable_amount = self.balance - self.min_bal
        if amount > usable_amount:
            raise MinimumFundsError(f"Insufficient Funds for {self.owner} - attempted: {amount}, available:{usable_amount}")
        self.balance -= amount
        print(f"{self.owner}'s new balance: {self.balance}")

aniruddh_account = BankAccount("Aniruddh", 100000)
aaddya_account = BankAccount("Aaddya", 8000)


try:
    aaddya_account.withdraw(9000)
except MinimumFundsError as e:
    print(e)
    
# print(aniruddh_account.owner)
# print(aaddya_account.owner)

# print(aniruddh_account.bank_name)
# print(aaddya_account.bank_name)
# print(BankAccount.min_bal)

# BankAccount.min_bal = 15000
# print(aniruddh_account.min_bal)
# print(aaddya_account.min_bal)

# aniruddh_account.min_bal = 20000
# print(aniruddh_account.min_bal)
# print(aaddya_account.min_bal)
# print(BankAccount.min_bal)

# aniruddh_account = BankAccount("Aniruddh", 15000)
# aaddya_account = BankAccount("Aaddya", 8000)

# aniruddh_account.deposit(5000)
# aaddya_account.withdraw(2000)

