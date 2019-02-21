# 用python语句判断所输入的手机号，是否正确
# 要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可.判断手机号码是否是由数字组成的
#进行异常抛出（只要不是输入的数字就会抛出异常）

# 用python语句判断所输入的手机号，

phone = input("请输入一个手机号:")
list = [182,137,158,184,151,172]
try:
    #判断手机号
    int(phone)
    #长度
    if(len(phone)==11):
        #截取
        head = phone[0:3]
        bool = False
        for i in list:
            if(int(head)==i):
                bool = True
                break
        if (bool):
            print("有效")
        else:
            print("无效")
    else:
        print("请输入正确手机号长度")



except:
    print("请输入正确的数字")
