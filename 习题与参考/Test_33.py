'''
Test 33



 '''
a = list([9, 12, 15, 10, 6, 8, 2, 18, 9, 5])


class dp:
    ta = [0 for i in range(len(a))]
    plist = [0 for i in range(len(a))]

    def __init__(self, i, step):
        self.i = i
        dp.plist[i] = self
        if (i == 0):
            dp.ta[0] = a[0]
            self.tr = list([a[0]])
            dp.ta[0] = a[0]
            return
        te_fn = 0
        if (i % 2 == 1):  # 左子点
            te_fn = int((i - 1) / 2)
        else:  # 左子点
            te_fn = int((i - 2) / 2)
        te=dp.plist[te_fn].tr.copy()
        te.append(a[i])
        self.tr = te
        dp.ta[i] = sum(self.tr)


t0 = dp(i=0, step=1)
step = 1
for i in range(1, len(a)):
    if (i == int((step + 1) * step / 2)):
        step = step + 1
    dp(i=i, step=step)

print(dp.ta)

