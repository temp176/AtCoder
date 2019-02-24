N,K = map(int,input().split())
X = [int(i) for i in input().split()]

min_cost = float('inf')

for i in range(N-K+1):
    l = X[i]
    r = X[i+K-1]
    tmp_l = abs(l) + abs(r-l)
    tmp_r = abs(r) + abs(l-r)
    tmp = min(tmp_l,tmp_r)

    if min_cost > tmp:
        min_cost = tmp

print(min_cost)
