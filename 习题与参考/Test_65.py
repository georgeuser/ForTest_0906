# 2019年8月27日10:49:53剑指offer 面试题65
#15.43-16.19,36分钟
#构思思路
#先判断最大的数最大的幂次
#然后按位运算(考虑up_sign)，这一部分设个函数，sum=sum^新的单位运算

a=24
b=13
def find_n(a):
    N=0

    while 1:
        if((a>>1)==0):
            break
        else:
            a=a>>1
            N=N+1
    return N+1
done=0
j=1
sum=0
up_sign=0

N=find_n(max(a,b))
while not done:

    te=0
    te_a=((a>>j)<<1)^(a>>j-1)
    te_b=((b>>j)<<1)^(b>>j-1)



    if(up_sign==0):
        if(te_a==1 and te_b==1):
            up_sign=1
            te=0
        else:
            up_sign=0
            te=te_a^te_b#这里异或没有错，0^0=0
    else:
        if(te_a ==0 and te_b==0):
            up_sign=0
            te=1
        else:
            up_sign=1
            te=te_a^te_b^1

    sum=sum|(te<<(j-1))
    j=j+1

    if( j>N+3):
        done=1
        break


print(sum)