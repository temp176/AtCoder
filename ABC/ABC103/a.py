A = [int(i) for i in input().split()]

total = 0
tmp = 0
for i in range(3):
    if i == 0:
        total += 0
    else:
        total += abs(tmp-min(A))
    tmp = min(A)
    A.remove(min(A))

print(total)
