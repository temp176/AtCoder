N,K = map(int,input().split())
H = [int(input()) for _ in range(N)]

H.sort()

res = 1000000000
for i in range(N-K+1):
    tmp = H[i+K-1]-H[i]
    if tmp < res:
        res = tmp
print(res)