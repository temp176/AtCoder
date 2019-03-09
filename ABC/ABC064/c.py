N = int(input())
A = [int(i) for i in input().split()]

counts = [0]*9

for i in A:
    color = int(i/400)
    if color > 8:
        color = 8
    counts[color] += 1

#print(counts)

v = 8 - counts[:-1].count(0)

if counts[-1] == 0:
    print(v,v)
else:
    if v == 0:
        print(1,counts[-1])
    else :
        print(v,v+counts[-1])





