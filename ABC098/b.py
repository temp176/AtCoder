N = int(input())
S = list(input())
maxNum = 0
for i in range(1,N):
    X = set(S[:i])
    Y = set(S[i:])
    n = len(X & Y)
    if maxNum < n:
        maxNum = n
print(maxNum)