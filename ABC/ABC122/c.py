def main():
    N,Q = map(int,input().split())
    S = input()
    lr = []
    for i in range(Q):
        lr.append(list(map(int,input().split())))

    cl = [0 for _ in range(len(S))]

    for i in range(1,len(S)):
        if S[i] == 'C' and S[i-1] == 'A':
            cl[i] = cl[i-1] + 1
        else:
            cl[i] = cl[i-1]


    #print(cl) 
    #print(S)

    for l,r in lr:
        res = cl[r-1] - cl[l-1] 
        print(res)


if __name__ == "__main__":
    main()
