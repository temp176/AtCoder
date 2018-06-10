H,W = map(int,input().split())
S = [input() for _ in range(H)] 

nS = [['' for i in range(W)] for j in range(H)]

cpC = [1, 0, -1, 0, 1, -1, -1, 1]
cpR = [0, 1, 0, -1, 1, 1, -1, -1]


for i in range(H):
    for j in range(W):
        counter = 0
        if S[i][j] == '#':
            nS[i][j] = '#'
            continue

        for r,c in zip(cpR,cpC):
            x = i + r
            y = j + c
            if x >= 0 and x < H and y >= 0 and y < W and S[x][y] == "#":
                counter += 1
        
        nS[i][j] = counter

for i in range(H):
    for j in range(W):
        print(nS[i][j], end="")
    print('')

