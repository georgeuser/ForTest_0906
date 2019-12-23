# 2019年8月27日10:49:53剑指offer 面试题59
# 生成两个指针，Max和Pos_SeMax
a = list([2, 3, 4, 2, 6, 2, 5, 1])
te_v = 0
ta = [te_v for i in range(0, len(a))]

wid = 3
Pos_Max = 0
Pos_SeMax = []

for i in range(0, len(a)):
    if (i < wid - 1):
        continue
    if (i - Pos_Max >= wid):  # 越界了
        if (Pos_SeMax):
            Pos_Max = Pos_SeMax
            Pos_SeMax = []
        else:
            print("Error,i pos is")
            print(i)


    if (a[i] > a[Pos_Max]):
        Pos_Max = i
        Pos_SeMax = []

    elif (a[i] <= a[Pos_Max]):

        if (Pos_SeMax == [] or a[Pos_SeMax] <= a[i]  ):
            Pos_SeMax = i
    ta[i]=a[Pos_Max]
print(ta)

