import random
import time
import copy

N,M,L= map(int,input().split())
S = [list(input()) for _ in range(N)]

def init_board(M):
    board = [list('.' * M) for i in range(M)]
    
    for i in range(M):
        board[0][i] = '#'
        board[-1][i] = '#' 
    for i in range(1,M-1):
        board[i][0] = '#'
        board[i][-1] = '#'
    
    return board

def output_board(board,M):
    for i in range(M):
        output = ''
        for j in range(M):
            output += board[i][j]
        print(output)

''' シミュレータ'''
def Move(pos,direction,board):
    if direction == 0:
        if board[pos[0]-1][pos[1]] == '#':
            pass
        else:
            pos[0] -= 1
    elif direction == 1:
        if board[pos[0]][pos[1]+1] == '#':
            pass
        else:
            pos[1] += 1
    elif direction == 2:
        if board[pos[0]+1][pos[1]] == '#':
            pass
        else:
            pos[0] += 1
    elif direction == 3:
        if board[pos[0]][pos[1]-1] == '#':
            pass
        else:
            pos[1] -= 1
    
    return pos

def Rotate_R(direction):
    direction += 1
    if direction == 4:
        direction = 0
    return direction

def Rotate_L(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

def sq_R(pos,direction,s,board):
    if s == 'R' or s == 'L':
        direction = Rotate_R(direction)
    else:
        pos = Move(pos,direction,board)
    
    return pos,direction

def sq_L(pos,direction,s,board):
    if s == 'R' or s == 'L':
        direction = Rotate_L(direction)
    else:
        pos = Move(pos,direction,board)
    
    return pos,direction

def sq_D(pos,direction,s,board):
    for i in range(2):
        if s == 'R':
            direction = Rotate_R(direction)
        elif s == 'L':
            direction = Rotate_L(direction)
        else:
            pos = Move(pos,direction,board)
    return pos,direction

def sq_T(pos,direction,s,board):
    for i in range(3):
        if s == 'R':
            direction = Rotate_R(direction)
        elif s == 'L':
            direction = Rotate_L(direction)
        else:
            pos = Move(pos,direction,board)
    return pos,direction

def sq_Dot(pos,direction,s,board):
    if s == 'R':
        direction = Rotate_R(direction)
    elif s == 'L':
        direction = Rotate_L(direction)
    else:
        pos = Move(pos,direction,board)
    return pos,direction

def calc_score(score_board):
    score = 0
    lower_index = [0,0]
    lower_value = 0
    for i in range(M):
        for j in range(M):
            if score_board[i][j] > lower_value:
                lower_value = score_board[i][j]
                lower_index[0] = i
                lower_index[1] = j

            if score_board[i][j] == 1:
                score += 10
            elif score_board[i][j] == 2:
                score += 3
            elif score_board[i][j] == 3:
                score += 1
    return score,lower_index[0],lower_index[1]

def simulate(board,M,S):
    score_board = [[0] * M for i in range(M)]
    for i in range(N):
        pos = [int(M/2),int(M/2)]
        direction = 0
        for j in range(L):
            #print(S[i][j],pos,direction)
            if board[pos[0]][pos[1]] == 'R':
                pos,direction = sq_R(pos,direction,S[i][j],board)
            elif board[pos[0]][pos[1]] == 'L':
                pos,direction = sq_L(pos,direction,S[i][j],board)
            elif board[pos[0]][pos[1]] == 'D':
                pos,direction = sq_D(pos,direction,S[i][j],board)
            elif board[pos[0]][pos[1]] == 'T':
                pos,direction = sq_T(pos,direction,S[i][j],board)
            else:
                pos,direction = sq_Dot(pos,direction,S[i][j],board)

        score_board[pos[0]][pos[1]] += 1

    score,index1,index2 = calc_score(score_board)
    return score,index1,index2

# ボードをランダムに変更
def create_rand_board(board,M,square_list):
    for i in range(1,M-1):
        for j in range(1,M-1):
            if i == int(M/2) and j == int(M/2):
                board[i][j] = square_list[random.randint(1,4)]
            else:
                board[i][j] = square_list[random.randint(0,4)]
    return board

#  ボードの一部をランダムに変更(r:変更する範囲の大きさ)
def alt_part_rand_board(board,M,square_list):
    r = 20
    start_i = random.randint(1,(M-r-1))
    start_j = random.randint(1,(M-r-1))
    for i in range(start_i,start_i+r):
        for j in range(start_j,start_j+r):
            if i == int(M/2) and j == int(M/2):
                board[i][j] = square_list[random.randint(1,4)]
            else:
                board[i][j] = square_list[random.randint(0,4)]
    return board

# ボードのnumマスをランダムに変更する(範囲を変えてみる)
def alt_point_rand_board(board,M,square_list,num):
    for i in range(num):
        index_i = random.randint(1,M-2)
        index_j = random.randint(1,M-2)
        if index_i == int(M/2) and index_j == int(M/2):
            board[index_i][index_i] = square_list[random.randint(1,4)]
        else:
            board[index_i][index_j] = square_list[random.randint(0,4)]
    return board

square_list = {
    0:'#',
    1:'D',
    2:'T',
    3:'L',
    4:'R'
}

start_time = time.time()
time_limit = 2.8

#count = 0

lower_index = [0,0]

board = init_board(M)
best_board = init_board(M)
score_best,lower_index[0],lower_index[1] = simulate(board,M,S)

num = 2

while time.time() - start_time < time_limit:
    board = alt_point_rand_board(board,M,square_list,num)
    board[lower_index[0]][lower_index[1]] == '#'
    score_tmp,lower_index[0],lower_index[1] = simulate(board,M,S)
    if score_tmp >= score_best:
        score_best = score_tmp
        best_board = copy.deepcopy(board)
    board = copy.deepcopy(best_board)
output_board(best_board,M)

#print(count)

