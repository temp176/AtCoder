W,H,N = map(int,input().split())

_input = []
for i in range(N):
    _input.append(list(map(int,input().split())))

rec = [[0 for i in range(W)] for j in range(H)]

for x,y,a in _input:
    if a == 1:
        for i in range(H):
            for j in range(x):
                rec[i][j] = 1

    elif a == 2:
        for i in range(H):
            for j in range(x,W):
                rec[i][j] = 1

    elif a == 3:
        for i in range(y):
            for j in range(W):
                rec[i][j] = 1
    
    else:
        for i in range(y,H):
            for j in range(W):
                rec[i][j] = 1

res = 0
for i in range(H):
    for j in range(W):
        if rec[i][j] == 0:
            res += 1

print(res)


