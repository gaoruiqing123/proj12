# 从a到z的26个小写字母中随机生成一个长度为15的字符串，，然后从终端任意输入第二个字符串，也从a到z的26个小写字母中任意取值且可以重复取值
import random

a="abcdefghigklmnopqlstuvwxyz"
li=[random.choice(a) for i in range(15)]
st1="".join(li)
print("".join(li))
while 1:
    try:
        st2=input("请输入一个字符串:")
        for i in st2:
            if i not in a:
                raise ValueError
        else:
            break
    except ValueError:
        print("输入信息有误请重新输入")
gli=[]
nli=[]
wli1=[]
wli2=[]
# 字符串1与字符串2中共同出现的所有字符
for i in st1:
    if i in st2:
        gli.append(i)
# 从a到z均未在字符串1和字符串2中出现的字符
for i in a:
    if i not in st1 and i not in st2:
        nli.append(i)
# 在字符串1出现但未在字符串2出现的字符
for i in st1:
    if i not in st2:
        wli1.append(i)
# 在字符串2出现但未在字符串1出现的字符
for i in st2:
    if i not in st1:
        wli2.append(i)
print("共同出现的字符有", set(gli))
print("a-z均未在字符串1和字符串2中出现字符有", set(nli))
print("在字符串1出现但未在字符串2出现的字符有", set(wli1))
print("在字符串2出现但未在字符串1出现的字符是", set(wli2))