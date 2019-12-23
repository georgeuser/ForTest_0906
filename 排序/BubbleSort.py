a=[1,3,5,7,2,3,324,4]
for i in range(0,len(a)-1):
    for j in range(0,len(a)-i-1):
        if(a[j]>a[j+1]):
            te=a[j]
            a[j]=a[j+1]
            a[j+1]=te
        else:
            pass

print(a)
