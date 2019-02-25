# 2.编写函数求三角形面积，输入参数为底边与高，输出面积（20分）


import math

def ssm(c,d):

    print("您输入的三角形面积是:", (c * d) / 2)


a = int(input("请输入三角形的底边数字:"))
b = int(input("请输入三角形的高数字:"))
ssm(a , b)