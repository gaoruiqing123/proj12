# 4．编写一个函数，判断一个字符串是否为回文，如果是回文返回整数1，否则返回返 回整数0（20分）
# 	回文：就是前后对称。例如：”abba”，”evilolive”是回文，”abxd”和”efga”不是回文。

import os
def fun(a):
    flag = True
    c = sorted(a)
    d = c[::-1]

    for i in range(len(c)):
        if c[i] == d[i]:
            flag = False
        else:
            flag = True

    if flag!=True:
        print("不是回文")
    else:
        print("是回文")



str = input("请输入一个字符串:")
fun(str)