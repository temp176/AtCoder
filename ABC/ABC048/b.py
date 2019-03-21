a,b,x = map(int,input().split())

def func(n):
    if n > -1:
        return n//x+1
    else:
        return 0

print(func(b)-func(a-1))