N = [int(i) for i in input().split()]

if N[0] + N[1] >= N[2] and N[0] <= N[2]:
    print('YES')
else:
    print('NO')