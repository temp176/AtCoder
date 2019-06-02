N,M = map(int,input().split())
LR = []
for i in range(M):
    LR.append(list(map(int,input().split())))

max_l = 0
min_r = float('inf')

for l,r in LR:
    max_l = max(max_l,l)
    min_r = min(min_r,r)

if max_l <= min_r:
    print(min_r - max_l + 1)
else:
    print(0)