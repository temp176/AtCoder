
def main():
    A,B,C,D,E,F = map(int,input().split())

    x_list = []
    for i in range(F+1):
        for j in range(F+1):
            x = 100*A*i + 100*B*j
            if x <= F:
                x_list.append(x)

    y_list = []
    for i in range(F+1):
        for j in range(F+1):
            y = i*C + j*D
            if y <= F:
                y_list.append(y)

    res = 0
    res_x = 0
    res_y = 0

    x_list = list(set(x_list))
    y_list = list(set(y_list))

    for x in x_list:
        for y in y_list:
            if x + y > F:
                continue

            if y == 0:
                tmp = 0
            else:
                tmp = y/(x+y)

            if tmp > E/(100+E):
                continue

            if res <= tmp:
                res = tmp
                res_x = x
                res_y = y


    print(res_x+res_y,res_y)

if __name__ == "__main__":
    main()






