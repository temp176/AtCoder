import collections

N = int(input())
A = [int(i) for i in input().split()]

el_count = collections.Counter(A)

res = 0
for X in range(100000):
    tmp = el_count[X-1] + el_count[X] + el_count[X+1]
    if res < tmp:
        res = tmp

print(res)

