N = int(input())
odd_num = 0

for num in range(1,N+1):
    if num % 2 == 1:
        odd_num += 1

print(odd_num/N)