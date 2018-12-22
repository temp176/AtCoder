import fractions
from functools import reduce

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

N,P = map(int,input().split())

factor = prime_factors(P)

res_fac = factor[:N]
rem_fac = factor[N:]

index = 0
for i in rem_fac:
    if len(res_fac)-1 < index:
        index = 0
    res_fac[index] *= i
    index += 1

print(gcd_list(res_fac))