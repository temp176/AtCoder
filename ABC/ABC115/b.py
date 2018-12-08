N = int(input())
P = [int(input()) for _ in range(N)]

total = 0
P.sort()

for i in range(N-1):
    total += P[i]

total += int(P[-1]/2)

print(total)
