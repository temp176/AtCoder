from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]

d = Counter(A).most_common()
d = d[::-1]

reCounter = 0

for i in range(len(d)):
    if d[i][0] < d[i][1]:
        reCounter += d[i][1] - d[i][0]
    if d[i][0] > d[i][1]:
        reCounter += d[i][1]
        
print(reCounter)