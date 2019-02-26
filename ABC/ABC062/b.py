H,W = map(int,input().split())
_input = []
for i in range(H):
    row = list(map(str,input().split()))
    row = '#' + row[0] + '#'
    _input.append(row)

for i in range(H+2):
    if i == 0 or i == H+1:
        for j in range(W+2):
            if j == W+1:
                print('#')
            else:
                print('#',end='')
    else:
        print(_input[i-1])
