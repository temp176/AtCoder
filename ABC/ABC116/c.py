N = int(input())
H = [int(i) for i in input().split()]
res = 0

for i in range(N):
    if i == 0:
        res += H[0]
    else:
        if H[i-1] < H[i]:
            res += H[i] - H[i-1]

print(res)