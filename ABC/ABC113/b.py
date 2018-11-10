N = int(input())
T,A = map(int,input().split())
H = [int(i) for i in input().split()]

res = - 1
res_val = 100000
for i in range(N):
    av_temp = T - H[i] * 0.006
    if res_val > abs(av_temp - A):
        res = i
        res_val = abs(av_temp - A)

print(res+1)
