N = [int(i) for i in input().split()]
A = N[0]
B = N[1]
C = N[2]
K = N[3]

if K % 2 == 0:
    if abs(A - B) > 10 ** 18:
        print('Unfair')
    else:
        print(A - B)
else :
    if abs(A - B) > 10 ** 18:
        print('Unfair')
    else:
        print(B - A)
