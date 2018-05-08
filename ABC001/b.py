m = int(input())
m = m / 1000
if m < 0.1:
    VV = 0
elif m <= 5:
    VV = m * 10
elif m <= 30:
    VV = int(m + 50)
elif m <= 70:
    VV = int((m - 30) / 5 + 80)
else:
    VV = 89
number_padded = '{0:02d}'.format(int(VV))
print(number_padded)
