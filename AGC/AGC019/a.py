QHSD = [int(i) for i in input().split()]
N = int(input())

ratio = [0]*4

ratio[0] = QHSD[0]*4
ratio[1] = QHSD[1]*2
ratio[2] = QHSD[2]
ratio[3] = QHSD[3]/2

res = 0

m_index = ratio.index(min(ratio))

if m_index == 3:
    res += int(N/2) * QHSD[3]
    N -= int(N/2) * 2


m_index = ratio[:3].index(min(ratio[:3]))

if m_index == 0:
    res += int(N/0.25) * QHSD[0]
elif m_index == 1:
    res += int(N/0.5) * QHSD[1]
elif m_index == 2:
    res += N * QHSD[2]


print(res)

