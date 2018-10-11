N = int(input())
A = [int(i) for i in input().split()]

count = 0
i = 0
while i < N - 1:
    if A[i] == A[i+1]:
        count += 1
        i += 1
    i += 1

print(count)