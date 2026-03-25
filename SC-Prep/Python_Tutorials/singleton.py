class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.04
            cls._instance.transaction_limit = 100000
        return cls._instance

# Test it yourself
config1 = BankConfig()
config2 = BankConfig()
print(config1 is config2)  # what do you expect this to print?