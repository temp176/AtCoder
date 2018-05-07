N = [int(i) for i in input().split()]
if N[0] * N[1] % 2 == 0:
    print('Even')
else:
    print('Odd')