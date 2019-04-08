N = int(input())
a = [int(i) for i in input().split()]

res = float('inf')
for i in range(-100,101):
    score = 0
    for j in a:
        score += (i-j) ** 2
    res = min(res,score)
print(res)
