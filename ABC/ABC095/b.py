N,X=[int(i) for i in input().split()]
m = [int(input()) for _ in range(N)] 

for i in range(N):
    X = X - m[i]

count = N
md = min(m) 

while X > 0:
    X = X - md
    count = count + 1

if X < 0:
    print(count - 1)
else :
    print(count)
