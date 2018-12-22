N,H,W = map(int,input().split())
AB = []
for i in range(N):
    AB.append(list(map(int,input().split())))

res = 0
for i in range(N):
    if AB[i][0] >= H and AB[i][1] >= W:
        res += 1

print(res)
