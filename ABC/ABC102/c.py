import collections
 
N = int(input())
A = [int(i) for i in input().split()]
 
sub = [A[i]-(i+1) for i in range(N)]
res = 0
sub = sorted(sub)
b = sub[int(N/2)]
 
res = 0
for i in range(N):
    res += abs(A[i]-(b+i+1))

print(res)