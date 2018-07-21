import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(numbers):
    return reduce(lcm_base, numbers, 1)

N = int(input())
A = [int(i) for i in input().split()]

m = lcm(A) - 1
f = 0
for i in range(N):
    f += m % A[i]
print(f)

