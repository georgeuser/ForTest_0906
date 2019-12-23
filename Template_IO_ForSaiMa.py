#!/usr/bin/env python
# coding=utf-8
# Python使用的是3.4.3，缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用
import math
while 1:
    te_v = 0
    LaoxiangList = [te_v for i in range(1001)]


    #每组第一行是N和M
    nm = list(map(int,input().split(" ")))
    N = nm[0]
    M = nm[1]

    # 接下来M行，每行a b c
    for i in range(M):
        abc = list(map(int,input().split(" ")))
      #  ttt=list(map(str,input().split(" ")))
        a = abc[0]
        b = abc[1]
        c = abc[2]
        if(c==1 and (a==1 or b==1 or LaoxiangList[a]==1 or LaoxiangList[b]==1)):
            LaoxiangList[a]=1
            LaoxiangList[b]=1
    count=0
    for i in range(N,1,-1):
        if LaoxiangList[i]==1:
            count=count+1
    print(count)

    ######另一种写法2019年8月26日21:47:28
    while 1:
        a = []
        s = input()

        if s != "":
            for x in s.split():
                a.append(int(x))

            print(sum(a))
        else:
            break