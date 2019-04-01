def main():
    x = int(input())
    dp = [0 for _ in range(x+1)]

    for i in range(1,x+1):

        dp[i] = 1 + dp[i-1]

        sup = 0
        while 1:
            if i - 6**sup < 0:
                break
            tmp = 1 + dp[i-6**sup]
            dp[i] = min(dp[i],tmp)
            sup += 1

        sup = 0
        while 1:
            if i - 9**sup < 0:
                break
            tmp = 1 + dp[i-9**sup]
            dp[i] = min(dp[i],tmp)
            sup += 1

    print(dp[x])

if __name__ == "__main__":
    main()