N = int(input())
D = [0 for i in range(N)]
for i in range(0,N):
    D[i] = int(input())
mochi = set(D)
print(len(mochi))