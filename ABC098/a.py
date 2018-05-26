A,B=[int(i) for i in input().split()]

X = A + B
Y = A - B
Z = A * B

if X >= Y and X >= Z:
    print(X)
elif Y >= X and Y >= Z:
    print(Y)
else:
    print(Z)