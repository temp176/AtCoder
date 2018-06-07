N = int(input())
A = [int(i) for i in input().split()]
i,counter = 0,0
divCheck = False
while True:
    i = 0
    for i in range(0,N):
        if A[i] % 2 == 0:
            A[i] /= 2
        else:
            divCheck = True
    if divCheck:
        break
    counter += 1
print(counter)