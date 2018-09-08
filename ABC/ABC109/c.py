import fractions
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)


N,X =[int(i) for i in input().split()]
c = [int(i) for i in input().split()]

for i in range(N):
    c[i] = abs(c[i] - X)

print(gcd_list(c))



