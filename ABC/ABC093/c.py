A,B,C = map(int,input().split())
 
counter = 0
 
while not A == B == C:
    A,B,C = sorted([A,B,C])
    if C - A > 1:
        A += 2
        counter += 1
    else:
        A += 1
        B += 1
        counter += 1
 
print(counter)