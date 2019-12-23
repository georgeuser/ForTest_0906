'''
2019年8月30日15:00:17
1.最大连续子序列之和

给定K个整数的序列{ N1, N2, ..., NK }，其任意连续子序列可表示为{ Ni, Ni+1, ..., Nj }，其中 1 <= i <= j <= K。
最大连续子序列是所有连续子序中元素和最大的一个， 例如给定序列{ -2, 11, -4, 13, -5, -2 }，其最大连续子序列为{ 11, -4, 13 }，最大和为20。

ta[i]=max(ta[i-1]+a[i],a[i])
用ma记录ta[i]所记录序列的起点
2019年8月30日16:36
 我这种写法太费时间了
 而且从底层往上层想好想大概


 '''
class dp:
    a = list([9, 12, 15, 10, 6, 8, 2, 18, 9, 5])
    nodepointlist=[0 for i in range(len(a))]
    noderesult=[0 for i in range(len(a))]

    def calMax(self,doublefathersign):
        if(doublefathersign==0):
             self.re = dp.a[self.i]+ dp.nodepointlist[self.i-self.step+1].re
             dp.noderesult[self.i]=self.re
             return

        if (doublefathersign == 1):
            self.re = dp.a[self.i] + dp.nodepointlist[self.i - self.step].re
            dp.noderesult[self.i] = self.re
            return
        if (doublefathersign == 2):
            self.re = dp.a[self.i] + max(dp.nodepointlist[self.i - self.step].re, dp.nodepointlist[self.i - self.step + 1].re)
            dp.noderesult[self.i] = self.re
            return

    def __init__(self,i,step=0):

        self.step=step
        self.i=i
        dp.nodepointlist[i] = self
        if(i==0):
            dp.nodepointlist[i]=self
            self.re=dp.a[i]
            return

      #I.先判断father是不是两个
        #判断单亲：
        if(self.i==int((self.step-1)*self.step/2 ) ):#左边或者右边最后一个，单亲
            self.calMax(doublefathersign=0)#没有左父亲,一行中最小的
        elif(self.i == int((self.step + 1) * self.step / 2) - 1):
          self.calMax(doublefathersign=1)  # 没有右父亲，一行中最大
        else:#不是单亲，有双亲
         #   dp.nodepointlist[i].calMax(doublefathersign=1)
            self.calMax(doublefathersign=2)

t0=dp(i=0,step=1,forward=None)
step=1
for i in range (1,len(dp.a)):
    if(i==int((step+1)*step/2 )):
        step=step+1
    dp.nodepointlist[i]=dp(i=i,step=step,forward=None)


print(2)