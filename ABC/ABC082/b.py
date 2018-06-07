s = list(input())
t = list(input())

s.sort()
t.sort()
t = t[::-1]

if s < t:
    print('Yes')
else:
    print('No')

