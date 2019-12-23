import re
text = 'c++ python2 python3 perl ruby lua java javascript php4 php5 c'

#match,search,findall,split,sub
a=re.match(r'java',text)#只找头，没有的话返回none 返回一个<_sre.SRE_Match object; span=(34, 38), match='java'>

b=re.search(r'java',text)#从头开始找，找符合的字符
# <_sre.SRE_Match object; span=(34, 38), match='java'>

c=re.match(r'c\++',text),re.match(r'c\+\+',text)#作用相同
#<_sre.SRE_Match object; span=(0, 3), match='c++'>

d=re.findall(r'python',text) #返回所有的python
# ['python', 'python']

e=re.split(r' perl ',text)#以某个字符为中心拆分
#['c++ python2 python3', 'ruby lua java javascript php4 php5 c']

f=re.sub(r'ruby','fortran',text) #替换某个字符
#'c++ python2 python3 perl fortran lua java javascript php4 php5 c'
print(2)
