# 2019年8月27日10:49:53剑指offer 面试题58
import re

# 正则表达式：匹配内容：数字+a~z+数字，并且进行分组
pattern = r'\w'
string = "abcdefg"
a=2

ma = re.match(pattern, string)  # 可以用ma作为个判断有无的先验
if (ma):
    ta = re.findall(pattern, string)  # 返回所有的python

    s = ''
    for i in range(a, len(ta)):
        s = s + ta[i]

    for i in range(0, a):
        s = s + ta[i]
    print(s)
