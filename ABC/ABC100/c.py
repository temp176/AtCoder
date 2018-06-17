N = int(input())
A = [int(i) for i in input().split()]

total = 0
for i in A:
    counter = 0
    if i % 2 == 0:
        tmp = i
        while tmp % 2 == 0:
            tmp /= 2
            counter += 1
    total += counter
print(total)