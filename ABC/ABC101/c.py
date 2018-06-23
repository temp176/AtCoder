import math

N,K = map(int,input().split())
A = [int(i) for i in input().split()]

res = math.ceil((N-1)/(K-1))

print(int(res))