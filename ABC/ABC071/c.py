import collections

N = int(input())
A = [int(i) for i in input().split()]

count = collections.Counter(A).most_common()

candidate = [(i,j) for i,j in count if j >= 2]

if len(candidate) == 0:
    print(0)
    exit()

candidate = sorted(candidate)

if candidate[-1][1] >= 4:
    print(candidate[-1][0] ** 2)
else:
    print(candidate[-1][0] * candidate[-2][0])
