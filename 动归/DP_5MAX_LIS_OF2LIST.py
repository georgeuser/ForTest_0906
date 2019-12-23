#5.最长公共子序列(LCS)

#一个序列 S ，如果分别是两个或多个已知序列的子序列，且是所有符合此条件序列中最长的，则 S 称为已知序列的最长公共子序列。


def dp_all(pos_i,pos_j):
    if (pos_i == 0 and pos_j==0):
        if(a[pos_i]==b[pos_j]):
            re[pos_i][pos_j]=1
            return 1
        else:
            re[pos_i][pos_j]=0
            return 0
    if (pos_i < 0 or pos_j < 0):
        return 0


    i=pos_i
    j=pos_j

    if(i>=0 and j>=0):
        if(a[i]!=b[j]):
            return 0
        else:

            re[pos_i][pos_j] = re[pos_i - 1][ pos_j - 1] + 1
            '''    if(re[pos_i-1][pos_j-1]==-1):
                     re[pos_i][pos_j]=dp_all(pos_i-1,pos_j-1)+1
            '''

    '''  
   等同于 
        else:
            i=i-1
            j=j-1
          #  re[i][j]=1
            re[pos_i][pos_j]= re[pos_i][pos_j]+1

   '''


    return  re[pos_i][pos_j]




a = list([1, 3, -5, 2, 1, 5, 6,-7, 6,3, 3])
b = list([7, 3, -5, 6, 3,3])


re=[[0 for t in range(len(b))] for i in range(len(a))]





for i  in range(len(a)):
    for j in  range(len(b)):
        dp_all(i,j)
te=0
for i in range(len(a)):
    if(max(re[i])>te):
        te=max(re[i])
print(te)
