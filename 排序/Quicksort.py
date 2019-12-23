#这个是自制的，其实有些问题2018年12月25日21:54:41
#标答是三个while，第一个while i<j，第二个while a【j】的判断，第三个while i的判断，然后两个回归
#我这种写法，每次迭代时都迭代的数组传输，内存占得多

import numpy as np
from numpy.core.multiarray import ndarray
def fastsort(a):
    '''

    :param a:
    :return:
    '''
    i = 0;
    #j = len(a)
    if len(a) == 0:
        return
    if len(a) == 1:
        return a
    for j in range(len(a) - 1, 0, -1):
        if (a[j] < a[0]):  # 发现右边有小的了
            for i in range(i, len(a)):
                if a[i] > a[0]:
                    te = a[i]
                    a[i] = a[j]
                    a[j] = te
                    break
                if j == i:
                    te = a[0]
                    a[0] = a[j]
                    a[j] = te
                    # if (a[0:i]!=[]):
                    a[0:i] = fastsort(a[0:i])
                    # if (a[i:]!=[]):
                    a[i + 1:] = fastsort(a[i + 1:])
                    return a

    # 能运行到这，就是j=1，i=0，也就是a[1:end]都比a[0]大，这时候应该把a[0]去除，a[1:end]进入迭代

    #  if a[i:]:

    a[1:] = fastsort(a[1:])



a = np.random.rand(10)
print(a)
b = sorted(a)
print(b)
a = fastsort(a)
print(a)
