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


#########################
