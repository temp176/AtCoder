A,B,K = map(int,input().split())

if B - A + 1 < K * 2:
    for i in range(A,B+1):
        print(i)
else:
    for i in range(A,min(B,A + K)):
        print(i)

    for i in range(max(B - K + 1,A + K),B + 1):
        print(i)