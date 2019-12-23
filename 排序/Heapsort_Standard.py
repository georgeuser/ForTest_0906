import numpy as np
import math
# 2019年4月2日15:00:40
# 堆支持以下的基本操作:
#
#     build:建立一个空堆；         build函数
#     insert:向堆中插入一个新元素；    append new元素，然后siftdown
#     update：将新元素提升使其符合堆的性质；        siftdown 就行
#     get：获取当前堆顶元素的值；
#     delete：删除堆顶元素；
#     heapify：使删除堆顶元素的堆再次成为堆。

class heap:
    def __init__(self,a):
        self.n=len(a)
        self.data=a
        self.build(a)
        print(self.data)
        self.heapsort()
        print(self.data)

    def build(self,a):
   #注：这里所有的节点是从0开始的，也就是根节点是0节点，为了和数组统一（数组的第一个元素是a[0]）
   #根节点是1节点，则第一个不是叶节点的节点为int(self.n/2)
   #根节点是0节点，则第一个不是叶节点的节点为int(self.n/2)-1
        times=int(self.n/2)-1##向下取整
        for i in range(times,-1,-1):#从倒数二层最后一个节点，到0节点（堆顶是0节点不是1节点）
            self.siftdown(i);#整理堆使其满足最小堆的性质，其实是从大节点往1节点上去

    def heapsort(self):
       while(self.n>1):
            self.swap(0,self.n-1)
            self.n=self.n-1
            self.siftdown(0)



    def siftdown(self,i):

        if(i<0 or i>(int(self.n/2)-1)):#没有子节点或溢出
            return
        #先跟左节点比较；一个父节点的左节点是其下标的2k+1，右节点是其父节点下标的2K+2。
        if(self.data[i]>self.data[i*2+1]):
            self.swap(i,i*2+1)
            self.siftdown(i*2+1)

        #再跟右边比较,跟右边比较需要先判断有没有右子点
        if(self.n>2*i+2):#有右子点
            if (self.data[i] > self.data[i * 2+2]):
                self.swap(i,i * 2+2)
                self.siftdown(i * 2 + 2)
        else:
            return #没有右边节点

    def swap(self,a,b):
        te=self.data[a]
        self.data[a]=self.data[b]
        self.data[b]=te






#
# a = [8, 3, 2, 4, 2, 6, 7, 3, 5, 3, 1, 0, 9]
# # a.append(3)
# # np.random.shuffle(a)

a=list(range(0,20))
a.append(3)
np.random.shuffle(a)
print(a)

b = heap(a)

