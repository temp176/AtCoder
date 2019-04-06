l = [int(input()) for _ in range(6)]
k = l.pop(-1)
for i in range(1,len(l)):
    if abs(l[0] - l[i]) > k:
        print(':(')
        exit()
print("Yay!")
