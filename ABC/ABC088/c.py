c = []
tmp = []
for i in range(3):
    tmp = list(map(int,input().split()))
    c.append(tmp)

for a1 in range(100+1):
    for b1 in range(100+1):
        if not a1 + b1 == c[0][0]:
            continue
        a2 = c[1][0] - b1
        b2 = c[0][1] - a1
        a3 = c[2][0] - b1
        b3 = c[0][2] - a1
        if a2 + b2 == c[1][1] and a2 + b3 == c[1][2] and a3 + b2 == c[2][1] and a3 + b3 == c[2][2]:
            print('Yes')
            exit()

print('No')