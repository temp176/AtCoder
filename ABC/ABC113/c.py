N,M = map(int,input().split())
PY = []
tmp = []
cheker = []
res = []
for i in range(M):
    tmp = list(map(int,input().split()))
    tmp.append(i)
    PY.append(list(tmp))
    res.append('')

sorted_py = sorted(PY, key=lambda x: x[1])
checker = [0 for i in range(N)]

for i in range(M):
    index = sorted_py[i][0]-1
    checker[index] += 1
    res[sorted_py[i][2]] = str(sorted_py[i][0]).zfill(6) + str(checker[sorted_py[i][0]-1]).zfill(6)

for i in range(M):
    print(res[i])