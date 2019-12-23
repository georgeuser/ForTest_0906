#复杂str的字母提取

test={"a":["b","c","d"],"b":["a","d"],"c":["d"]}
t=test.split("],")
for i in range(0,len(t)):
    te=list(t[i])
    te2=""
    for j in range(0,len(te)):
        if te[j] not in {'"','{',',',':','[',']','}'}:
             te2=te2+te[j]
    t[i]=te2

print(t)