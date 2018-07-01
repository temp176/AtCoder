N = int(input())
a = []
tmp = []
for i in range(N):
    tmp = [int(i) for i in input().split()]
    a.append(tmp)

res = 0
for i in a:
    if i[1] - i[0] == 0:
        res += 1
    else:
        res += i[1] - i[0] + 1

print(res)
