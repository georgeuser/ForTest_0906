import numpy as np
import pandas as pd

te2 = np.zeros([5, 4])
map = pd.DataFrame(te2)

map.values[0, 2] = 1
map.values[2, 2] = 1
map.values[3, 1] = 1
map.values[4, 3] = 1


class M:
    startx = 0
    starty = 0
    terminalx = 3
    terminaly = 2

    def __init__(self, startx=0, starty=0, terminalx=3, terminaly=2):
        M.terminalx = terminalx
        M.terminaly = terminaly
        M.startx = startx
        M.starty = starty

        self.cx = self.startx
        self.cy = self.starty

        self.nx = -1
        self.ny = -1

        # self.trackx = np.zeros(15)
        # self.tracky = np.zeros(15)

        self.oncedirect = -1
        self.direct = -1

        te = np.zeros([20, 4])
        self.track = pd.DataFrame(te, columns=list(['x坐标', 'y坐标', '前进方向', '来时方向']))

    def Func_goahead(self, i, step):
        if (i == 0):
            if (self.oncedirect == 2):
                return 0
            self.nx = self.cx
            self.ny = self.cy + 1

        if (i == 1):
            if (self.oncedirect == 3):
                return 0
            self.nx = self.cx + 1
            self.ny = self.cy

        if (i == 2):
            if (self.oncedirect == 0):
                return 0
            self.nx = self.cx
            self.ny = self.cy - 1

        if (i == 3):
            if (self.oncedirect == 1):
                return 0
            self.nx = self.cx - 1
            self.ny = self.cy

        if ((self.nx < 0) | (self.ny < 0) | (self.nx > 4) | (self.ny > 3)):  # 走出地图了
            return 0
        if (map.values[self.nx, self.ny] > 0):
            return 0

        self.direct = i

        return 1


def dfs(a, step):
    # 先判断边界条件
    if(step>0):
        a.oncedirect = a.direct
        a.cx = a.nx
        a.cy = a.ny


    if (step >= 16):
        return
    # 发现终点
    if ((a.cx == a.terminalx) and (a.cy == a.terminaly)):


        a.track.values[step, 0] = a.cx
        a.track.values[step, 1] = a.cy
        a.track.values[step, 2] = -1
        a.track.values[step, 3] = a.oncedirect

        print("Found 1 track：")
        print(step)
        for i in range(0, step + 1):
            # if (a.trackx[i] == 0):
            #     break
            str = "({x},{y})=>".format(x=int(a.track.values[i, 0]), y=int(a.track.values[i, 1]))
            print(str, end=' ')
        print('Next:')
        return

    for i in range(0, 4):
        # i=0,向右

        t = a.Func_goahead(i, step)
        if (t):
            # save 当前节点
            a.track.values[step, 0] = a.cx
            a.track.values[step, 1] = a.cy
            a.track.values[step, 2] = a.direct
            a.track.values[step, 3] = a.oncedirect



            dfs(a, step + 1)

            a.cx = int(a.track.values[step, 0])
            a.cy = int(a.track.values[step, 1])
            a.direct = int(a.track.values[step, 2])
            a.oncedirect = int(a.track.values[step, 3])
            a.track.values[step + 1, 0] = 0
            a.track.values[step + 1, 1] = 0
            a.track.values[step + 1, 2] = -1
            a.track.values[step + 1, 3] = -1


a = M()
dfs(a, 0)
