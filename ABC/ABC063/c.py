N = int(input())
S = [int(input()) for _ in range(N)]

S = sorted(S)

if sum(S) % 10 != 0:
    print(sum(S))
    exit()

mod_list = [i%10 for i in S]

#print(mod_list)

if sum(mod_list) == 0:
    print(0)
    exit()

for i in range(len(mod_list)):
    if mod_list[i] != 0:
        print(sum(S) - S[i])
        exit()

