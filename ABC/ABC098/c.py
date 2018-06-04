#TLE...

N = int(input())
S = list(input())
 
minNum = N
for i in range(N):
    cost = 0
    for j in range(N):
        if cost > minNum:
            break
        if i == j:
            continue
        if j < i:
            if S[j] == 'W':
                cost += 1
        else :
            if S[j] == 'E':
                cost += 1
    if minNum > cost:
        minNum = cost
 
print(cost-1)