N = int(input())
S = [input() for _ in range(N)] 
M = int(input())
T = [input() for _ in range(M)] 

Sw = list(set(S))
Tw = list(set(T))

mm = 0
for i in Sw:
    tmp = S.count(i) - T.count(i)
    if mm < tmp:
        mm = tmp

for i in Tw:
    tmp = S.count(i) - T.count(i)
    if mm < tmp:
        mm = tmp

print(mm)