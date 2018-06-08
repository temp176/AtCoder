N = input()

sumN = 0
for i in list(N):
    sumN += int(i)

if int(N) % sumN == 0:
    print('Yes')
else:
    print('No')