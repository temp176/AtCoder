'''
X = int(input())
i = 1
while i**2 <= X:
    i += 1
if i != 1:
    print((i-1)**2)
else:
    print(1)
'''
X = int(input())
num = 1
max = 0
for i in range(1,X):
    for j in range(2,X):
        num = i ** j
        if num > X:
            break
        if max < num:
            max = num
if max != 0:
    print(max)
else:
    print(1)
