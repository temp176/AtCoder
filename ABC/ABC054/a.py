A,B = map(int,input().split())
if A == B:
    print('Draw')
elif A == 1:
    print('Alice')
elif B == 1:
    print('Bob')
else:
    print('Alice' if A > B else 'Bob')