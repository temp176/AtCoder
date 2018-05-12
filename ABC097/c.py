s = list(input())
k = int(input())
sub = []
sub += s[:]
 
for j in range(2,k+1):
    charGram = [''.join(s[i:i+j]) for i in range(len(s)-1)]
    sub += charGram
sub = list(set(sub))
print(sorted(sub)[k-1])