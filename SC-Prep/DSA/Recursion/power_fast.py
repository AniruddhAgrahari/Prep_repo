
def power_fast(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
         half = power_fast(base, exp//2)
         return half * half
    else:
        return base * power_fast(base, exp-1)
    
print(power_fast(2, 8))    # 256
print(power_fast(2, 10))   # 1024
print(power_fast(3, 5))    # 243