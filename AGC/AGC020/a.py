N,A,B = map(int,input().split())

if A - N == 0:
    print('Borys')
elif abs(A-B) % 2 == 0:
    print('Alice')
else:
    print('Borys')