# dp典型题，coin/骰子
#有a种硬币，面值随意
#问达到某个value时最少使用的硬币
#状态转移方程 for j in a,dp（value）=min(dp（value-j）+1)
a = list([2, 4,5])
INFINITY=999
v = 0
ta = [v for i in range(100)]

ta[0] = 0#重复的放表里备查
for j in a:
    ta[j]=1

def dp(value):
    assert value >= 0, "Err Input"

    SetCoins = INFINITY;
    if (value == 0):
        return 0

    for j in a:
        if (value - j < 0):
            break
        if(ta[value - j]!=0):#已经计算了
            temp = ta[value - j] + 1
        elif (dp(value - j) == INFINITY):  # 上一次结果是无法完成
            break
        else:
            temp = dp(value - j) + 1
        if (temp > 0 and temp < SetCoins):
            SetCoins = temp
    if (SetCoins < INFINITY and SetCoins > 0):
        ta[value] = SetCoins
    return SetCoins


print(dp(3))
print(dp(4))
print(dp(7))
print(dp(10))
print(dp(12))
print(dp(22))
