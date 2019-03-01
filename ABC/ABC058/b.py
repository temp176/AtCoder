O = input()
E = input()

res = ''
o,e = 0,0
for i in range(len(O+E)):
    if i % 2 == 0:
        res += O[o]
        o +=1
    else:
        res += E[e]
        e += 1

print(res)