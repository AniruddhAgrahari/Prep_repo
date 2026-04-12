
def power_naive(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power_naive(base, exp-1)

print(power_naive(2, 8))   # 256
