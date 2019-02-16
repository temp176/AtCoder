N = int(input())
A = [int(i) for i in input().split()]

A.sort()

a = A[0]
b = 0
if a % 2 == 0:
    for i in A[1:]:
        if i % 2 == 1:
            b = i
            
if b < a:
    b = A[1]

b -= int(b/a) * a

if b == 0:
    print(a)
    exit()

res = 0
while b > 0 and a > 0:
    na = max(a,b)
    nb = min(a,b)
    a = na - nb
    b = nb
    res = b
    #print(a,b)

print(res)