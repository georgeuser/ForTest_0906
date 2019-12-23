import numpy as np
import pandas as pd
import copy



excelFile = r'a.xlsx'
map= pd.DataFrame(pd.read_excel(excelFile))




class N:

    ps = set()#点集合
    point_sum = 0
    start="6,8"

    te2 = np.zeros([10, 10])
    map2show = pd.DataFrame(te2)
    del te2



    # def ins(self,a,s):
    #     if(s<0):
    #         return
    #
    #     N.track[s]=a.pos
    #     self.ins(a.forward,s-1)
    #
    # def generate_track(self, step):
    #     # N.track[step, 1]=self.pos
    #     self.ins(self,step)

    def printdata(self):
        print(N.map2show)


    def __init__(self, x, y, step,forwardN=None):
        self.forward = forwardN
        self.step=step
        self.pos = "{x},{y}".format(x=x,y=y)

        self.x = x
        self.y = y
        self.nx = 0
        self.ny = 0
        if(self.pos not in N.ps) :
            N.ps.add(self.pos)
            N.point_sum= N.point_sum+1
            N.map2show.values[self.x,self.y]=9


def Func_runperpoint(a,step,pointpointer_currentstep):

    for j in range(0,4):#分别从2个方向判断是否有可能，本题从左上开始，只能右或下寻找
        if( Func_goahead(a,j)):#如果可以这点可以+上
            te=N(a.nx,a.ny, step,forwardN=a)#生成了新的点
            pointpointer_currentstep.append(te)


    return pointpointer_currentstep



def Func_runperstep(step, ps_pointer):
    ps_currentstep = set()
    pointpointer_currentstep = list()


    for i in ps_pointer:
         Func_runperpoint(i, step,  pointpointer_currentstep)


    ps_pointer=pointpointer_currentstep
    return ps_pointer



def Func_goahead(a,i):
        if (i == 0):
            a.nx = a.x
            a.ny = a.y + 1


        if (i == 1):
            a.nx = a.x + 1
            a.ny = a.y

        if (i == 2):
 
            a.nx = a.x
            a.ny = a.y - 1

        if (i == 3):
 
            a.nx = a.x - 1
            a.ny = a.y



        point_te="{x},{y}".format(x=a.nx,y=a.ny)
        if ((a.nx < 0) | (a.ny < 0) | (a.nx > 9) | (a.ny > 9)):  # 走出地图了
            return 0
        if (map.values[a.nx, a.ny] ==0):#地图障碍了
            return 0
        if point_te in N.ps :#已经生成过这个点了
            return 0

        return 1

        #########################main 部分

step=0
a0=N(x=6, y=8, step=0)
te3 = np.zeros([20, 20])#当前路径集合，估计最多14step
# ps_set = pd.DataFrame(te3)  # 路径集合
# # ps_set.values[0,0]=start

ps_pointer=list()             #每step的点的指针集合,这个不一样的是只是本层的
ps_pointer.append(a0)

# while terminal not in ps_perstep:
while ps_pointer:
    step=step+1
    # Func_run(step,ps_set,ps_pointer)#这个会把N.track弄满
    ps_pointer=Func_runperstep(step, ps_pointer)
#到这时应该N.track满了，找到路径了，输出路径


N.printdata(a0)