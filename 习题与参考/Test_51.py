#剑指offer Test51,我觉得我的这个dp的思路也可以
#

a = [7,5,6,4]

list_num=[0 for i in range(10)]#每个以该字母为结尾的字符串长度


for i in range(0, len(a)):

    count=0
    if(i==0):
        list_num[a[0]]=1
        continue
    list_num[a[i]]=list_num[a[i]]+1
    for j in range(a[i]+1,10):
        if(list_num[j]>0):
            count=count+list_num[j]

    print(count)
print("end")

