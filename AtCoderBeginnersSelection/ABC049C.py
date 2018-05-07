wl = ['dream','dreamer','erase','eraser']
S = input()
i = 0
for i in range(4):
    S = S.replace(wl[3-i],'')
if len(S) == 0:
    print('YES')
else:
    print('NO')