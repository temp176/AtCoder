import copy

S = list(input())
T = list(input())

c = {}
for i in range(len(S)):
    if S[i] in c:
        if c[S[i]] != T[i]:
            print('No')
            exit()
    elif T[i] in c.values():
        ct = copy.copy(c)
        ct[S[i]] = T[i]
        keys = [k for k, v in ct.items() if v == T[i]]
        if len(set(keys)) != 1:
            print('No')
            exit()
    else:
        c[S[i]] = T[i]
    
print('Yes')