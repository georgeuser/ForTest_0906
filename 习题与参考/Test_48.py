#剑指offer Test48
#

test = "arabcacfr"

a = list(test)



list_max=[0 for i in range(0,len(a))]#每个以该字母为结尾的字符串长度
list_aph=[-1 for i in range(26)]#每个以该字母为结尾的字符串的排列

list_seq=[[] for i in range(0,len(a))]#list_aph的集合


for i in range(0, len(a)):


    if(i==0):
        list_max[0]=1
        list_aph[ord(a[i]) - 97]=0
        list_seq[0]=list_aph
        continue


    te_p = ord(a[i]) - 97
    list_aph=list_seq[i-1]

    if(list_aph[te_p]==-1):#未出现过

        list_max[i]=list_max[i-1]+1

        list_aph[te_p] = i
        list_seq[i]= list_aph
    else:
        te_d=i-list_aph[te_p]
        if(te_d<=list_max[i-1]):
            list_max[i]=te_d
        else:
            list_max[i]=list_max[i-1]+1
        list_aph[te_p] = i
        list_seq[i]= list_aph

print(2)

