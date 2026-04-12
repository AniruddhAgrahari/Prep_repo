
#TC: O(n) - n recursive calls
#SC: O(n) - n stack frames

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(0))   # should be 1
print(factorial(1))   # should be 1
print(factorial(4))   # should be 24
print(factorial(5))   # should be 120