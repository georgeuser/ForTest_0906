'''
2019年8月30日15:00:17
1.最大连续子序列之和

给定K个整数的序列{ N1, N2, ..., NK }，其任意连续子序列可表示为{ Ni, Ni+1, ..., Nj }，其中 1 <= i <= j <= K。
最大连续子序列是所有连续子序中元素和最大的一个， 例如给定序列{ -2, 11, -4, 13, -5, -2 }，其最大连续子序列为{ 11, -4, 13 }，最大和为20。

ta[i]=max(ta[i-1]+a[i],a[i])
用ma记录ta[i]所记录序列的起点
'''
def dp(pos_i):
    if (pos_i == 0):
        ta[pos_i] = a[pos_i]
        ma[pos_i] = pos_i
        return
    if (ta[pos_i - 1] < 0):
        ta[pos_i] = a[pos_i]
        ma[pos_i] = pos_i
    else:
        ta[pos_i] = a[pos_i] + ta[pos_i-1]
        ma[pos_i] = ma[pos_i-1]



a = list([1, 3, -5, 2, 1, 5, -7, 3, 3])
ta = [0 for i in range(len(a))]#以对应底标结尾得连续list的最大值
ma= [0 for i in range(len(a))]#以对应底标结尾得连续list的起始pos底标


for i in range(len(a)):
    dp(i)
print(a)
print(ta)
print(ma)