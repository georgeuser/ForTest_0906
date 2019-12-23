
'''
2018年12月27日15:35:40
这个的感受是，对list的理解加深了
list.append后接的是对象，
list.extend后接的是list
而list中这题中每个元素都是int，有时候不好比，需要[]化为list


不知道为嘛和书上答案不一致
'''
class Stack:


    def __init__(self, inlist=[]):
        self.stack = inlist
        self.pos = len(self.stack) - 1

    def Stack_In(self, inlist):

        for i in range(len(self.stack)):
            if ([self.stack[i]] == inlist):
                n = self.pos - i + 1  # 共计stackout这么多个
                ListReturn = []
                while n > 0:
                    te = self.Stack_Out()
                    ListReturn.extend(te)
                    n=n-1
                self.Stack_Print()
                return ListReturn

        self.stack.extend(inlist)
        self.pos = self.pos + len(inlist)
        self.Stack_Print()
        ListReturn = -1
        return ListReturn

    def Stack_Out(self):
        if (self.pos < 0):
            print('''空栈了,无法out''')
            return

        te=self.stack.pop(self.pos)
        self.pos = self.pos - 1
        return [te]

    def Stack_Print(self):
        print("Stack:")
        print(self.stack)
        print("Stack.Pos:")
        print(self.pos)

    def ReLastElement(self):
        return self.stack[self.pos]


class Queue:
    Qlist = list()
    head = 0
    tail = 1

    def __init__(self, inlist):
        self.Qlist = inlist
        self.head = 0
        self.tail = len(inlist)

    def Quene_Out(self):
        if (self.head == self.tail):
            print('''空队列了,无法out''')
            return

        te=self.Qlist.pop(self.head)
        # self.head = self.head + 1
        self.tail=self.tail-1
        return [te]

    def Quene_In(self, inlist):
        self.Qlist.extend(inlist)
        self.tail = self.tail + len(inlist)  # self.tail = len(self.Qlist)
        self.Quene_Print()

    def Quene_Print(self):
        print("Quene:")
        print(self.Qlist[self.head:self.tail])
        print("Quene.H&T:")
        print(self.head)
        print(self.tail)


A = Queue([2, 4, 1, 2, 5, 6])
B = Queue([3, 1, 3, 5, 6, 4])
C = Stack([])

while (A.Qlist != []) & (B.Qlist != []):

    t1 = A.Quene_Out()
    ListReturn = C.Stack_In(t1)
    if (ListReturn != -1):
        A.Quene_In(t1)
        A.Quene_In(ListReturn)


    t2 = B.Quene_Out()
    ListReturn = C.Stack_In(t2)
    if (ListReturn != -1):
        B.Quene_In(t2)
        B.Quene_In(ListReturn)

cc=1
