import itertools
def bit(n, m):
    bit_list = list(itertools.product([i for i in range(m)], repeat=n))
    return bit_list

l = [int(input()) for _ in range(5)]
bit = bit(5,5)
bit_n = []
for i in bit:
    if len(set(i)) == 5:
        bit_n.append(i)

res = float("inf")
for i in bit_n:
    time = 0
    for j in i:
        if time == 0:
            time += l[j]
        else:
            if time % 10 != 0:
                while time % 10 != 0:
                    time += 1
                time += l[j]
            else:
                time += l[j]
    if res > time:
        res = time

print(res)
