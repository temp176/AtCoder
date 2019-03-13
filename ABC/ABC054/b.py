N, M = map(int, input().split())
A = []
for i in range(N):
    row = list(map(str,input().split()))
    A.append(list(row[0]))
B = []
for i in range(M):
    row = list(map(str,input().split()))
    B.append(list(row[0]))

for i in range(N-M+1):
    for j in range(N-M+1):
        sub_A = [a[j:j+M] for a in A[i:M+i]]
        if sub_A == B:
            print('Yes')
            exit()

print('No')