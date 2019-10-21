N = int(input())
H = [int(i) for i in input().split()]

C = [0] * N

C[-1] = False
for i in range(len(H)-1):
    if H[i+1] <= H[i]:
        C[i] = True
    else:
        C[i] = False

res = 0
tmp = 0
for i in range(len(C)):
    if C[i]:
        tmp += 1
    else:
        res = max(res,tmp)
        tmp = 0

print(res)

