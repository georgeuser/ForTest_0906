# 用python写这个题，以骰子为例
# 骰子可能的组合数设为list([1,2,3,4,5,6])
# 次数设为 int n
# Sum或value对应设为list([])[暂时不考虑下标溢出问题]，对应的sum[i]也是一个list，这个list中是一串数字（按顺序，n个）的集合，表示结果为i下的骰子从1至n次的结果集合。也就是说是个三维list，生成2维list，然后append进list元素变为三维list
# 至此可以用函数(参量：当前n次，上一次sum结果)实现了，如果用class，建议用在n和sum都没给定的情况下，这时class为函数结果的集合，对应的index就是n和sum
# 2019年8月29日12:28:00用class而言，就定n就可以了。然后将上一轮的结果指针代入

#2019年8月30日09:38:16其实这个本质上，也是dp
#2019年8月30日10:40:36这个就是dp，只不过是从下往上的思考流程

# 用python写这个题，以骰子为例
# 骰子可能的组合数设为list([1,2,3,4,5,6])
# 次数设为 int n
# Sum或value对应设为list([])[暂时不考虑下标溢出问题]，对应的sum[i]也是一个list，这个list中是一串数字（按顺序，n个）的集合，表示结果为i下的骰子从1至n次的结果集合。也就是说是个三维list，生成2维list，然后append进list元素变为三维list
# 至此可以用函数(参量：当前n次，上一次sum结果)实现了，如果用class，建议用在n和sum都没给定的情况下，这时class为函数结果的集合，对应的index就是n和sum
# 2019年8月29日12:28:00用class而言，就定n就可以了。然后将上一轮的结果指针代入

# 2019年8月30日09:38:16其实这个本质上，也是dp
# 2019年8月30日10:40:36这个就是dp，只不过是从下往上的思考流程


class func:
    a = list([1, 2, 3, 4, 5, 6])

    def __init__(self, n, Obj_lt=[]):
        assert n > 0, 'Error'
        self.n = n
        self.sumlist = [0 for i in range(n * len(func.a) + 1)]
        self.unisumlist = [0 for i in range(n * len(func.a) + 1)]
        for i in range(len(self.sumlist)):
            self.sumlist[i] = []
        if (n == 1):
            for i in range(len(func.a)):
                te = [func.a[i]]
                self.sumlist[func.a[i]] = [te]
            return
        if (Obj_lt.n + 1 != self.n):
            print('Error last Obj')
            return

        for j in func.a:
            for k in range(len(Obj_lt.sumlist)):
                if (Obj_lt.sumlist[k] == []):
                    continue
                for t in Obj_lt.sumlist[k]:
                    if (type(t) == list):
                        te = t.copy()
                    else:
                        te = list([t])
                    te.append(j)
                    te_sum = k + j
                    self.sumlist[te_sum].append(te)

    def CountSomeSumTimes(self, n):  # 计算和结果为n的出现次数，这个是排列，有顺序的次数（依次1，2,1和2,1,1不等）
        k = 0
        if (n > self.n * len(func.a) or n < self.n * func.a[0]):
            print('CountSomeSumTimes:N is out of range:too large or small')
            return -1
        if (self.sumlist[n] == []):
            pass
        else:
            k = len(self.sumlist[n])

        # print('CountSomeSumTimes:Times {k} '.format( k=k))
        return k

    def CountSomeSumWaysUnique(self, n):  # 计算和结果为n出现次数中各个a分量用的不同的次数，也就是组合（依次1,2,1和2,1,1和1,1,2等）
        k = 0
        if (n > self.n * len(func.a) or n < self.n * func.a[0]):
            print('N is out of range:too large or small')
            return -1
        if (self.sumlist[n] == []):
            return k

        unilist = list()

        for i in self.sumlist[n]:
            te = [0 for i in range(len(func.a) + 1)]
            for j in i:
                te[j] = te[j] + 1
            if te not in unilist:
                unilist.append(te)

        self.unisumlist[n] = unilist
        print('CountSomeSumWaysUnique: {k1} when n={k2} at self.n={k3} '.format(k1=len(unilist), k2=n, k3=self.n))
        return len(unilist)

        # print('Times {k} '.format( k=k))

    def CountSomeSumTimesPercenTage(self, n):
        Per = 0
        if (n > self.n * len(func.a) or n < self.n * func.a[0]):
            print('CountSomeSumTimesPercenTage:N is out of range:too large or small，not happened')
            return -1
        re_n = self.CountSomeSumTimes(n)
        re_all = 0
        for i in range(self.n * func.a[0], self.n * len(func.a) + 1):
            re_all = re_all + self.CountSomeSumTimes(i)
        if (re_all == 0):
            print('Error')
            return -1

        Result = re_n / re_all
        print('CountSomeSumTimesPercenTage:Times {k1} of {k2},{k3} '.format(k1=re_n, k2=re_all, k3=Result))
        return Result

    def FindMostWays_Sum(self, value):
        if (self.sumlist[value] == []):
            return False
        else:
            return True


times = 5

n = 2
t1 = func(1)
t1.CountSomeSumTimesPercenTage(3)
t2 = func(2, t1)
t2.CountSomeSumTimesPercenTage(7)
t2.CountSomeSumWaysUnique(8)
t3 = func(3, t2)
t3.CountSomeSumTimesPercenTage(14)
t3.CountSomeSumWaysUnique(14)
print(3)
