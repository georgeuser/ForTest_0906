import sys
import numpy as np




def factorial(n):
    temp1 = 1
    for i in range(1, n + 1):
        temp1 = temp1 * i
    return temp1%1000000007


def C(n, p):
    temp1 = 1
    for i in range(1, n + 1):
        temp1 = temp1 * i%1000000007
        y = (temp1%1000000007) / (factorial(p)%1000000007 )/ (factorial(n - p)%1000000007)
    return int(y)

n = 2
p = 1
q = 0
num_all = 0

temp1 =factorial(n)


for i in range(1, (n - q - p + 1) + 1):
    num_all = num_all + C(n, int(p + i - 1))


expect_all = 0
for i in range (1,(n - q - p + 1)+1):
    expect_all = expect_all + (p + i - 1) * C(n, p + i - 1)


expect = expect_all / num_all
re=expect%1000000007

print(expect)
print(re)
te2=333333337*3%1000000007
np.mod(4/3,1000000007)
print(te2)