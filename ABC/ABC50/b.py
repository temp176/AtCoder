N = int(input())
T = [int(i) for i in input().split()]
M = int(input())
PX = []
for i in range(M):
    PX.append(list(map(int,input().split())))

d_sum = sum(T)
for p,x in PX:
    res = d_sum
    res -= T[p-1]
    res += x
    print(res)

