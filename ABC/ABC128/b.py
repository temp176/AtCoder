N = int(input())
_input = []
for i in range(N):
    _input.append([i+1] + list(map(str,input().split())))

_input.sort(key=lambda x:(x[1],-int(x[2])))

for i in range(N):
    print(_input[i][0])
