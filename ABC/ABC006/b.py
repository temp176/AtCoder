def main():
    n = int(input())
    if n < 4:
        if n < 3:
            print(0)
        else:
            print(1)
        exit()

    a1 = 0
    a2 = 0
    a3 = 1
    for i in range(3,n):
        tmp = sum([a1,a2,a3])
        a1 = a2 % 10007
        a2 = a3 % 10007
        a3 = tmp % 10007

    print(a3%10007)

if __name__ == "__main__":
    main()


