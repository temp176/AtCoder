N = int(input())
S = [i for i in input().split()]
if len(set(S)) == 3:
    print('Three')
else:
    print('Four')
