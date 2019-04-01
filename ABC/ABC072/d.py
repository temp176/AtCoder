N = int(input())
P = [int(i) for i in input().split()]

count = 0
pre = False
for i in range(1,N+1):
    if P[i-1] == i:
        if pre:
            pre = False
        else:
            count += 1
            pre = True
    else:
        pre = False

print(count)