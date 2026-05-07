#Data class that records single transaction event
# - amount, type, date, account_id

from datetime import datetime

class Transaction:
    def __init__(self, account_id, amount, txn_type, timestamp=None):
        self.account_id = account_id
        self.amount = amount
        self.txn_type = txn_type
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
         return (f"[{self.timestamp}] {self.txn_type.upper()} "
                 f"| Account: {self.account_id} "
                 f"| Amount: Rs.{self.amount}")
    

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "amount":self.amount,
            "txn_type":self.txn_type,
            "timestamp":str(self.timestamp)
        }
        

    @classmethod

    def from_dict(cls, d):
        return cls(
            account_id=d["account_id"],
            amount=d["amount"],
            txn_type=d["txn_type"],
            timestamp=d["timestamp"]
        )

