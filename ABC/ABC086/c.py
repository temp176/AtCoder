N = int(input())
point = [[0,0,0]]
tmp = []
for i in range(N):
    tmp = list(map(int,input().split()))
    point.append(list(tmp))

for i in range(N):

    if i == len(point):
        break

    Np = point[i][0]
    xp = point[i][1]
    yp = point[i][2]

    Nn = point[i+1][0]
    xn = point[i+1][1]
    yn = point[i+1][2]

    dist = abs(xn-xp) + abs(yn-yp)

    if dist != Nn - Np:
        if dist > Nn - Np:
            print('No')
            exit()
        else:
            if dist % 2 != (Nn - Np) % 2:
                print('No')
                exit()

print('Yes')

