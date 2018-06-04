A,B=[int(i) for i in input().split()]
S = input()

if S[A] == '-' and S.count('-') == 1:
    print('Yes')
else:
    print('No')