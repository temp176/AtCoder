N,L = map(int,input().split())
S = [input() for _ in range(N)]
S.sort()
res = ""
for i in S:
    res += i
print(res)