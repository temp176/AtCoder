import math

xa,ya,xb,yb,xc,yc = map(int,input().split())

dist_ab = math.sqrt((xa-xb)**2 + (ya-yb)**2)
dist_bc = math.sqrt((xb-xc)**2 + (yb-yc)**2)
dist_ca = math.sqrt((xa-xc)**2 + (ya-yc)**2)

s = (dist_ab + dist_bc + dist_ca)/2
res = math.sqrt(s*(s-dist_ab)*(s-dist_bc)*(s-dist_ca))

print(round(res,1))
