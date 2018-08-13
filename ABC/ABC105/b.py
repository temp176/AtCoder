N = int(input())

for i in range(100):
    for j in range(100):
        if i * 4 + j * 7 == N:
            print('Yes')
            exit()

print('No')