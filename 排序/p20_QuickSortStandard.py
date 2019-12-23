#
class book:
    bnum = 0
    blist = list()

    def __init__(self, issn):
        self.issn = issn
        book.bnum = book.bnum + 1
        book.blist.append(issn)

    def bookprint(self):
        print(book.bnum)
        print(book.blist)


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
    quicksort(a, left, i - 1)
    quicksort(a, i + 1, right)
    return a


a = [0, 2, 5, 4, 0, 9, 9, 9, 5, 9, 4, 1, 0,7 ,11,21, 5, 3, 1, 5, 0, 9, 9, 9, 5, 9, 4, 1, 0, 5, ]
n = len(a)

b = quicksort(a, 1, n - 1)
print (b)

for i in range(1, len(b)):
    if (b[i] != b[i - 1]):
        t = book(b[i])

t.bookprint()
c = 2
