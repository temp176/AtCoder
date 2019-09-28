A,B,C = map(int,input().split())
res = 0
if A <= B:
    while C > 0:
        C -= A
        res += 1
else:
    while C > 0:
        C -= B
        res += 1

if C < 0:
    res -= 1

print(res)
