'''
Test 47



 '''
a = list([[9, 12, 15, 10],[6, 8, 2, 18],[9, 5,0,1]])
m=len(a)
n=len(a[0])

ta=[[0 for i in range(n)] for j in range(m)]

def func(i,j):
    if(i==0 and j==0):
        ta[i][j]=a[0][0]
        ta[i][j+1] = ta[i][j]+a[i][j+1]
        ta[i+1][j] = ta[i][j]++a[i+1][j]

        func(i+1,j)
        func(i,j+1)
        return
    t1=0
    t2=0
    if( j+1<=n-1):
        t1 = 1
        te=ta[i][j] + a[i][j + 1]
        if(te>ta[i][j + 1]):
           ta[i][j + 1] = ta[i][j] + a[i][j + 1]

    if (i+ 1 <=m-1):

        te= ta[i][j] + +a[i + 1][j]
        if(te>ta[i][j + 1]):
            ta[i + 1][j] = ta[i][j] + +a[i + 1][j]
    func(i, j + 1)
    func(i + 1, j)

ta[0][0]=a[0][0]
for i in range(1,n):
    ta[0][i]=ta[0][i-1]+a[0][i]
for i in range(1, m):
    ta[i][0] = ta[i - 1][0] + a[i][0]

lastpoint_list=[[1,1]]
newpoint_list=[[]]
for i in range(1,max(n,m)+1):
    lastpoint_list=newpoint_list
    newpoint_list = []
    if(i==1):
        ta[i][i]=max(ta[i-1][i],ta[i][i-1])+a[i][i]
        newpoint_list = [[1,2],[2,1]]
        continue
    for j in lastpoint_list:
        t_i=j[0]
        t_j=j[1]
        ta[t_i][t_j] = max(ta[t_i-1][t_j], ta[t_i][t_j-1]) + a[t_i][t_j]
        if [t_i+1,t_j] not in newpoint_list and t_i+1<m:
            newpoint_list.append([t_i+1,t_j] )

        if [t_i, t_j + 1] not in newpoint_list and t_j+1<n:
            newpoint_list.append([t_i, t_j + 1])


print(ta)