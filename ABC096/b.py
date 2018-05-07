N = [int(i) for i in input().split()]
K = int(input())
index_max = N.index(max(N))
i = 0
total = 0
for i in range(3):
    if i != index_max:
        total += N[i]
print(N[index_max]*(2**K)+total)