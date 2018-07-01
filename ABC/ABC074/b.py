N = int(input())
K = int(input())
X = [int(i) for i in input().split()]

total = 0
for i in range(N):
    if abs(X[i] - K) < abs(X[i]):
        total += 2 * abs(X[i] - K)
    else:
        total += 2 * abs(X[i])

print(total)