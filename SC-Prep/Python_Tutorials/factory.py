class BankAccount:
     
    def __init__(self, owner, balance, account_type):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type

    

class SavingsAccount(BankAccount):

    def __init__(self, owner, balance, account_type = "savings"):
        super().__init__(owner, balance, account_type)

class CurrentAccount(BankAccount):

    def __init__(self, owner, balance, account_type = "current"):
        super().__init__(owner, balance, account_type)

class AccountFactory:

    @staticmethod
    def create(account_type, owner, balance):
        if account_type == "savings":
            return SavingsAccount(owner, balance)
        elif account_type ==  "current":
            return CurrentAccount(owner, balance)
    
acc1 = AccountFactory.create("savings", "Aniruddh", 50000)
acc2 = AccountFactory.create("current", "Rahul", 100000)
print(acc1.account_type, acc1.owner, acc1.balance)
print(acc2.account_type, acc2.owner, acc2.balance)