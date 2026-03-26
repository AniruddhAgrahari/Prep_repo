class TransactionEventSystem:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)
    
    def unsubscribe(self, observer):
        self.subscribers.remove(observer)

    def notify(self, amount):
        for i in self.subscribers:
            i.update(amount)

class SMSNotifier:

    def update(self, amount):
        print(f"SMS sent: transaction of amount {amount} posted.")

class EmailNotifier:

    def update(self, amount):
        print(f"Email sent: transaction of amount {amount} posted.")

class FraudMonitor:

    def update(self, amount):
        if amount > 50000:
            print(f"Fraud Alert!!! {amount} flagged")
        else:
            print(f"Fraud check cleared: {amount}")

system = TransactionEventSystem()
system.subscribe(SMSNotifier())
system.subscribe(EmailNotifier())
system.subscribe(FraudMonitor())
system.notify(75000)
system.notify(10000)
