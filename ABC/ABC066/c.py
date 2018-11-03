from collections import deque

N = int(input())
A = [int(i) for i in input().split()]

B = deque(maxlen=2*10**5)

if N % 2 == 0:
    for i in range(N):
        if i % 2 == 0:
            B.append(A[i])
        else:
            B.appendleft(A[i])
else:
    for i in range(N):
        if i % 2 == 0:
            B.appendleft(A[i])
        else:
            B.append(A[i])

print(*B)