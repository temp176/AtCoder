N,M,C = map(int,input().split())
B = [int(i) for i in input().split()]
_input = []
for i in range(N):
    _input.append(list(map(int,input().split())))

res = 0

for A in _input:
    cal = 0
    for a,b in zip(A,B):
        cal += a * b
    if cal + C > 0:
        res += 1

print(res)


