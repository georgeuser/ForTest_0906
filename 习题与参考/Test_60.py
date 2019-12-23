# 2019年8月27日10:49:53剑指offer 面试题60
# 常规dp解法，个人觉得dp用class好解
class dp:
    # 常规dp求解方法，节点为avalue 和 step
    def __init__(self, avalue, step):
        self.avalue = avalue
        self.alist = list()
        if (step == 0 or avalue <= 0):
            self.alist = []
            return

        if (avalue > 0 and avalue <= 6 and step == 1):
            self.alist = [[0, 0, 0, 0, 0, 0, 0]]
            self.alist[0][avalue] = 1
            return

        for j in range(1, 7):

            te_alist = [0, 0, 0, 0, 0, 0, 0]
            te_alist[j] = 1
            if (self.avalue - j < 0):
                break
            te_dp = dp(avalue - j, step - 1)
            for k in te_dp.alist:
                te = [k[tetete] + te_alist[tetete] for tetete in range(min(len(k), len(te_alist)))]
                if (te and (te not in self.alist)):
                    self.alist.append(te)


n = 4

for i in range(n, 6 * n + 1):
    a = dp(i, n)
    print(a.alist)
