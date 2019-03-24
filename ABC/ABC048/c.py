N,x = map(int,input().split())
A = [int(i) for i in input().split()]

res = 0
for i in range(N-1):
    if A[i] + A[i+1] > x:
        eat = A[i]+A[i+1]-x
        A[i+1] = max(0,A[i+1]-eat)
        res += eat
        if A[i+1]-eat < 0:
            A[i] -= abs(A[i+1]-eat)

#print(A)
print(res)