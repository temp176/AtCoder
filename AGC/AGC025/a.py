N = int(input())

m = float("inf")
for i in range(1,N):
    A = i
    B = N - i
    factor_A = [int(x) for x in list(str(A))]
    factor_B = [int(x) for x in list(str(B))]
    tmp = sum(factor_A) + sum(factor_B)
    if m > tmp:
        m = tmp

print(m)


