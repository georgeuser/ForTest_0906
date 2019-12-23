# 标准输入截取
import sys

TESTIN = list()
N = 100
M =0
Di =list()
Pi =list()

try:
    count = 0
    while True:
        # line = sys.stdin.readline().strip()
        line = sys.stdin.readline().strip()
        count = count + 1

        if line == '':
            break

        if (count == 1):
            lines = line.split()
            N = int(lines[0])
            M = int(lines[1])

            continue



        if (count > 1 and count <N +2 ):
            lines = line.split()
            Di.append(int(lines[0]))
            Pi.append(int(lines[1]))

            continue

        if (count == N +2):
            TESTIN.append(line)

            break
except:
    pass

INPUT_LINE=list()
for i in TESTIN:
    INPUT_LINE.append([int(te_str) for te_str in i.split()])
# INPUT_LINE2 = [ int(te_str) for te_str in TESTIN[1].split() ]

#INPUT_LINE是正式的内容



ans=list()

for i in INPUT_LINE:
    maxPro_te=0
    for j in i:
        for k in range(0,len(Di)):
            if(j>=Di[k] and Pi[k]>maxPro_te):
                maxPro_te=Pi[k]
        ans.append(maxPro_te)
for ii in ans:
    print(ii)