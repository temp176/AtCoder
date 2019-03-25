S = input()

st = ['A', 'C', 'G', 'T']

res = 0

for i in range(len(S)+1):
    for j in range(1,len(S)+1):
        flag = True
        if -j+1 == 0:
            #print(S[i:])
            for k in S[i:]:
                if k not in st:
                    flag = False
                    break
        
            if flag:
                res = max(res,len(S[i:]))
        
        else:
            for k in S[i:-j+1]:
                if k not in st:
                    flag = False
                    break
            
            if flag:
                res = max(res,len(S[i:-j+1]))

print(res)

