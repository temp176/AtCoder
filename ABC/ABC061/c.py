N,K = map(int,input().split())
ab = []
for i in range(N):
    ab.append(list(map(int,input().split())))

ab.sort()

index = 0

for a,b in ab:
    index += b
    if index >= K:
        print(a)
        break