A,B = map(int,input().split())

res = 0
num = 1
while num < B:
    num -= 1
    num += A
    res += 1

print(res)
