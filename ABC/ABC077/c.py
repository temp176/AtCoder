from bisect import bisect_left, bisect_right

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

A.sort()
C.sort()

result = 0

for i in B:
    a = bisect_left(A,i)
    c = bisect_right(C,i)
    result += a * (N - c)

print(result)

