# 用python语句判断所输入的手机号，是否正确
# 要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可.判断手机号码是否是由数字组成的
#进行异常抛出（只要不是输入的数字就会抛出异常）


# 用python语句判断所输入的手机号，是否正确
phone=input("请输入一个手机号:")
#号段任意给出6个作为模拟号段即可
list = [137,182,135,184,151,158]
#try判断是否输入为字符串
try:
    #判断
    int(phone)
    #判断长度
    if(len(phone)==11):
        #截取
        head = phone[0:3]
        bool = False
        for i in list:
            if(int(head)==i):
                bool=True
                break
        #判断最后手机号是否正确
        if(bool):
            print("正确")
        else:
            print("错误")

    else:
        print("请输入正确长度的号码")
except:
    print("请输入数字作为手机号")
