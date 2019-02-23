S = input()
K = int(input())

if len(S) >= K and set(S[:K]) == {'1'}:
    print(1)
else:
    for i in S:
        if i != '1':
            print(int(i))
            exit()
