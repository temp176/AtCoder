input = [int(i) for i in input().split()]

N = input[0]
Y = input[1]

ans = False
total = 0

for i in range(0,N+1):
    for j in range(0,(N+1-i)):
        total = 10000 * i + 5000 * j + (N-i-j) * 1000
        if Y == total:
            print(i,j,(N-i-j))
            ans = True
            break
    else:
        continue
    break
if ans == False:

    print(-1,-1,-1)