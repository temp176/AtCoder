N, M = map(int, input().split())
ab = []
cd = []
for i in range(N):
    ab.append(list(map(int,input().split())))

for i in range(M):
    cd.append(list(map(int,input().split())))

for sx,sy in ab:
    dist_min = float('inf')
    num_min = -1
    for i in range(M):
        tmp = abs(sx-cd[i][0]) + abs(sy-cd[i][1])
        if dist_min > tmp:
            num_min = i + 1
            dist_min = tmp
    print(num_min)


