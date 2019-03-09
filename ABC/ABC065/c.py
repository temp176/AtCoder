import math

N,M = map(int,input().split())
if abs(N-M) >= 2:
    print(0)
    exit()
elif abs(N-M) == 1:
    res = math.factorial(N)*math.factorial(M)
    print(res%(10**9+7))
else:
    res = math.factorial(N)*math.factorial(M) * 2
    print(res%(10**9+7))