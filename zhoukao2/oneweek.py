# 1.生成50个范围在0-80的整数，并且能够打印输出？

import random

#定义一个空列表

list = []

#循环输出题目要求

for i in range(50):
    list.append(random.randint(0,80))

#输出随机数
print("随机数为", list)
print("0---80之间的随机数:%d个" %len(list))