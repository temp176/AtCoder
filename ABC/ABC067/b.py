N,K = map(int,input().split())
L = [int(i) for i in input().split()]

L = sorted(L)[::-1]

res = 0
for i in range(K):
    res += L[i]

print(res)
