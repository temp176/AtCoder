A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A < B:
    if C < D:
        print(A + C)
    else:
        print(A + D)
else:
    if C < D:
        print(B + C)
    else:
        print(B + D)
