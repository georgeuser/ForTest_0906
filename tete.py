def dp(pos_i):
    if (pos_i == 0):
        start_ta[pos_i] = pos_i
        end_ta[pos_i] = pos_i
        return
    if (a[pos_i]>a[pos_i-1]):
        start_ta[pos_i] = start_ta[pos_i-1]
        end_ta[pos_i] = pos_i
    else:
        start_ta[pos_i] = pos_i
        end_ta[pos_i] = pos_i



a = list([1, 3, -5, 2, 1, 5, 6,-7, 3, 3])


start_ta = [0 for i in range(len(a))]#以对应底标结尾得连续list的最大值
end_ta= [0 for i in range(len(a))]

for i in range(len(a)):
    dp(i)
print(2)