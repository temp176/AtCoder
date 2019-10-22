import itertools

N = int(input())
D = [int(i) for i in input().split()]

comb_list = list(itertools.combinations(D,2))

res = 0
for comb in comb_list:
    res += comb[0] * comb[1]

print(res)


