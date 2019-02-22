A,B,C,D = list(input())

for op1 in ['+','-']:
    for op2 in ['+','-']:
        for op3 in ['+','-']:
            formula = A+op1+B+op2+C+op3+D
            res = eval(formula)
            if res == 7:
                print(formula+'=7')
                exit()

