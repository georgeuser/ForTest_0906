#!/usr/bin/env python
# coding=utf-8
# Python使用的是3.4.3，缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用
import math
class subs:
    sublist=[]
    count=0

    def __init__(self,s,a):

        if s not in subs.sublist:
            self.str = s
            subs.sublist.append(s)
            self.count=0
            self.cal(a)
        else:
            return

    def cal(self,all):
        for i in range(0,len(all)):
            for j in range(i+1,len(all)):
                if(j-i<len(self.str)):
                    continue

                if(self.str==all[i:j]):
                    self.count=self.count+1
        if(self.count>subs.count):
            subs.count=self.count

while 1:


    #每组第一行是N和M
    nm = list(map(str,input().split(" ")))

    a = list(nm[0])
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            subs(a[i:j],a)



    print(subs.count)
