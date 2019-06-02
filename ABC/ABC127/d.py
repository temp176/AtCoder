N,M= map(int,input().split())
A = [int(i) for i in input().split()]
BC = []
for i in range(M):
    BC.append(list(map(int,input().split())))

A.sort()
BC.sort(key = lambda x:-x[1])

s = 0
for b,c in BC:
    s_tmp = 0
    for i in range(s,N):
        if A[i] < c and b > 0:
            A[i] = c
            b -= 1
            s_tmp = i + 1
        elif A[i] >= c:
            print(sum(A))
            exit()
        elif b == 0:
            s = s_tmp
            break

print(sum(A))
