N = int(input())
A = [int(i) for i in input().split()]

mean = 0

for i in range(len(A)):
    mean += A[i]

mean /= len(A)

min_value = 1000
min_frame = 0
for i in range(len(A)):
    tmp_value = abs(A[i] - mean)
    if min_value > tmp_value:
        min_value = tmp_value
        min_frame = i

print(min_frame)