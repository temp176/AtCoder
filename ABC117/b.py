N = int(input())
L = [int(i) for i in input().split()]
L.sort()
max_edge = L[-1]
total_length = 0
for i in L[:-1]:
    total_length += i

if max_edge < total_length:
    print('Yes')
else:
    print('No')


