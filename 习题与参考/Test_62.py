# 2019年8月27日10:49:53剑指offer 面试题63
a=list([9, 11, 5, 7, 16, 1, 4, 2 ])

Last_Min=[]
Last_Max=[]
Cur_Min=0
Cur_Max=[]

for i in range(1,len(a)):
    if(a[i]==a[Cur_Min]):
        continue
    elif(a[i]<a[Cur_Min]):
        if(Cur_Min!=[] and Cur_Max!=[]):
            Last_Min=Cur_Min
            Last_Max=Cur_Max
        Cur_Min=i
        Cur_Max = []
    elif(a[i]>a[Cur_Min]):
        if(Cur_Max==[] or a[i] >a[Cur_Max]):
            Cur_Max=i
        else:
            pass
if(Cur_Min!=[] and Cur_Max!=[]):
    te=a[Cur_Max]-a[Cur_Min]

if(Last_Min!=[] and Last_Max!=[]):
    te2=a[Last_Max]-a[Last_Min]
    te=max(te,te2)
    print(te)