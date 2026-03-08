class InsufficientFundsError(Exception):
    pass



class BankAccount:
    def __init__(self, owner:str, balance:float = 0.0):
        self.owner = owner
        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount: float) -> None:
        self.__balance += amount
        self.__transactions.append(("deposit", amount))

    def withdraw(self, amount: float) -> None:
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(("withdraw", amount))
        else:
            raise InsufficientFundsError

    @property
    def balance(self) -> float:
        return self.__balance
    
    def get_transactions(self):
        for transaction in self.__transactions:
            yield transaction


if __name__ == "__main__":
    acc = BankAccount("Aniruddh", 5000)
    acc.deposit(2000)
    acc.withdraw(1000)
    print(acc.balance)

    for t in acc.get_transactions():
        print(t)
    
    # acc.withdraw(99999)

