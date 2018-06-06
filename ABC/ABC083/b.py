input = [int(i) for i in input().split()]
N = input[0]
A = input[1]
B = input[2]
 
total = 0
for i in range(1,N+1):
    sums = sum(list(map(int,str(i))))
    if A <= sums <= B:
        total += i
print(total)