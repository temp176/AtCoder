A,B=[i for i in input().split()]
counter = 0
for i in range(int(A),int(B)+1):
    if str(i) == str(i)[::-1]:
        counter += 1
print(counter)
