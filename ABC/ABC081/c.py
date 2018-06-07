from collections import Counter

N,K = map(int,input().split())
A = [i for i in input().split()]

altCounter = 0
d = Counter(A).most_common()
d = d[::-1]

for i in range(len(d)-K):
    altCounter += d[i][1]

print(altCounter)


