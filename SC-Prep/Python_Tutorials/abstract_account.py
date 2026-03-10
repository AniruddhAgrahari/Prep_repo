from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def calculate_interest(self, time):
        pass

class SavingsAccount(Account):

    def __init__(self, owner, balance, min_bal):
        self.balance = balance
        self.min_bal = min_bal

    def calculate_interest(self, time):
        return (self.balance * 4 * time) / 100
    
class CurrentAccount(Account):

    def __init__(self, owner, balance, overdraft):
        self.balance = balance
        self.overdraft = overdraft

    def calculate_interest(self, time):
        return (self.balance * 2 * time) / 100
    

acc1 = SavingsAccount("Aniruddh", 1000, 500)
result = acc1.calculate_interest(1)
assert result == 40

acc2 = CurrentAccount("Aniruddh", 10000, 5000)
result = acc2.calculate_interest(2)
assert result == 400
