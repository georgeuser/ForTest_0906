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
    # INPUT_LINE.append([int(te_str) for te_str in line.split()])
    INPUT_LINE_str.append([te_str for te_str in line.split()])

#########################


test_len = int(INPUT_LINE_str[0][0])
test = INPUT_LINE_str[1][0]
M = int(INPUT_LINE_str[2][0])

a = list(test)
# la = list(range(26))

# for i in range(26):
#  la[i] = 0
# for i in range(0, len(a)):
# la[ord(a[i]) - 97] = la[ord(a[i]) - 97] + 1
count = 0
for times in range(M):

    Substr = INPUT_LINE_str[times + 3][0]
    substr = list(Substr)
    l_substr = list(range(26))
    #   for i in range(26):
    #      l_substr[i]=0

    #  for i in range(0, len(substr)):
    #      l_substr[ord(substr[i]) - 97] = l_substr[ord(substr[i]) - 97] + 1
    # 第一层判断：有不相同符号
    #   for i in range(26):
    #       if((la[i]==0 and l_substr[i]>0 )or (la[i]>0 and l_substr[i]==0)):
    # print('not')
    #           break
    if (len(substr) >= len(a)):
        if (a == substr[0:len(a)]):
            count = count + 1
            continue

        else:
            #   print('no')
            continue
    elif (len(substr) < len(a)):
        te_o = len(a) % len(substr)
        te_k = int((len(a) - te_o) / len(substr))
        te = []
        for i in range(te_k):
            te.extend(substr)
        if (te_o != 0):
            te.extend(substr[0:te_o])
        if (te == a):
            count = count + 1
            continue
        else:
            # print('no')
            continue
print(count)
