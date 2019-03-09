W,a,b = map(int,input().split())

if a <= b <= a + W:
    res = 0
else:
    if a+W < b:
        res = b - (a + W)
    else:
        res = a - (b + W)

print(res)