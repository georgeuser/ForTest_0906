import sys

##################
####这一块删掉，上交代码时
file = open('input.txt')
sys.stdin = file

####################
######标准获取数据代码，就readlines.
# n = sys.stdin.readline()也可以用，是读一行，一般读第一行，然后继续用readlines()自动从第二行开始读

lines = sys.stdin.readlines()

######################
#######这一部分是自制的代码，INPUT_LINE是一个list，每一个元素是一个list，将输入的str化为了int
######建议直接对INPUT_LINE操作，每一个

INPUT_LINE = list()
INPUT_LINE_str = list()
for line in lines:
    INPUT_LINE.append([int(te_str) for te_str in line.split()])
    INPUT_LINE_str.append([te_str for te_str in line.split()])
# INPUT_LINE2 = [ int(te_str) for te_str in TESTIN[1].split() ]

#########################

TESTIN = list()
N = -1
M = 0
Di = list()
Pi = list()

Cur_Input_Line=INPUT_LINE

while(1):
    if(Cur_Input_Line==[]):
        break
    for i in range(0, len(Cur_Input_Line)):
        if (i == 0):
            N = Cur_Input_Line[0][0]
            M = Cur_Input_Line[0][1]
            continue

        if (i == N+1 and N>-1):
            TESTIN=Cur_Input_Line[i]
            Cur_Input_Line = Cur_Input_Line[i+1:]
            break

        if (i > 0 and i<N+1):

            Di.append(Cur_Input_Line[i][0])
            Pi.append(Cur_Input_Line[i][1])
            continue

    ans = list()

    for i in TESTIN:
        maxPro_te = 0
        for k in range(0, len(Di)):
            if (i >= Di[k] and Pi[k] > maxPro_te):
                maxPro_te = Pi[k]
        ans.append(maxPro_te)

    for ii in ans:
        print(ii)

    TESTIN = list()
    N = -1
    M = 0
    Di = list()
    Pi = list()
