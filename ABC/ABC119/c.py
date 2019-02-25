N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]
INF = 10 ** 9

def dfs(cur, a, b, c):
    '''
    深さがNだったら使用MPを評価
    N本の竹を使うときに必要な合成回数はN-1のため，最後に-1*10*3(?)
    1本も竹を使用していなかったら棄却→MPを無限に使うこととしている
    '''
    if cur == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF

    '''
    cur番目の竹に対して
        ret0:ABCどれにも使わない
        ret1:Aに使う（合成:MP+10）
        ret2:Bに使う（合成:MP+10）
        ret3:Cに使う（合成:MP+10）
    '''
    ret0 = dfs(cur + 1, a, b, c)
    ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
    ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
    ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
    return min(ret0, ret1, ret2, ret3)
print(dfs(0, 0, 0, 0))