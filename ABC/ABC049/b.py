H,W = map(int,input().split())
_input = []
for i in range(H):
    row = list(map(str,input().split()))
    _input.append(list(row[0]))

for i in range(2*H):
    row = ""
    for j in range(W):
        row += _input[int(i/2)][j]
    print(row)