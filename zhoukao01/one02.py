# 用python语句判断所输入的手机号，是否正确
# 要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可.判断手机号码是否是由数字组成的
#进行异常抛出（只要不是输入的数字就会抛出异常）

# 用python语句判断所输入的手机号，
#输入手机号
phone = input("请输入手机号:")
list = [182,137,158,184,151,139]
#判断手机号是否是数字
try:
    #转型
    int(phone)
    #判断长度
    if(len(phone)==11):
        #截取前三
        head = phone[0:3]
        bool = False
        for i in list:
            if(int(head)==i):
                bool = True
                break
        if(bool):
            print("正确")
        else:
            print("错误")
    else:
        print("长度有误")
except:
    print("请输入数字")