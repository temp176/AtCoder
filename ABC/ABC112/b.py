N,T = map(int,input().split())

ct = []
tmp = []
for i in range(N):
    tmp = list(map(str,input().split()))
    #tmp = list(map(int,input().split()))
    ct.append(list(tmp))

res = 1001
for c,t in ct:
    if int(t) <= int(T):
        if res > int(c):
            res = int(c)

if res == 1001:
    print('TLE')
else:
    print(res)



