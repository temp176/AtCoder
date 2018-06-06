N = int(input())
S = list(input())

reS = S[::-1]

wSum = [0 for i in range(N)]
eSum = [0 for i in range(N)]

for i in range(N):
    if i == 0:
        if S[i] == 'W':
            wSum[i] = 1
        if reS[i] == 'E':
            eSum[i] = 1
    else:
        if S[i] == 'W':
            wSum[i] = wSum[i-1] + 1
        else:
            wSum[i] = wSum[i-1]
        if reS[i] == 'E':
            eSum[i] = eSum[i-1] + 1
        else:
            eSum[i] = eSum[i-1]

eSum = eSum[::-1]

cost = eSum[1]

for i in range(1,N):
    if i == N - 1:
        if cost > wSum[N-2]:
            cost = wSum[N-2]
    else:
        if cost > wSum[i-1] + eSum[i+1]:
            cost = wSum[i-1] + eSum[i+1]
print(cost)
