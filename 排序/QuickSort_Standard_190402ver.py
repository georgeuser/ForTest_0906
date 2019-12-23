#2019年4月2日14:15:10
#这个ver我修改了，比较符合背诵，以这个为准吧
import numpy as np
def quicksort(a, left, right):
    if (left >= right):  # 越界
        return

    i = left
    j = right
    key = a[left]

    while (i != j):

        while ((a[j] >= key) & (i < j)):
            j = j - 1

        while ((a[i] <= key) & (i < j)):
            i = i + 1
        if(i<j):
            te=a[i]
            a[i] = a[j]
            a[j]=te
            continue;


    te=a[i];
    a[i]=key;
    a[left]=te;


    quicksort(a, left , i-1)
    quicksort(a, i+1, right)
    return a

a=list(range(0,10))
a.append(3)
np.random.shuffle(a)

print(a)
n = len(a)

b = quicksort(a, 0, n - 1)
print (b)


