N,K,Q = map(int,input().split())
A = [int(input()) for _ in range(Q)]

res = [K for _ in range(N)]

ac_num = [0]*N

for a in A:
    ac_num[a-1] += 1

for i in range(N):
    res[i] -= (Q - ac_num[i])


for i in res:
    if i > 0:
        print('Yes')
    else:
        print('No')
