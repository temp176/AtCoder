S = input()
w_count = [0]*len(S)
if S[0] == 'W':
    w_count[0] = 1

res = 0
for i in range(1,len(S)):
    if S[i] == 'W':
        res += i - w_count[i-1]
        w_count[i] = w_count[i-1] + 1
    else:
        w_count[i] = w_count[i-1]

#print(w_count)
print(res)
