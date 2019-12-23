#剑指offer 2019年9月10日16:14，面试题31
#测试用例
#除了标准外，
#stack_ou长度>stack_in长度肯定错，<=有可能对
#stack_in空队列
#stack_ou空队列
#stack_ou中出现了stack_in中没有的元素
#1标准用例
stack_in=[1,2,3,4,5]
stack_ou=[4,5,3,2,1]



assisst_st1=[]#表征当前的stack里面的东西
assisst_st2=stack_in#表征还未使用的队列

for i in range(len(stack_ou)):
    if(i==0 and stack_in!=[]):
        te=stack_in.index(stack_ou[0])
        assisst_st1=stack_in[0:te]
        assisst_st2=stack_in[te+1:]
        continue
    if(assisst_st1!=[] and stack_ou[i]==assisst_st1[-1]):
        assisst_st1.pop()
        continue
    elif(assisst_st2!=[] and stack_ou[i]==assisst_st2[0]):
        assisst_st2.pop(0)
        continue
    else:
        print("Not possible")
        break


