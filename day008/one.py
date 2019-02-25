# 1. 编写函数，判断输入参数字符串是否为邮箱地址，检验条件为：
# 字符串中间用@分隔，末尾是.com或者.net（40分）


str = input("请输入一个邮箱:")
# print(type(str))
if(type(str)=='str'):
    print("输入正确")
else:
    print("输入错误")