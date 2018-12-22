N,x = map(int,input().split())
a = [int(i) for i in input().split()]

a.sort()

counter = 0
for i in range(len(a)):
    x = x - a[i]
    if x < 0:
        break
    counter = counter + 1

if x > 0:
    counter = counter - 1

print(counter)
