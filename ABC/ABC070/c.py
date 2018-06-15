#https://note.nkmk.me/python-gcd-lcm/
#Python3(3.4.3)

import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

N = int(input())
T = [int(input()) for _ in range(N)]

print(lcm_list(T))



