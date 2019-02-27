# 2.读入文件‘a.txt’.统计文件中每个单词的数量并且进行输出。

import os

#读文件

f = open("a.txt", "r")
d = f.read()
#切割字符串
c = d.split(" ", 100)
print("切割字符串为:", c)

#定义一个次数

count = 0

#循环字符串

for i in range(len(c)):
    count += 1

print("一共有:%d个单词" % count)

