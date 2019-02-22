import math

N = int(input())
A = [int(i) for i in input().split()]

mul_num = 0
two_num = 0
other_num = 0

for i in A:
    if i % 4 == 0:
        mul_num += 1
    elif i % 2 == 0:
        two_num += 1
    else:
        other_num += 1

if mul_num + two_num//2 >= N // 2:
    print('Yes')
else:
    print('No')

