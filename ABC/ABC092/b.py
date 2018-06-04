N = int(input())
D,X = map(int,input().split())
A = [int(input()) for _ in range(N)] 

chocolate = 0
for i in range(N):
    count = 0
    for j in range(D+1):
        if j == (count * A[i] + 1):
            chocolate += 1
            count += 1
print(chocolate + X)