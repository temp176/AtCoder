N = int(input())
K = int(input())

Dis = 1

for i in range(N):
    if (2 * Dis - Dis < K):
        Dis *= 2
    else:
        Dis += K

print(Dis)