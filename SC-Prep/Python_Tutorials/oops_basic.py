class InsufficientFundsError(Exception):
    pass

class MinimumFundsError(Exception):
    pass

class BankAccount:
    bank_name = "Standard Chartered"
    min_bal = 10000

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError(f"Balance cannot be negative for {self.owner}")
        self._balance = amount

    @classmethod
    def create_student_account(cls, owner):
        return cls(owner, 0)
    
    @staticmethod
    def validate_account_number(account_number):
        return len(str(account_number)) == 10

    def deposit(self, amount):
        self._balance += amount
        print(f"{self.owner}'s new balance: {self._balance}")

    def withdraw(self, amount):
        usable_amount = self._balance - self.min_bal
        if amount > usable_amount:
            raise MinimumFundsError(f"Insufficient Funds for {self.owner} - attempted: {amount}, available:{usable_amount}")
        self._balance -= amount
        print(f"{self.owner}'s new balance: {self._balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance) 
        self.interest_rate = interest_rate

class CurrentAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        total_withdrawable = self._balance + self.overdraft_limit
        if amount > total_withdrawable:
            raise MinimumFundsError(f"Insufficient Funds for {self.owner} - attempted:{amount}, available:{total_withdrawable}")
        self._balance -= amount




aniruddh_account = BankAccount("Aniruddh", 100000)
aaddya_account = BankAccount("Aaddya", 8000)

current = CurrentAccount("Aniruddh", 5000, 10000)
print(current.balance)      # 5000

current.withdraw(3000)
print(current.balance)      # 2000 — normal withdrawal

current.withdraw(8000)
print(current.balance)      # -6000 — overdraft used

try:
    current.withdraw(5000)  # should fail — exceeded overdraft
except MinimumFundsError as e:
    print(e)

# savings = SavingsAccount("Aniruddh", 15000, 0.04)
# print(savings.owner)
# print(savings.balance)
# print(savings.interest_rate)

# print(BankAccount.validate_account_number(1234567890))  # True
# print(BankAccount.validate_account_number(123))          # False
# student_account = BankAccount.create_student_account("Aniruddh")
# print(student_account.owner)
# print(student_account.balance)

# print(aniruddh_account.balance)   # should work
# aniruddh_account.balance = 5000   # what happens here?


# try:
#     aaddya_account.withdraw(9000)
# except MinimumFundsError as e:
#     print(e)
    
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

