X,Y=[int(i) for i in input().split()]

lenCount = 0
while X <= Y:
    X *= 2
    lenCount += 1

print(lenCount)