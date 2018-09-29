import collections
 
n = int(input())
v = [int(i) for i in input().split()]
 
v1 = [v[i] for i in range(0,n,2)]
v2 = [v[i] for i in range(1,n,2)]
 
count1 = collections.Counter(v1).most_common(2)
count2 = collections.Counter(v2).most_common(2)

if count1[0][0] != count2[0][0]:
    res = len(v1) - count1[0][1] + len(v2) - count2[0][1]
    print(res)
else:
    if len(count1) == 1:
        print(len(v1))
    else:
        res1 = len(v1) - count1[0][1] + len(v2) - count2[1][1]
        res2 = len(v1) - count1[1][1] + len(v2) - count2[0][1]
        print(min(res1,res2))
