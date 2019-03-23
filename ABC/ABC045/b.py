Sa = input()
Sb = input()
Sc = input()

turn = 'a'

while 1:
    if turn == 'a':
        if not Sa:
            print('A')
            exit()
        turn = Sa[0]
        Sa = Sa[1:]
    elif turn == 'b':
        if not Sb:
            print('B')
            exit()
        turn = Sb[0]
        Sb = Sb[1:]
    else:
        if not Sc:
            print('C')
            exit()
        turn = Sc[0]
        Sc = Sc[1:]
