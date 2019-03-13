N = int(input())
S = input()
x = [0]*N

if S[0] == 'I':
        x[0] += 1
else:
    x[0] -= 1

for i in range(1,N):
    if S[i] == 'I':
        x[i] = x[i-1] + 1
    else:
        x[i] = x[i-1] - 1

print(max(x) if max(x) > 0 else 0)