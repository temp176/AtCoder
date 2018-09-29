N = list(input())

r = []

for i in N:
    if i == '1':
        r.append('9')
    else:
        r.append('1')

print(''.join(r))

