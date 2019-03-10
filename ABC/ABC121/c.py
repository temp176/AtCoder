N,M = map(int,input().split())
AB= []
for i in range(N):
    AB.append(list(map(int,input().split())))

AB.sort()

res = 0
count = 0

for A,B in AB:
    if  B <= M - count:
        count += B
        res += A * B
    else:
        res += A * (M - count)
        count = M

    if count == M:
        break

print(res)
