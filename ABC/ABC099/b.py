a,b=[int(i) for i in input().split()]

d = b - a

h = 0
for i in range(1,d):
    h += i

print(h-a)
