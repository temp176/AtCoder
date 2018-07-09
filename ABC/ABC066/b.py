S = input()

resString = ''

for i in range(1,len(S)):
    resString = S[:len(S)-1-i]
    if len(resString) % 2 == 0:
        border = int(len(resString)/2)
        if resString[:border] == resString[border:]:
            print(len(resString))
            exit()
