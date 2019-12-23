# 2019年8月27日10:49:53剑指offer 面试题63
#官方的思路好，我的思路需要考虑
a=list([9, 11, 5, 7, 16, 1, 4, 2 ])
te_v = 0
ta = [te_v for i in range(0,len(a))]
Cur_Min=a[0]
for i in range(0,len(a)):
    if(a[i]<Cur_Min):
        ta[i]=a[i]-Cur_Min
        Cur_Min=a[i]

    else:
        ta[i] = a[i] - Cur_Min

print(a)
print(ta)
print(max(ta))