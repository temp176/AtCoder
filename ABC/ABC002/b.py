W = input()
res = ""
for i in W:
    if i not in ['a','i','u','e','o']:
        res += i
print(res)