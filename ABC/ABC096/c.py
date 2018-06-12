H, W = map(int, input().split())
a = []
tmp = []
for i in range(H):
    tmp = list(map(str,input().split()))
    a.append(list(tmp[0]))

for i in range(H):
    for j in range(W):
        if a[i][j] == '#':
            if j - 1 >= 0 and a[i][j - 1] == "#":
                continue
            elif j + 1 < W and a[i][j + 1] == "#" :
                continue
            elif i + 1 < H and a[i + 1][j] == "#" :
                continue
            elif i - 1 >= 0 and a[i - 1][j] == "#":
                continue
            else:
                print("No")
                exit()
 
print("Yes")