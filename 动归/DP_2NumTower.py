'''
2019年8月30日15:00:17
2.数塔问题 ：要求从顶层走到底层，若每一步只能走到相邻的结点，则经过的结点的数字之和最大是多少？

转移方程：sum[i] = max(a[左孩子] , a[右孩子]) + a[i]

ta[i]=max(ta[i-1]+a[i],a[i])
用ma记录ta[i]所记录序列的起点
2019年8月30日16:36
 我这种写法太费时间了
2019年8月30日16:46:33
修改了。少用各种参量，每层/每个节点需要计算什么，就完事了。如果一个数，就放进dp里面，另外建议输入节点放入外面，方便调用和改
 


 '''
a = list([9, 12, 15, 10, 6, 8, 2, 18, 9, 5])
class dp:

    ta=[0 for i in range(len(a))]
    def __init__(self,i,step):
        self.i=i
        if(i==0):

            dp.ta[0]=a[0]
            return
        elif(i==int((step-1)*step/2)):#这是这一层的最左点，无左边父亲
            dp.ta[i] = a[i]+dp.ta[i-step+1]

        elif(i==int((step+1)*step/2)-1):#这是这一层的最右边点，无右边父亲
            dp.ta[i] = a[i]+dp.ta[i-step]
        else:#这是这一层的中间点，有双亲
            dp.ta[i] = a[i]+max(dp.ta[i-step],dp.ta[i-step+1])
    
t0=dp(i=0,step=1)
step=1
for i in range (1,len(a)):
    if(i==int((step+1)*step/2 )):
        step=step+1
    dp(i=i,step=step)


print(dp.ta)