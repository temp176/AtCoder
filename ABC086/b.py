import numpy as np

a,b = [i for i in input().split()]
N = int(a+b)
if N == int(np.sqrt(N)) ** 2:
    print('Yes')
else:
    print('No')