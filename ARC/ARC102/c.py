N,K = map(int,input().split())

res1 = 0
for i in range(1,N+1):
    if i % K == 0:
        res1 += 1

if K % 2 != 0:
    print(res1**3)
    exit()

res2 = 0

for i in range(1,N+1):
    if i % K == int(K/2):
        res2 += 1


print(res1**3+res2**3)
