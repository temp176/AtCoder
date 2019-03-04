S = input()

count_z = S.count('0')
count_o = S.count('1')

if count_o < 1 or count_z < 1:
    print(0)
else:
    print(min(count_z,count_o)*2)