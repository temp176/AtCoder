N = [int(i) for i in input().split()]
if abs(N[2] - N[0]) <= N[3]:
    print('Yes')
elif abs(N[1] - N[0]) <= N[3] and abs(N[2] - N[1]) <= N[3]:
    print('Yes')
else:
    print('No')