import numpy as np
Cards=np.ones(9)
Cards_cp=list(np.zeros(9))
Cards_pos=np.zeros(9)
count = 0

'''
解决的问题是XXX+YYY=ZZZ，0~8的数字分别列入，如何得出等式及个数
深度优先搜索
·dfs(状态) [3] 
–if 状态 是 目标状态then
·dosomething
–else
·for 每个新状态
–if 新状态合法
»dfs(新状态)
·主程序：
·dfs(初始状态)


'''

def dfs(step):
    #边界与判断
    if(step==len(Cards)):#已经完成了一次搜索

        if (list(Cards)==Cards_cp):
            t1=Cards_pos[0]*100+Cards_pos[1]*10+Cards_pos[2]
            t2 = Cards_pos[3] * 100 + Cards_pos[4] * 10 + Cards_pos[5]
            t3= Cards_pos[6] * 100 + Cards_pos[7] * 10 + Cards_pos[8]
            if((t1+t2 )==t3):
                 print(Cards_pos)
                 global count
                 count = count+1
            return
        else:
            return

    #循环找节点与迭代
    for i in range(0,len(Cards)):
        if(Cards[i]==1):
            Cards_pos[step]=i
            Cards[i] =0

            dfs(step+1)
            Cards[i] = 1  #回溯到这时节点重置
            Cards_pos[step] = -1



dfs(0)
print("------count")
print(count/2)

