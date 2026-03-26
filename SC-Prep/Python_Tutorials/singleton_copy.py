class BankConfig:
    _instance = None

    def __new__(cls):
      if cls._instance is None:
        cls._instance = super().__new__(cls)
        cls._instance.interest_rate = 0.04
        cls._instance.transaction_limit = 25000
      return cls._instance
    


config1 = BankConfig()
config2 = BankConfig()
print(config1 is config2)
print(config1.interest_rate)
print(config2.interest_rate)


# print(config1 is config2)  # Should print True


