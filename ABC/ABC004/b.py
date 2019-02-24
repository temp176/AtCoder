import numpy as np
input_map = []
for i in range(4):
    input_map.append(list(map(str,input().split())))
res = np.rot90(np.rot90(np.array(input_map),k=-1),k=-1).tolist()
for i in res:
    print(*i)