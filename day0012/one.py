# 1. 八维学院三律一值考核一直是学生管理的方法之一，班长统筹全班，学委负责班级学习，
# 书记负责文化方面内容，纪律班长控制自己班的违纪。
# 请编程实现一个投票统计程序，运行程序，分别输入“班长”，“学习委员”，“文化书记”，“纪律委员”，
# 代表投给班长、学习委员、文化书记、纪律委员一票，输入“结束”终止投票。（60分）
# 要求：
# 1.用字典来存储投票结果
# 2.循环输入计票，直到输入“结束”后终止投票。
# 3.终止投票后，输出最高得票班委及得票数
# 3.将字典内存储得票结果按得票数目倒序排列，并输出。
# 4.一票未得的，最后输出显示为“xxx  0票”
# 5.做好输入内容的错误与异常处理



a = 0
b = 0
c = 0
d = 0

while True:
    name = input("请输入一个名字:")
    if (name == '班长'):
        a += 1
    elif (name == '学习委员'):
        b += 1
    elif (name == '文化书记'):
        c += 1
    elif (name == '纪律委员'):
        d += 1
    elif (name == '结束'):
        break
    else:
        print("请输入有效的名字")

print("班长获得%d票，学习委员获得%d票，文化书籍获得%d票，纪律委员获得%d票" % (a, b, c, d))

