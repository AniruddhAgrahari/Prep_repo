from abc import ABC, abstractmethod

class InsufficientFundsError(Exception):
    pass

class MinimumBalanceError(Exception):
    pass

class IDepositable(ABC):
    
    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

class IWithdrawable(ABC):

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

class IInterestBearing(ABC):

    @abstractmethod
    def calculate_interest(self, time: float) -> float:
        pass

class TransactionLogger():

    def __init__(self):
        self._transactions = []
    def log(self, txn_type: str, amount: float):
        self._transactions.append((txn_type, amount))
    def get_transactions(self):
        for transaction in self._transactions:
            yield transaction

class BankAccount(IDepositable, IWithdrawable):

    def __init__(self, owner, balance, logger=None):
        self.owner = owner
        self._balance = balance
        self._logger = logger or TransactionLogger()
    
    @property
    def balance(self):
        return self._balance
    def get_transactions(self):
        return self._logger.get_transactions()
    def deposit(self, amount):
        self._balance += amount
        self._logger.log("deposit", amount)
    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError
        self._balance -= amount
        self._logger.log("withdraw", amount)

class SavingsAccount(BankAccount, IInterestBearing):

    def __init__(self, owner, balance, min_bal, logger=None):
        super().__init__(owner, balance, logger)
        self.min_bal = min_bal

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError
        rem_bal = self._balance - amount
        if rem_bal < self.min_bal:
            raise MinimumBalanceError
        super().withdraw(amount)
        
    def calculate_interest(self, time):
        return (self._balance * 4 * time) / 100 
    
class CurrentAccount(BankAccount, IInterestBearing):

    def __init__(self, owner, balance, overdraft, logger=None):
        super().__init__(owner, balance, logger)
        self.overdraft = overdraft

    def withdraw(self, amount):
        total_limit = self._balance + self.overdraft
        if amount > total_limit:
            raise InsufficientFundsError
        self._balance -= amount
        self._logger.log("withdraw", amount)


    def calculate_interest(self, time):
        return 0



acc = BankAccount("Aniruddh", 1000)
acc.deposit(500)
assert acc.balance == 1500
acc.withdraw(200)
assert acc.balance == 1300

acc1 = SavingsAccount("Aniruddh", 1000, 500)
acc1.withdraw(100)
assert acc1.balance == 900

acc2 = SavingsAccount("Ani", 800, 300)
try:
    acc2.withdraw(1300)
    assert False
except InsufficientFundsError:
    pass

acc3 = SavingsAccount("Harshal", 1500, 1000)
try:
    acc3.withdraw(800)
    assert False
except MinimumBalanceError:
    pass

acc4 = CurrentAccount("Aniru", 2000, 200)
acc4.withdraw(400)
assert acc4.balance == 1600

acc5 = CurrentAccount("Aryan", 1500, 125)
acc5.withdraw(1600)
assert acc5.balance == -100

acc6 = CurrentAccount("Sachin", 2500, 250)
try:
    acc6.withdraw(3000)
    assert False
except InsufficientFundsError:
    pass
