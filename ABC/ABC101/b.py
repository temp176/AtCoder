s = int(input())
N = list(str(s))

sumN = 0
for i in range(len(N)):
    sumN += int(N[i])

if s % sumN == 0:
    print('Yes')
else:
    print('No')