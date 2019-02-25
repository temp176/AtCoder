N = int(input())
in_num = []
for i in range(N):
    in_num.append(list(map(str,input().split())))

res = 0

for x,u in in_num:
    if u == 'JPY':
        res+=float(x)
    else:
        res+= float(x)*380000.0

print(res)