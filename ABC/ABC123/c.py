l = [int(input()) for _ in range(6)]
N = l[0]
l = l[1:]

print(-(-N//min(l))+4)
