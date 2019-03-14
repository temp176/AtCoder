def dfs(n,a,b,c):
    if n == N:
        return abs(A-a)+abs(B-b)+abs(C-c) - 30 if min(a,b,c) > 0 else float('inf')

    ret1 = dfs(n+1,a+l[n],b,c) + 10
    ret2 = dfs(n+1,a,b+l[n],c) + 10
    ret3 = dfs(n+1,a,b,c+l[n]) + 10
    ret4 = dfs(n+1,a,b,c)

    return min(ret1,ret2,ret3,ret4)



if __name__ == "__main__":
    N,A,B,C = map(int,input().split())
    l = [int(input()) for _ in range(N)]
    print(dfs(0,0,0,0))