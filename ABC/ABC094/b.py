N,M,X = map(int,input().split())
A = [int(i) for i in input().split()]

counterToN,counterToX = 0,0

for i in A:
    if i - 1 < X :
        counterToN += 1
    else :
        counterToX += 1

print(min([counterToN,counterToX]))


