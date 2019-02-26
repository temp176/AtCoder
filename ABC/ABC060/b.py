A,B,C = map(int,input().split())

for i in range(100000):
    if (B*i+C)%A == 0:
        print('YES')
        exit()

print('NO')