# 2019年8月27日10:49:53剑指offer 面试题63
a=list([9,11,8,5,6,12,16,14])

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
    print(a[Cur_Min],a[Cur_Max])
if(Last_Min!=[] and Last_Max!=[]):
    print(a[Last_Min],a[Last_Max])

    print("None")