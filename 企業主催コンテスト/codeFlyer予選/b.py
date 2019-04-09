A,B,N = map(int,input().split())
X = input()

for i in X:
    if i == 'S':
        A = max(0,A-1)
    elif i == 'C':
        B = max(0,B-1)
    else:
        if A >= B:
            A = max(0,A-1)
        else:
            B = max(0,B-1)

print(A)
print(B)
