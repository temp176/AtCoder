N,K = map(int,input().split())
H = [int(i) for i in input().split()]

res = 0

for h in H:
    if h >= K:
        res += 1

print(res)