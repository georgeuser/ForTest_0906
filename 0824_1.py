

#标准输入截取
import sys
TESTIN=list()
try:
    count=1
    while True:
      # line = sys.stdin.readline().strip()
        line = sys.stdin.readline().strip()
        if line == '':
            break


        if(count==1):
            TESTIN.append(line)
            count=count+1
            continue

        if (count > 1):
            TESTIN.append(line)
            count = count + 1
            continue
except:
    pass

INPUT_LINE1 = [ int(te_str) for te_str in TESTIN[0].split() ]

MaxEquVal=0
te1=INPUT_LINE1[0]+INPUT_LINE1[1]+INPUT_LINE1[2]
te2=INPUT_LINE1[0]+INPUT_LINE1[1]*INPUT_LINE1[2]
te3=INPUT_LINE1[0]*INPUT_LINE1[1]+INPUT_LINE1[2]
te4=INPUT_LINE1[0]*INPUT_LINE1[1]*INPUT_LINE1[2]
te5=(INPUT_LINE1[0]+INPUT_LINE1[1])*INPUT_LINE1[2]
te6=INPUT_LINE1[0]*(INPUT_LINE1[1]+INPUT_LINE1[2])

MaxEquVal=max(te1,te2,te3,te4,te5,te6)
print(MaxEquVal)