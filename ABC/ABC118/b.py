N,M = map(int,input().split())
res = []
for i in range(N):
    res.append(list(map(int,input().split())))

if N == 1:
    print(res[0][0])
    exit()

s = [0 for i in range(M)]
for i in res:
    for j in i[1:]:
        #print(j)
        s[j-1] += 1

#print(s)

count = 0
for i in range(M):
    if s[i] == N:
        count += 1

print(count)