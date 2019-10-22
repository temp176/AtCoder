N = int(input())
S = input()

res = 1
for i in range(len(S)-1):
    if i == len(S) - 2:
        if S[i] != S[i+1]:
            res += 1
    else:
        if S[i] != S[i+1]:
            res += 1

print(res)
