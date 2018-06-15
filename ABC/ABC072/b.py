s = input()

res = ''
for i in range(1,len(s)+1):
    if i % 2 != 0:
        res += s[i-1]

print(res)