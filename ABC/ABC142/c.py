N = int(input())
A = [int(i) for i in input().split()]

index_order = sorted(range(len(A)), key=lambda x: A[x])

res = [0]*N

for i,index in enumerate(index_order):
    res[i] = index + 1

print(*res)
