import numpy as np
import pandas as pd
import copy

excelFile = r'b.xlsx'
map = pd.DataFrame(pd.read_excel(excelFile))  # 管道类型

# te2 = np.zeros([4, 3])
# map_tube2place = pd.DataFrame(te2)  # 管道放置地图
map_tube2place = [list(['', '', '', '']) for _ in range(5)]

L2R_1 = '━'
U2D_1 = '┃'

L2D_2 = '┓'
L2U_2 = '┛'
R2D_2 = '┏'
R2U_2 = '┗'


class TubeForest:
    PointsSet = set()  # 点集合
    PointsSum = 0
    m_start = "0,0"
    m_termin = "4,3"

    # del te2

    def __init__(self, x, y, step, forwardN=None):
        self.forward = forwardN
        self.x = x
        self.y = y
        self.nx = 0
        self.ny = 0

        self.inDirect = 9
        self.outDirect = 9
        self.pos = "{x},{y}".format(x=self.x, y=self.y)

        self.tubetype = map.values[x, y]
        self.tubeplace = []

        self.step = step
        if forwardN is not None:
            self.Func_CalinDirect(forwardN.outDirect)
        if (self.pos not in TubeForest.PointsSet):
            TubeForest.PointsSet.add(self.pos)

    def Func_NextDir_forTubeTypeI(self):
        if (self.inDirect == 3):  # 从上边来的，到下边
            t = list([1])
            self.tubeplace = U2D_1
        if (self.inDirect == 2):  # 从左边来的，到右边
            t = list([0])
            self.tubeplace = L2R_1
        if (self.inDirect == 1):  # 从下边来的，到上边
            t = list([3])
            self.tubeplace = U2D_1
        if (self.inDirect == 0):  # 从右边来的，到左边
            t = list([2])
            self.tubeplace = L2R_1

        self.outDirect = int(t[0])
        return t

    def Func_goahead_forTubeTypeI(self, i):#i是去向，outDirect

        if (i == 0):  # 从左边来的，到右边
            self.nx = self.x
            self.ny = self.y + 1

            point_te = "{x},{y}".format(x=self.nx, y=self.ny)

            if ((self.nx < 0) | (self.ny < 0) | (self.nx > 4 | (self.ny > 3) | (map.values[self.nx, self.ny] == 0))):
                return 0
            if point_te in TubeForest.PointsSet:  # 已经生成过这个点了
                return 0

            self.inDirect=2
            self.outDirect=0
            return 1

        if (i == 1):  # 从上边来的，到下边
            self.nx = self.x+1
            self.ny = self.y
            point_te = "{x},{y}".format(x=self.nx, y=self.ny)

            if ((self.nx < 0) | (self.ny < 0) | (self.nx > 4 | (self.ny > 3) | (map.values[self.nx, self.ny] == 0))):
                return 0
            if point_te in TubeForest.PointsSet:  # 已经生成过这个点了
                return 0
            self.inDirect=3
            self.outDirect=1
            return 1
        if (i == 2):  # 从右边来的，到左边
            self.nx = self.x
            self.ny = self.y - 1
            point_te = "{x},{y}".format(x=self.nx, y=self.ny)

            if ((self.nx < 0) | (self.ny < 0) | (self.nx > 4 | (self.ny > 3) | (map.values[self.nx, self.ny] == 0))):
                return 0
            if point_te in TubeForest.PointsSet:  # 已经生成过这个点了
                return 0
            self.inDirect=0
            self.outDirect=2
            return 1

        if (i == 3):  # 从下边来的，到上边
            self.nx = self.x - 1
            self.ny = self.y
            point_te = "{x},{y}".format(x=self.nx, y=self.ny)


            if ((self.nx < 0) | (self.ny < 0) | (self.nx > 4) | (self.ny > 3)):
                return 0
            if ((map.values[self.nx, self.ny] == 0)):
                return 0

            if point_te in TubeForest.PointsSet:  # 已经生成过这个点了
                return 0
            self.inDirect=1
            self.outDirect=3
            return 1

    def Func_NextDir_forTubeTypeII(self):
        if (self.inDirect == 3):  # 从上边来的，到左右
            t = list([0, 2])
        # self.tubeplace=U2D_1
        if (self.inDirect == 2):  # 从左边来的，到上下
            t = list([1, 3])
        # self.tubeplace = L2R_1
        if (self.inDirect == 1):  # 从下边来的，到左右
            t = list([0, 2])
        #   self.tubeplace = U2D_1
        if (self.inDirect == 0):  # 从右边来的，到上下
            t = list([1, 3])
        #   self.tubeplace = L2R_1

        # self.outDirect=t
        return t

    def Func_goahead_forTubeTypeII(self, inDir, outDir):

        if ((inDir == 3)):  # 从上边来的，到左右
            if (outDir == 0):
                self.nx = self.x
                self.ny = self.y + 1
                self.tubeplace = R2U_2

            if (outDir == 2):
                self.nx = self.x
                self.ny = self.y - 1
                self.tubeplace = L2U_2

        if ((inDir == 2)):  # 从左边来的，到上下
            if (outDir == 3):
                self.nx = self.x - 1
                self.ny = self.y
                self.tubeplace = L2U_2
            if (outDir == 1):
                self.nx = self.x + 1
                self.ny = self.y
                self.tubeplace = L2D_2
        if ((inDir == 1)):  # 从上边来的，到左右
            if (outDir == 2):
                self.nx = self.x
                self.ny = self.y - 1
                self.tubeplace = L2D_2
            if (outDir == 0):
                self.nx = self.x
                self.ny = self.y + 1
                self.tubeplace = R2D_2

        if ((inDir == 0)):  # 从上边来的，到左右
            if (outDir == 3):
                self.nx = self.x - 1
                self.ny = self.y
                self.tubeplace = R2U_2
            if (outDir == 1):
                self.nx = self.x + 1
                self.ny = self.y
                self.tubeplace = R2D_2
        point_te = "{x},{y}".format(x=self.nx, y=self.ny)

        if ((self.nx < 0) | (self.ny < 0) | (self.nx > 4) | (self.ny > 3)):
            return 0
        if ((map.values[self.nx, self.ny] == 0)):
            return 0
        if point_te in TubeForest.PointsSet:  # 已经生成过这个点了
            return 0
        self.inDirect=inDir
        self.outDirect=outDir
        return 1

    def Func_CalinDirect(self, i):
        if (i == 2):
            self.inDirect = 0
        if (i == 0):
            self.inDirect = 2
        if (i == 3):
            self.inDirect = 1
        if (i == 1):
            self.inDirect = 3

    def Dfs(self, x, y, step, Tem):
        a = self
        if (step > 0):
            a = TubeForest(x, y, step, forwardN=Tem)
            # a.inDirect = a.Func_CalinDirect(Tem.outDirect)
            a.Func_CalinDirect(Tem.outDirect)
        # 1.边界条件,到了最后的点
        if a.pos == TubeForest.m_termin:
            if map.values[4, 3] == 1:
                if a.forward.pos == "4,2":
                    a.tubeplace = L2R_1
                    map_tube2place[a.x][a.y] = a.tubeplace
                    print("TubePlacementRoute Found")
                    # for i in range
                    for i in range (0,map_tube2place.__len__()):
                        print(map_tube2place[i])
                    TubeForest.PointsSet.discard(a.pos)
                    return

            if map.values[4, 3] == 2:
                if a.forward.pos == "3,3":
                    a.tubeplace = R2U_2
                    map_tube2place[a.x][a.y] = a.tubeplace
                    print("TubePlacementRoute Found")
                    for i in range (0,map_tube2place.__len__()):
                        print(map_tube2place[i])
                    TubeForest.PointsSet.discard(a.pos)
                    return

        # 2.遍历可能的选择
        if a.tubetype == 1:  # 直棍，只有一种选择
            t = a.Func_NextDir_forTubeTypeI()  # t是去向，#生成去向

            for i in t:
                flag = a.Func_goahead_forTubeTypeI(i)#生成indir，outdir
                a_backup = copy.deepcopy(a)

                if (flag):
                    map_tube2place[a.x][a.y] = a.tubeplace

                    a.Dfs(a.nx, a.ny, step + 1, a)
                    #回归
                    TubeForest.PointsSet.discard(a.pos)
                    map_tube2place[a.x][a.y] = ''
                    a = a_backup

        if a.tubetype == 2:  # 曲棍，两种选择
            t = a.Func_NextDir_forTubeTypeII()

            for i in t:
                flag = a.Func_goahead_forTubeTypeII(a.inDirect, i)
                if (flag):
                    map_tube2place[a.x][a.y] = a.tubeplace
                    a_backup = copy.deepcopy(a)

                    a.Dfs(a.nx, a.ny, step + 1, a)
                    # 回归
                    TubeForest.PointsSet.discard(a.pos)
                    map_tube2place[a.x][a.y]=''
                    a = a_backup

    #########################main 部分


#
# step = 0
# a0 = N(x=6, y=8, step=0)
# te3 = np.zeros([20, 20])  # 当前路径集合，估计最多14step
# # ps_set = pd.DataFrame(te3)  # 路径集合
# # # ps_set.values[0,0]=start
#
# ps_pointer = list()  # 每step的点的指针集合,这个不一样的是只是本层的
# ps_pointer.append(a0)

if map.values[0, 0] == 1:
    a0 = TubeForest(0, 0, 0, None)

    a0.tubeplace = L2R_1
    a0.inDirect = 2

    a0.Dfs(0, 0, 0, None)
    c=2

if map.values[0, 0] == 2:
    a1 = TubeForest(0, 0, 0, None)

    a1.tubeplace = L2D_2
    a1.inDirect = 2

    a1.Dfs(0, 0, 0, None)
    c=2