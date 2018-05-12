'''
def cm(a,b):
    if a[0] == b [0] or a[1] == b[0] or a[0] == b [1]:
        return True
    else:
        False

def countMatch(a):
    count = 0
    for i in range(len(a)):
        if a[i] == i+1:
            count += 1
    return count

N,M=[int(i) for i in input().split()]
P = [int(i) for i in input().split()]
XY = []
for i in range(M):
    XY.append(input().split(' '))
    XY[i][0],XY[i][1] = int(XY[i][0]),int(XY[i][1])

max = 0
check = False
for j in range(M-1):
    check = cm(XY[j],XY[j+1])

if check:
    print('わからん')
else:
    for i in range(M):
        cloneP = P[:]
        cloneP[XY[i][0]-1], cloneP[XY[i][1]-1] = cloneP[XY[i][1]-1], cloneP[XY[i][0]-1]
        count = countMatch(cloneP)
        if max < count:
            max = count
    print(max)
'''

