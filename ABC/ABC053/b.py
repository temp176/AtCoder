s = input()
res = 0
index_a = -1
index_z = -1
for i in range(len(s)):
    if s[i] == 'A':
        index_a = i
        for j in range(len(s[i:])):
            if s[i+j] == 'Z':
                index_z = i+j
        break

#print(index_a,index_z)
print(index_z - index_a + 1)