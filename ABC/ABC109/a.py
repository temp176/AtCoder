a,b=[int(i) for i in input().split()]

res = 0
f = False
for i in range(1,4):
    res = a * b * i
    if res % 2 == 1:
        f = True

if f:
    print('Yes')
else:
    print('No')


