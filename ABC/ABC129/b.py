N = int(input())
W = [int(i) for i in input().split()]

res = float('inf')

for i in range(N):
    res = min(res,abs(sum(W[:i])-sum(W[i:])))

print(res)
