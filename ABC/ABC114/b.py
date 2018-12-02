S = list(input())

res = 753

for i in range(len(S)-2):
    X = ''
    for i in S[i:i+3]:
        X += i 
    X = int(X)
    tmp = abs(753-X)
    if tmp < res:
        res = tmp

print(res)