N = int(input())
V = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

res = 0
for i in range(N):
    if V[i] > C[i]:
        res += V[i] - C[i]

print(res)
