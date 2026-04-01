from collections import deque


class TransactionQueue:
    def __init__(self):
        self.queue = deque()


    def enqueue(self, transaction):
        self.queue.append(transaction)

    def dequeue(self):
        return self.queue.popleft()

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False


q = TransactionQueue()
q.enqueue({"id":1, "amount":5000, "type":"CREDIT"})
q.enqueue({"id":2, "amount":2000, "type":"DEBIT"})
q.enqueue({"id":3, "amount":8000, "type":"CREDIT"})


print(q.peek())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
print(q.dequeue())
print(q.is_empty())