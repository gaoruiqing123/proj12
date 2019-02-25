# 2.编写程序，包含try…except…else …finally各个分支内语句,通过调用测试每个分支运行正确（20分）


try:
    str = int(input("请输入一个数字:"))
    print("您输入对了")
except:
    print("您输入的不是数字")
else:
    print("您可能输入有误")
finally:
    print("不管怎么都会执行")

