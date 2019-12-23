'''
2019年8月30日15:00:17
3.背包问题

有N件物品和一个容量为V的背包。第i件物品的费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使价值总和最大。
这个问题和最长子序列值一样，一共 物品件数次 ， 每一次物品都可以选择选或者不选
转移方程：dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]] + value[i]
i是物品index，j是现在的weight
如果正向推的话，就是第一个有选或者不选，从而有两个dp[0][j]，然后第二次判断第一次的结果，最后判断全部的value

2019年8月30日17:46:38 看做二维表的问题。i是件数，j是weight，是一个二维表，递归方程
转移方程：dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]] + value[i]
要先算一个i下所有的j，再算下一个i


 '''

class dp:
    def __init__(self, i, weight):
        self.i = i
        if (i == 0):
            for j in range(0,len(a)):
                ta[j][weight]=0
            ta[i][weight - wa[i]] = a[i]
            return

        ta[i][weight] = max(ta[i][weight - a[weight - wa[i]]] + a[i], ta[i - 1][weight])

      #  ta[i][weight] = max(ta[i][weight - a[weight - wa[i]]]+a[i], ta[i - 1][weight])




a = list([0, 8 , 10 , 4 , 5 , 5])
wa =list([0, 6 , 4 , 2 , 4 , 3])
weight=10
ta=[[0 for i in range(weight+1)] for  i in range(len(a))]
v=[]
re=[v for i in range(len(a))]




for i in range(1,len(a)):
    for j in range(0,weight+1):
        if (j >= wa[i]):

            ta[i][j] = max(ta[i-1][j], ta[i-1][j-wa[i]] + a[i]);
        else:
            ta[i][j] = ta[i-1][j];


print(ta)
