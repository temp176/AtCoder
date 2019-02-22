N = int(input())
A = [int(i) for i in input().split()]
A_total = [0 for i in A]

A_total[0] = A[0]

for i in range(1,len(A)):
    A_total[i] = A_total[i-1] + A[i]

min_num = float('inf')

for i in range(len(A_total[:-1])):
    snuke = A_total[i]
    bear = A_total[-1] - A_total[i]
    tmp = abs(snuke-bear)
    if min_num > tmp:
        min_num = tmp

print(min_num)
