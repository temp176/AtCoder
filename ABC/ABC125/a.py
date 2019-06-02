A,B,T = map(int,input().split())

time = A
res = 0
while time <= T + 0.5:
    res += B
    time += A

print(res)
