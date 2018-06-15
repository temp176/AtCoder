S = input()

al = list("abcdefghijklmnopqrstuvwxyz")

for i in range(len(S)):
    try:
        al.remove(S[i])
    except:
        pass

if len(al) == 0:
    print('None')
else:
    print(al[0])
