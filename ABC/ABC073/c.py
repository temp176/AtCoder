from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]

res = 0

c = Counter(A)

for i in c.values():
    if i % 2 != 0:
        res += 1

print(res)
