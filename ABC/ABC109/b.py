N = int(input())
l = [input() for _ in range(N)] 

if len(l) != len(set(l)):
    print('No')
    exit()

for i in range(1,N):
    if l[i-1][-1] != l[i][0]:
        print('No')
        exit()

print('Yes')