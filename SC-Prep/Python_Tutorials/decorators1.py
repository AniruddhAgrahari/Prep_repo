
def decorator(func):
    def wrapper():
        print("The function is starting.")
        func()
        print("The function is ending.")
    return wrapper
    



@decorator
def greet():
    print("Hi, Aniruddh")

# greet = decorator(greet)
greet()