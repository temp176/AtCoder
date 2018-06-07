N = int(input())
X = [int(i) for i in input().split()]

sortedX = X[:]
sortedX.sort()
lenX = len(X)

for i in X:
    if i > sortedX[int(lenX/2) - 1]:
        print(sortedX[int(lenX/2)-1])
    else:
        print(sortedX[int(lenX/2)])

