N = int(input())
AB = []
for i in range(N):
    AB.append(list(map(int,input().split())))

AB.sort(key=lambda x:x[0]+x[1],reverse=True)

T = 0
A = 0
for i in range(N):
    if i % 2 == 0:
        T += AB[i][0]
    else:
        A += AB[i][1]

print(T-A)