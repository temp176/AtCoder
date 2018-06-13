N = int(input())
a = []
tmp = []
for i in range(2):
    tmp = list(map(int,input().split()))
    a.append(list(tmp))

maxCandies = 0
for i in range(N):
    total = sum(a[0][:i+1]) + sum(a[1][i:])
    if maxCandies < total:
        maxCandies = total
    total = 0

print(maxCandies)
