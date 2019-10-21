N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

res = 0
for i in range(len(A)):
    res += B[A[i] - 1]
    if i + 1 < N:
        if A[i+1] == A[i] + 1:
            res += C[A[i] - 1]

print(res)
