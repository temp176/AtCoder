def genetarete_num(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int(3*n+1)

s = int(input())

num = genetarete_num(s)

if num == s:
    print(2)
    exit()

num_list = [s,num]

for i in range(3,1000001):
    num = genetarete_num(num)
    if num in num_list:
        print(i)
        exit()
    num_list.append(num)
