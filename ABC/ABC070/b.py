A,B,C,D = map(int,input().split())

if A < C:
    if B < D:
        if B - C >= 0:
            print(B-C)
        else:
            print(0)
    else:
        if D - C >= 0:
            print(D-C)
        else:
            print(0)
else:
    if B < D:
        if B - A >= 0:
            print(B-A)
        else:
            print(0)
    else:
        if D - A >= 0:
            print(D-A)
        else:
            print(0)
