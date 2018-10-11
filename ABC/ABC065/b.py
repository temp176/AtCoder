N = int(input())
a = [int(input()) for _ in range(N)]

lu = a[0] - 1
count = 0

for i in range(N):
    count += 1
    if lu == 1:
        print(count)
        exit()
    lu = a[lu] - 1

if lu == 1:
    print(count)
else:
    print(-1)
