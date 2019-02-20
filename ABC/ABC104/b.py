S = input()

if S[0] == 'A':
    S = S[1:]
    index = 0
    i_count = 1
    count = 0
    for i in S[1:-1]:
        if i == 'C':
            count += 1
            index = i_count
        i_count += 1
    if count == 1:
        S = S[0:index] + S[index+1:]
        if S.islower():
            print('AC')
            exit()

print('WA')

