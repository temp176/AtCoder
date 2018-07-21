S = list(input())
T = list(input())

slen = len(S)

for i in range(len(T)):
    if S == T:
        print('Yes')
        exit()
    else:
        slen = len(S)
        S.insert(0,S[len(S)-1])
        S.pop(len(S)-1)
print('No')