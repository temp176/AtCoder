N = int(input())
res = ""

while N != 0:
    if N % 2 != 0:
        N -= 1
        res = "1" + res
    else:
        res = "0" + res
    
    N /= -2

if res == "":
    res = "0"
    
print(res)