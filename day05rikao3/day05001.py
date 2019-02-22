# 1. 通过用户输入数字，计算阶乘。（30分）

num = int(input("请输入一个数字:"))

sum = 1
for i in range(1,num+1):
    sum*=i

print("您输入的%d的阶乘是:%d"%(num,sum))