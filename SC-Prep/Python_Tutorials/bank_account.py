class InsufficientFundsError(Exception):
    pass



class BankAccount:
    def __init__(self, owner:str, balance:float = 0.0):
        self.owner = owner
        self._balance = balance
        self._transactions = []

    def deposit(self, amount: float) -> None:
        self._balance += amount
        self._transactions.append(("deposit", amount))

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise InsufficientFundsError
            self._balance -= amount
            self._transactions.append(("withdraw", amount))
        else:
            raise InsufficientFundsError

    @property
    def balance(self) -> float:
        return self._balance
    
    def get_transactions(self):
        for transaction in self._transactions:
            yield transaction


if __name__ == "__main__":
    acc = BankAccount("Aniruddh", 5000)
    acc.deposit(2000)
    acc.withdraw(1000)
    print(acc.balance)

    for t in acc.get_transactions():
        print(t)
    
    # acc.withdraw(99999)

