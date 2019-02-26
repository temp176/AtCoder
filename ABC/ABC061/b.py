N,M= map(int,input().split())
_input = []
for i in range(M):
    _input.append(list(map(int,input().split())))

counters = [0 for i in range(N)]

for i in range(len(_input)):
    counters[_input[i][0]-1] += 1
    counters[_input[i][1]-1] += 1

for i in range(N):
    print(counters[i])
