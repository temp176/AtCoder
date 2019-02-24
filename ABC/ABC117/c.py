N,M = map(int,input().split())
X = [int(i) for i in input().split()]
X.sort()
X_intvl = [0 for i in range(M-1)]

#print(X)

for i in range(1,M):
    X_intvl[i-1] = X[i] - X[i-1]

#print(X_intvl)

X_intvl.sort(reverse=True)

#print(X_intvl)

print(sum(X_intvl[N-1:]))
