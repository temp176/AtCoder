N,K = map(int,input().split())
D = [str(i) for i in input().split()]

#print(D)
#print(list(str(N)))

while 1:
    check = True
    for i in D:
        if i in list(str(N)):
            check = False
            break
    if check:
        break
    
    N += 1

print(N)