N = int(input())

if N%2 == 0:
    res = 0
    for i in range(2,N,2):
        res += i
    print(res*2)
else:
    res = 0
    for i in range(1,N-2,2):
        res += i
    print(res*2+N-2)