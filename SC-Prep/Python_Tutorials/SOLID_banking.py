from abc import ABC, abstractmethod

class InsufficientFundsError(Exception):
    pass

class IDepositable(ABC):
    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

class IWithdrawable(ABC):
    @abstractmethod
    def withdraw(self, amount:float) -> None:
        pass

class IInterestBearing(ABC):
    @abstractmethod
    def calculate_interest(self, time: float) -> float:
        pass

class TransactionLogger:
    def __init__(self):
        self._transactions = []
    def log(self, transaction_type: str, amount: float) -> None:
        self._transactions.append((transaction_type, amount))

    def get_transactions(self):
        for transaction in self._transactions:
            yield transaction

class BankAccount(IDepositable, IWithdrawable):
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance
        self._logger = TransactionLogger()

    def deposit(self, amount: float) -> None:
        self._balance += amount
        self._logger.log("deposit", amount)
    
    def withdraw(self, amount:float) -> None:
        if amount > self._balance:
            raise InsufficientFundsError
        self._balance -= amount
        self._logger.log("withdraw", amount)

    @property
    def balance(self) -> float:
        return self._balance
    def get_transactions(self):
        return self._logger.get_transactions()