s = input()
res = ""
for i in range(len(s)):
    if s[i] == 'B' and len(res) > 0:
        res = res[:-1]
    elif s[i] != 'B':
        res += s[i]

print(res) 