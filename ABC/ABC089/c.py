import itertools

N = int(input())
S = [input() for _ in range(N)]

top = [0 for i in range(5)]
ans = 0

for i in range(N):
    if S[i][0] == 'M':
       top[0] += 1
    elif S[i][0] == 'A':
        top[1] += 1
    elif S[i][0] == 'R':
       top[2] += 1
    elif S[i][0] == 'C':
        top[3] += 1
    elif S[i][0] == 'H':
        top[4] += 1

comb = [0 for i in range(10)]
comb = list(itertools.combinations(top,3))


for i in range(len(comb)):
    mul = 1
    for j in comb[i]:
        mul *= j
    ans += mul

print(ans)