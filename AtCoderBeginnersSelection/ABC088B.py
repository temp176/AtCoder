N = int(input())
A = [int(i) for i in input().split()]
A.sort()
A.reverse()
Bob,Alice = 0,0
for i in range(0,N,2):
    Alice += A[i]
    if i+1 < N:
        Bob += A[i+1]
print(Alice - Bob)