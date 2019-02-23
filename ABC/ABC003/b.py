S = input()
T = input()

replace_words = ['a','t','c','o','d','e','r']

for i in range(len(S)):
    if T[i] != S[i]:
        if T[i] == '@':
            if S[i] not in replace_words:
                print('You will lose')
                exit()
        elif S[i] == '@':
            if T[i] not in replace_words:
                print('You will lose')
                exit()
        else:
            print('You will lose')
            exit()

print('You can win')


