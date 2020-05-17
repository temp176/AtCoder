N = int(input())
A = [int(i) for i in input().split()]

res = 0

for a in A:
    res += 1/a

print(1/res)