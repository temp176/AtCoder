N = int(input())
C = input()
res_min = min(C.count('1'),C.count('2'),C.count('3'),C.count('4'))
res_max = max(C.count('1'),C.count('2'),C.count('3'),C.count('4'))
print(res_max,res_min)
    