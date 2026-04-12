
# TC: O(2^n) — each call branches into 2, exponential growth
# SC: O(n) — maximum stack depth at any point is n frames

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(6))  # 8
print(fibonacci(7))  # 13