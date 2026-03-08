def normal():
    return [1, 2, 3]

def generators():
    yield 1
    yield 2 
    yield 3

print(normal())

g = generators()

print(next(g))
print(next(g))
print(next(g))
