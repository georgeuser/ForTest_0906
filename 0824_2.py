
N = 3
M =3
Di =list([1,2,3])
Pi =list([2,3,4])
INPUT_LINE=list([list([1,2,3])])
print(2)

ans=list()

for i in INPUT_LINE:
    maxPro_te=0
    for j in i:
        for k in range(0,len(Di)):
            if(j>=Di[k] and Pi[k]>maxPro_te):
                maxPro_te=Pi[k]
        ans.append(maxPro_te)
print(ans)