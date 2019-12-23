class book:
    bnum = 0
    blist = []

    def __init__(self, issn):
        self.issn = issn
        bnum = bnum + 1
        blist = blist.append(issn)

    def bookprint(self):
        print(blist)

import numpy as np
def quicksort(a, left, right):
    if (left >= right):  # 越界
        return

    i = left
    j = right
    key = a[left]

    while (i < j):

        while ((a[j] >= key) & (i < j)):
            j = j - 1
        a[i] = a[j]
        while ((a[i] <= key) & (i < j)):
            i = i + 1
        a[j] = a[i]

    a[i] = key
    quicksort(a, left , i-1)
    quicksort(a, i+1, right)
    return a

a = np.random.rand(15)
print(a)
n = len(a)

b = quicksort(a, 1, n - 1)
print (b)


