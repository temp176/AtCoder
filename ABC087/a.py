inputNum = [int(input()) for _ in range(3)] 
inputNum[0] -= inputNum[1]
print(inputNum[0] - inputNum[2] * int(inputNum[0]/inputNum[2]))
